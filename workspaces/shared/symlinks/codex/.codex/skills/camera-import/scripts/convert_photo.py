#!/usr/bin/env python3
"""Convert one NEF, validate the derivative, and print evidence as JSON."""
import argparse
import json
import os
from pathlib import Path
import platform
import subprocess
import tempfile

from import_photos import digest, find_exiftool, fraction

SKILL = Path(__file__).resolve().parents[1]
CONTENTS = Path('/Applications/digiKam.org/digikam.app/Contents')
PINNED = {
    'lib/libdigikamcore.9.1.0.dylib': 'ce92c3874976d4acdaeb5d04236d97341bac7460ae1adfc6e9f356a85420e22d',
    'libexec/qt6/lib/QtCore.framework/Versions/A/QtCore': 'a7c4d463b17d308da2751999fb081eb8deb51800a981d45bd459495a4814a0d2',
}

def run(command, **kwargs):
    result = subprocess.run([str(x) for x in command], capture_output=True, text=True, **kwargs)
    if result.returncode:
        raise RuntimeError('Command failed: ' + str(command[0]) + '\n' +
                           (result.stdout + result.stderr)[-6000:])
    return result.stdout

def tags(path):
    return json.loads(run([find_exiftool(), '-json', '-DateTimeOriginal', '-SubSecTimeOriginal',
                           '-Orientation', '-DNGVersion', '-Model', path]))[0]

def verify(source, target, kind):
    import rawpy
    import numpy as np
    original, converted = tags(source), tags(target)
    if not original.get('DateTimeOriginal') or original.get('DateTimeOriginal') != converted.get('DateTimeOriginal'):
        raise ValueError('Capture date was not preserved')
    if fraction(original.get('SubSecTimeOriginal')) != fraction(converted.get('SubSecTimeOriginal')):
        raise ValueError('Capture subsecond was not preserved')
    evidence = dict(capture_metadata_verified=True, capture_time=original['DateTimeOriginal'],
                    subsecond=original.get('SubSecTimeOriginal'))
    with rawpy.imread(str(source)) as raw:
        if kind == 'dng':
            with rawpy.imread(str(target)) as dng:
                if not converted.get('DNGVersion'):
                    raise ValueError('Output is not a DNG')
                if original.get('Orientation') != converted.get('Orientation'):
                    raise ValueError('DNG orientation was not preserved')
                if not np.array_equal(raw.raw_pattern, dng.raw_pattern) or not np.array_equal(raw.raw_image_visible, dng.raw_image_visible):
                    raise ValueError('DNG visible sensor samples or CFA pattern changed')
                evidence.update(raw_sensor_pixels_identical=True,
                                raw_sensor_shape=list(dng.raw_image_visible.shape))
        else:
            from PIL import Image
            with Image.open(target) as image:
                image.load()
                if image.format != 'JPEG':
                    raise ValueError('Output is not a decodable JPEG')
                # RawTherapee removes a four-pixel demosaic border on this camera.
                # LibRaw's visible sensor size includes that border.
                if original.get('Model') != 'NIKON D7000':
                    raise ValueError('Verify full-resolution JPEG dimensions for this camera before extending the recipe')
                expected = sorted([raw.sizes.width - 8, raw.sizes.height - 8])
                if sorted(image.size) != expected:
                    raise ValueError('JPEG was resized: ' + str(image.size) + '; expected ' + str(expected))
                if not image.info.get('icc_profile'):
                    raise ValueError('JPEG output profile is missing')
                evidence.update(width=image.width, height=image.height, full_resolution=True)
    return evidence

def convert(source, output, kind):
    source, output = Path(source).resolve(), Path(output).absolute()
    if source.suffix.upper() != '.NEF' or not source.is_file():
        raise ValueError('Source must be an existing NEF')
    if output.exists() or output.is_symlink():
        raise ValueError('Output already exists; verify and reuse it instead of overwriting')
    if output.suffix.lower() != ('.dng' if kind == 'dng' else '.jpg'):
        raise ValueError('Output extension does not match conversion kind')
    # Load validation dependencies before spending time converting.
    import rawpy
    import numpy
    if kind == 'jpeg':
        from PIL import Image
    before = digest(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.camera-convert-', dir=output.parent) as work:
        work = Path(work)
        target = work / output.name
        if kind == 'jpeg':
            app = Path('/Applications/RawTherapee.app/Contents')
            env = dict(os.environ, RT_SETTINGS=str(work / 'settings'), RT_CACHE=str(work / 'cache'))
            run([app / 'MacOS/rawtherapee-cli-bin', '-o', target, '-q', '-j95', '-js3',
                 '-p', app / 'Resources/share/profiles/Auto-Matched Curve - ISO Low.pp3',
                 '-p', SKILL / 'assets/jpeg-export.pp3', '-c', source], env=env)
            run([find_exiftool(), '-TagsFromFile', source, '-DateTimeOriginal', '-CreateDate',
                 '-SubSecTimeOriginal', '-SubSecTimeDigitized', '-OffsetTimeOriginal',
                 '-overwrite_original', target])
        else:
            if platform.machine() != 'arm64':
                raise ValueError('The tested digiKam engine adapter requires Apple Silicon')
            for relative, expected in PINNED.items():
                path = CONTENTS / relative
                if not path.is_file() or digest(path) != expected:
                    raise ValueError('digiKam/Qt changed; use its supported DNG GUI or review the adapter before updating its pins')
            executable = work / 'dng-engine'
            run(['clang++', '-std=c++17', SKILL / 'scripts/digikam_9_1_engine.cpp',
                 '-Wl,-rpath,' + str(CONTENTS), '-o', executable])
            run([executable, source, target])
            run([find_exiftool(), '-TagsFromFile', source, '-IPTC:all', '-XMP:all', '-MakerNotes',
                 '-SubSecTime', '-SubSecTimeOriginal', '-SubSecTimeDigitized',
                 '-overwrite_original', target])
        evidence = verify(source, target, kind)
        if digest(source) != before:
            raise ValueError('Source NEF changed during conversion')
        evidence.update(kind=kind, source_sha256=before, local_path=str(output),
                        sha256=digest(target), bytes=target.stat().st_size, verified=True)
        os.link(target, output)
        return evidence

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=['jpeg', 'dng'])
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    if args.verify_only:
        evidence = verify(Path(args.source), Path(args.output), args.kind)
        evidence.update(kind=args.kind, source_sha256=digest(args.source), local_path=str(Path(args.output).absolute()),
                        sha256=digest(args.output), bytes=Path(args.output).stat().st_size, verified=True)
    else:
        evidence = convert(args.source, args.output, args.kind)
    print(json.dumps(evidence))

if __name__ == '__main__':
    main()
