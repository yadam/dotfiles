import import_photos as workflow
import unittest

class MatchingTests(unittest.TestCase):
    def test_burst_pairs_use_subseconds_and_camera_identity(self):
        def record(ext, fraction, digest, stem):
            return dict(extension=ext, capture_time='2026:10:08 18:39:36', subsecond=fraction,
                        camera='NIKON D7000', camera_serial='test-camera-001', sha256=digest,
                        original_stem=stem, original_parent='/card/DCIM/102D7000')
        photos=[record('.NEF','50','raw-a','_DSC3638'),record('.NEF','60','raw-b','_DSC3639'),
                record('.JPG','50','jpg-a','_DSC3638'),record('.JPG','60','jpg-b','_DSC3639')]
        actual=workflow.match_photos(photos)
        self.assertEqual([x['jpeg_sha256'] for x in actual],['jpg-a','jpg-b'])
        photos[2]['camera_serial']='another-camera'
        self.assertEqual(workflow.match_photos(photos)[0]['status'],'unmatched')

    def test_indistinguishable_exposures_do_not_share_a_jpeg(self):
        common=dict(capture_time='2026:10:08 18:39:36',subsecond='50',camera='NIKON D7000')
        records=[dict(common,extension='.NEF',sha256='raw-a'),
                 dict(common,extension='.NEF',sha256='raw-b'),
                 dict(common,extension='.JPG',sha256='jpg')]
        self.assertEqual([x['status'] for x in workflow.match_photos(records)],['ambiguous','ambiguous'])
        records[0].update(subsecond=None,original_stem='_DSC1',original_parent='/card/DCIM')
        records[2].update(subsecond=None,original_stem='_DSC1',original_parent='/card/DCIM')
        result=workflow.match_photos(records)
        self.assertEqual([x['status'] for x in result],['matched','unmatched'])

import tempfile,pathlib,hashlib

class ImportTests(unittest.TestCase):
    def test_review_import_copies_without_entering_conversion_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp);project=root/'project';project.mkdir()
            source=root/'DSC_2.NEF';source.write_bytes(b'review-raw')
            tags=[dict(SourceFile=str(source),DateTimeOriginal='2018:09:14 12:00:00')]
            ledger=dict(version=1,sources=[],derivatives=[])
            plan=workflow.build_plan(project,tags,ledger,review=True)
            self.assertEqual(plan['ledger']['sources'],[])
            self.assertEqual(plan['ledger']['review_imports'][0]['status'],'awaiting_user_review')
            workflow.apply_plan(project,plan)
            copied=project/'unverified/2018-09-14 12.00.00.NEF'
            self.assertEqual(copied.read_bytes(),b'review-raw')
            self.assertEqual(source.read_bytes(),b'review-raw')
            self.assertEqual(workflow.load_ledger(project)['sources'],[])
            resumed=workflow.build_plan(project,tags,workflow.load_ledger(project))
            self.assertEqual(resumed['sources_to_import'],[])
            self.assertEqual(resumed['already_in_review'],[str(source.resolve())])
            self.assertEqual(resumed['matches'],[])
            copied.write_bytes(b'changed')
            with self.assertRaisesRegex(ValueError,'changed|mismatch'):
                workflow.build_plan(project,tags,workflow.load_ledger(project))

    def test_verified_archive_is_skipped_without_a_local_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp);project=root/'project';project.mkdir()
            source=root/'DSC_1.NEF';source.write_bytes(b'old-raw')
            ledger=dict(version=1,sources=[],derivatives=[],historical_imports=[
                dict(sha256=workflow.digest(source),status='archive_verified',
                     dropbox_file_id='id:archived',dropbox_path='/edited DNG Files/2018/photo.dng',
                     verification=dict(method='capture_metadata',matched_fields=['DateTimeOriginal','SerialNumber','ShutterCount']))])
            tags=[dict(SourceFile=str(source),DateTimeOriginal='2018:03:17 13:50:47')]
            plan=workflow.build_plan(project,tags,ledger)
            self.assertEqual(plan['sources_to_import'],[])
            self.assertEqual(plan['already_archived'],[str(source.resolve())])
            workflow.save_json(project/workflow.LEDGER,ledger)
            workflow.apply_plan(project,plan)
            self.assertEqual(workflow.load_ledger(project)['historical_imports'],ledger['historical_imports'])
            self.assertFalse(any(project.glob('*.NEF')))
            changed=workflow.load_ledger(project)
            changed['historical_imports'][0]['dropbox_file_id']='id:changed'
            workflow.save_json(project/workflow.LEDGER,changed)
            with self.assertRaisesRegex(ValueError,'Ledger changed'):
                workflow.apply_plan(project,plan)

    def test_plan_copy_and_resume_preserve_originals_and_share_pair_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp);card=root/'card';project=root/'project';card.mkdir();project.mkdir()
            photos=[]
            for name,payload,subsecond in [('_DSC1.NEF',b'raw-a','50'),('_DSC1.JPG',b'jpg-a','50'),('_DSC2.NEF',b'raw-b','60')]:
                path=card/name;path.write_bytes(payload)
                photos.append(dict(SourceFile=str(path),DateTimeOriginal='2026:10:08 18:39:36',
                                   SubSecTimeOriginal=subsecond,Model='NIKON D7000',SerialNumber=123))
            ledger={'version':1,'sources':[],'derivatives':[]}
            plan=workflow.build_plan(project,photos,ledger)
            self.assertEqual([pathlib.Path(x['local_path']).name for x in plan['sources_to_import']],
                             ['2026-10-08 18.39.36.JPG','2026-10-08 18.39.36.NEF','2026-10-08 18.39.36-1.NEF'])
            workflow.apply_plan(project,plan)
            self.assertEqual((card/'_DSC1.NEF').read_bytes(),b'raw-a')
            resumed=workflow.build_plan(project,photos,workflow.load_ledger(project))
            self.assertEqual(resumed['sources_to_import'],[])
            self.assertEqual([x['status'] for x in resumed['matches']],['matched','unmatched'])
            (project/'2026-10-08 18.39.36.NEF').write_bytes(b'changed')
            with self.assertRaisesRegex(ValueError,'changed|mismatch'):
                workflow.build_plan(project,photos,workflow.load_ledger(project))

    def test_missing_metadata_is_rejected_and_zero_subsecond_is_known(self):
        self.assertEqual(workflow.fraction(0),workflow.fraction('00'))
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp);photo=root/'a.NEF';photo.write_bytes(b'raw')
            plan=workflow.build_plan(root,[{'SourceFile':str(photo)}],{'version':1,'sources':[],'derivatives':[]})
            self.assertEqual(plan['sources_to_import'],[])
            self.assertEqual(len(plan['rejected']),1)

    def test_existing_file_is_not_overwritten_and_stale_plan_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp);project=root/'project';project.mkdir()
            source=root/'a.NEF';source.write_bytes(b'raw')
            occupied=project/'2026-10-08 18.39.36.NEF';occupied.write_bytes(b'existing')
            metadata=[dict(SourceFile=str(source),DateTimeOriginal='2026:10:08 18:39:36')]
            plan=workflow.build_plan(project,metadata,workflow.load_ledger(project))
            self.assertTrue(plan['sources_to_import'][0]['local_path'].endswith('-1.NEF'))
            destination=pathlib.Path(plan['sources_to_import'][0]['local_path'])
            destination.write_bytes(b'another-file')
            with self.assertRaisesRegex(ValueError,'mismatch'):
                workflow.apply_plan(project,plan)
            self.assertEqual(occupied.read_bytes(),b'existing')
            self.assertEqual(destination.read_bytes(),b'another-file')
            workflow.save_json(project/workflow.LEDGER,dict(version=1,sources=[],derivatives=[dict(kind='new')]))
            with self.assertRaisesRegex(ValueError,'Ledger changed'):
                workflow.apply_plan(project,plan)

if __name__=='__main__': unittest.main()
