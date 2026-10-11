#!/usr/bin/env python3
"""Plan, verify, and copy NEF/JPEG originals. No conversions or cloud mutations."""
from decimal import Decimal
import argparse
import copy
import datetime
import glob
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

LEDGER = 'camera-import-ledger.json'
EXTENSIONS = {'.NEF', '.JPG', '.JPEG'}

def digest(path):
    h = hashlib.sha256()
    with open(path, 'rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def save_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)

def load_ledger(project):
    project = Path(project)
    if (project / LEDGER).exists():
        ledger = json.loads((project / LEDGER).read_text())
        if ledger.get('version') != 1:
            raise ValueError('Unsupported import ledger version')
        return ledger
    ledger = dict(version=1, sources=[], derivatives=[])
    legacy = project / 'photo-import-manifest.json'
    if legacy.exists():
        for old in json.loads(legacy.read_text()).get('files', []):
            source = Path(old['source'])
            record = copy.deepcopy(old)
            record.update(source_path=str(source), original_stem=source.stem,
                          original_parent=str(source.parent), verified=old.get('local_verified', False))
            ledger['sources'].append(record)
    by_path = {x['local_path']: x['sha256'] for x in ledger['sources']}
    for filename, kind, path_key, hash_key in [
        ('jpeg-conversion-manifest.json', 'jpeg', 'jpeg', 'jpeg_sha256'),
        ('dng-conversion-manifest.json', 'dng', 'local_dng', 'dng_sha256')]:
        manifest = project / filename
        if manifest.exists():
            for old in json.loads(manifest.read_text()).get('files', []):
                record = copy.deepcopy(old)
                record.update(kind=kind, local_path=old[path_key], sha256=old[hash_key],
                              source_sha256=old.get('source_sha256', by_path.get(old['source'])),
                              verified=(old.get('verified', False) if kind == 'jpeg' else
                                        old.get('conversion_status') == 'verified'))
                ledger['derivatives'].append(record)
    return ledger

def fraction(value):
    value=str(value if value is not None else '').strip()
    return Decimal('0.'+value) if value.isdigit() else None

def same_camera(a,b):
    return bool(a.get('camera') and a['camera']==b.get('camera') and
                (not a.get('camera_serial') or not b.get('camera_serial') or
                 a['camera_serial']==b['camera_serial']))

def match_photos(sources):
    jpegs=[x for x in sources if x['extension'].upper() in {'.JPG','.JPEG'}]
    result=[]
    for nef in [x for x in sources if x['extension'].upper()=='.NEF']:
        candidates=[]
        for jpg in jpegs:
            if not same_camera(nef,jpg) or nef['capture_time']!=jpg['capture_time']:continue
            a,b=fraction(nef.get('subsecond')),fraction(jpg.get('subsecond'))
            original=(nef.get('original_stem') and nef.get('original_stem')==jpg.get('original_stem') and
                      nef.get('original_parent')==jpg.get('original_parent'))
            if (a is not None and b is not None and a==b) or ((a is None or b is None) and original):
                candidates.append(jpg)
        if len(candidates)>1:
            by_name=[j for j in candidates if j.get('original_stem')==nef.get('original_stem') and
                     j.get('original_parent')==nef.get('original_parent')]
            if len(by_name)==1:candidates=by_name
        status='matched' if len(candidates)==1 else 'ambiguous' if candidates else 'unmatched'
        result.append(dict(nef_sha256=nef['sha256'],status=status,
                           jpeg_sha256=candidates[0]['sha256'] if status=='matched' else None,
                           candidates=[j['sha256'] for j in candidates]))
    # A camera JPEG must represent one exposure, not several indistinguishable NEFs.
    for match in result:
        if match['status']=='matched' and sum(x['jpeg_sha256']==match['jpeg_sha256'] for x in result)>1:
            match['status']='ambiguous'
    for match in result:
        if match['status']!='matched':match['jpeg_sha256']=None
    return result

def build_plan(project, metadata, ledger, review=False):
    project = Path(project).resolve()
    ledger = copy.deepcopy(ledger)
    known = {x['sha256']: x for x in ledger['sources']}
    review_known = {x['sha256']: x for x in ledger.get('review_imports', [])}
    historical = {}
    for record in ledger.get('historical_imports', []):
        if record.get('status') != 'archive_verified':
            raise ValueError('Historical import has no accepted status')
        if record['status'] == 'archive_verified' and not (
                record.get('dropbox_file_id') and record.get('dropbox_path') and record.get('verification')):
            raise ValueError('Verified archive record is missing its evidence')
        historical[record['sha256']] = record
    for record in ledger['sources'] + ledger['derivatives'] + ledger.get('review_imports', []):
        if not record.get('verified'):
            raise ValueError('Unverified ledger entry: ' + record['local_path'])
        path = Path(record['local_path'])
        if not path.is_file() or digest(path) != record['sha256']:
            raise ValueError('Local file missing or changed; hash mismatch: ' + str(path))
    rejected, incoming, already, duplicates = [], [], [], []
    archived, in_review = [], []
    seen = set(known) | set(historical) | set(review_known)
    for tags in metadata:
        source = Path(tags['SourceFile']).resolve()
        if source.suffix.upper() not in EXTENSIONS:
            continue
        sha = digest(source)
        if sha in seen:
            if sha in known:
                already.append(str(source))
            elif sha in review_known:
                in_review.append(str(source))
            elif sha in historical:
                archived.append(str(source))
            else:
                duplicates.append(str(source))
            continue
        try:
            captured = str(tags['DateTimeOriginal'])
            datetime.datetime.strptime(captured, '%Y:%m:%d %H:%M:%S')
        except (KeyError, ValueError):
            rejected.append(dict(source_path=str(source), reason='Missing or invalid DateTimeOriginal'))
            continue
        record = dict(source_path=str(source), sha256=sha, bytes=source.stat().st_size,
                      extension=source.suffix.upper(), capture_time=captured,
                      subsecond=str(tags.get('SubSecTimeOriginal', '')),
                      camera=str(tags.get('Model', '')),
                      camera_serial=str(tags.get('SerialNumber', tags.get('BodySerialNumber', ''))),
                      original_stem=source.stem, original_parent=str(source.parent), verified=False)
        if review:
            record['status'] = 'awaiting_user_review'
        incoming.append(record)
        seen.add(sha)
    incoming.sort(key=lambda x: (x['capture_time'], fraction(x['subsecond']) or Decimal(0),
                                 x['original_stem'], x['extension']))
    all_sources = ledger['sources'] + ([] if review else incoming)
    matches = match_photos(all_sources)
    partners = {}
    for match in matches:
        if match['status'] == 'matched':
            partners[match['nef_sha256']] = match['jpeg_sha256']
            partners[match['jpeg_sha256']] = match['nef_sha256']
    by_hash = {x['sha256']: x for x in all_sources}
    destination_root = project / 'unverified' if review else project
    existing_paths = list(destination_root.iterdir()) if destination_root.exists() else []
    occupied_stems = {p.stem.casefold() for p in existing_paths
                      if p.suffix.upper() in EXTENSIONS | {'.DNG'}}
    prior = ledger.get('review_imports', []) if review else ledger['sources']
    occupied_stems.update(Path(x['local_path']).stem.casefold() for x in prior)
    occupied_names = {p.name.casefold() for p in existing_paths}
    for record in incoming:
        partner = by_hash.get(partners.get(record['sha256']))
        paired_stem = Path(partner['local_path']).stem if partner and partner.get('local_path') else None
        stem = datetime.datetime.strptime(record['capture_time'], '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d %H.%M.%S')
        number = 0
        if paired_stem and (paired_stem + record['extension']).casefold() not in occupied_names:
            stem = paired_stem
        else:
            base = stem
            while stem.casefold() in occupied_stems:
                number += 1
                stem = base + '-' + str(number)
        destination = destination_root / (stem + record['extension'])
        record['local_path'] = str(destination)
        occupied_names.add(destination.name.casefold())
        occupied_stems.add(stem.casefold())
    ledger['sources'] = all_sources
    if review:
        ledger['review_imports'] = ledger.get('review_imports', []) + incoming
    ledger['matches'] = matches
    return dict(project=str(project), mode='review' if review else 'normal',
                sources_to_import=incoming, already_imported=already,
                already_archived=archived, already_in_review=in_review,
                duplicates=duplicates, rejected=rejected, matches=matches, ledger=ledger)

def apply_plan(project, plan):
    project = Path(project).resolve()
    if str(project) != plan['project']:
        raise ValueError('Plan belongs to a different project')
    # Refuse a stale plan after another import or upload updated the ledger.
    current = load_ledger(project)
    pending_hashes = {x['sha256'] for x in plan['sources_to_import']}
    review = plan.get('mode') == 'review'
    collection = 'review_imports' if review else 'sources'
    planned_prior = ([x for x in plan['ledger']['sources'] if x['sha256'] not in pending_hashes]
                     if not review else plan['ledger']['sources'])
    review_prior = ([x for x in plan['ledger'].get('review_imports', []) if x['sha256'] not in pending_hashes]
                    if review else plan['ledger'].get('review_imports', []))
    if (current['sources'] != planned_prior or current['derivatives'] != plan['ledger']['derivatives'] or
            current.get('historical_imports', []) != plan['ledger'].get('historical_imports', []) or
            current.get('review_imports', []) != review_prior):
        raise ValueError('Ledger changed; scan again before importing')
    ledger = copy.deepcopy(plan['ledger'])
    destination_root = project / 'unverified' if review else project
    if destination_root.is_symlink():
        raise ValueError('Unsafe destination directory')
    destination_root.mkdir(exist_ok=True)
    for record in ledger.get(collection, []):
        if record['sha256'] not in pending_hashes:
            continue
        destination = Path(record['local_path'])
        if destination.parent.resolve() != destination_root or destination.is_symlink():
            raise ValueError('Unsafe destination: ' + str(destination))
        if digest(record['source_path']) != record['sha256']:
            raise ValueError('Source changed after scan: ' + record['source_path'])
        if destination.exists():
            if digest(destination) != record['sha256']:
                raise ValueError('Destination hash mismatch: ' + str(destination))
        else:
            # Write atomically so an interrupted copy cannot be mistaken for a photo.
            temporary = destination.with_name(destination.name + '.importing')
            if temporary.exists():
                raise ValueError('Incomplete import exists; inspect it before retrying: ' + str(temporary))
            with open(record['source_path'], 'rb') as source, open(temporary, 'xb') as target:
                shutil.copyfileobj(source, target, 1024 * 1024)
            if digest(temporary) != record['sha256']:
                raise ValueError('Copied bytes failed verification: ' + str(temporary))
            # Exclusive link publishes the file without replacing an existing destination.
            os.link(temporary, destination)
            temporary.unlink()
        record['verified'] = True
        checkpoint = copy.deepcopy(ledger)
        checkpoint['sources'] = [x for x in checkpoint['sources'] if x.get('verified')]
        if 'review_imports' in checkpoint:
            checkpoint['review_imports'] = [x for x in checkpoint['review_imports'] if x.get('verified')]
        checkpoint['matches'] = match_photos(checkpoint['sources'])
        save_json(project / LEDGER, checkpoint)
    if not plan['sources_to_import']:
        save_json(project / LEDGER, ledger)
    return load_ledger(project)

def find_exiftool():
    executable = shutil.which('exiftool')
    bundled = sorted(glob.glob('/Applications/digiKam.org/digikam.app/Contents/bin/Image-ExifTool-*/exiftool'))
    if not executable and not bundled:
        raise ValueError('ExifTool is unavailable; locate it before importing')
    return executable or bundled[-1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    scan = commands.add_parser('scan')
    scan.add_argument('--card', required=True)
    scan.add_argument('--project', required=True)
    scan.add_argument('--plan', required=True)
    scan.add_argument('--review', action='store_true', help='Copy new originals into unverified for user review')
    apply = commands.add_parser('import')
    apply.add_argument('--project', required=True)
    apply.add_argument('--plan', required=True)
    args = parser.parse_args()
    if args.command == 'scan':
        card = Path(args.card).resolve()
        if not card.is_dir():
            raise ValueError('Card directory does not exist')
        output = subprocess.check_output([find_exiftool(), '-json', '-r', '-ext', 'NEF', '-ext', 'JPG',
                                          '-ext', 'JPEG', '-DateTimeOriginal', '-SubSecTimeOriginal',
                                          '-Model', '-SerialNumber', '-BodySerialNumber', str(card)])
        plan = build_plan(args.project, json.loads(output), load_ledger(args.project), review=args.review)
        save_json(args.plan, plan)
        print(json.dumps({k: len(plan[k]) for k in ['sources_to_import', 'already_imported', 'already_archived',
                                                 'already_in_review', 'duplicates', 'rejected']}))
    else:
        ledger = apply_plan(args.project, json.loads(Path(args.plan).read_text()))
        print(json.dumps(dict(verified_sources=len(ledger['sources']), derivatives=len(ledger['derivatives']),
                              review_imports=len(ledger.get('review_imports', [])))))

if __name__ == '__main__':
    main()
