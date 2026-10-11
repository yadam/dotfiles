---
name: camera-import
description: Import new DSLR NEF and JPEG photos from an inserted SD card into Adam's camera companion project. Match camera JPEGs to NEFs, create missing JPEGs and lossless DNGs, and upload JPEGs to Camera Uploads and DNGs to capture-year folders in Dropbox. Use for a requested camera import or resuming that workflow.
---

# Camera import

Import all photos not previously imported, regardless of capture date. The default
project is `~/Pictures/camera companion`. Honor an explicit destination
or scope override in the current request.

Keep card originals and local NEFs. Never upload NEFs to Camera Uploads. Preserve
camera JPEGs as supplied by the camera. A requested import authorizes this workflow
and its Dropbox destinations. State the planned copies, conversions, uploads, and
any new year folders before acting. Ask only when a missing input changes the
result, such as multiple candidate cards or unusable capture dates. Loading the
skill during a discussion alone does not authorize an import.

## Desktop application cleanup

Before launching a desktop application, record whether it is already running.
Track each app this run launches, plus any windows or browser tabs it creates
in apps that were already open. Prefer the command-line conversion helpers when
available so no desktop application needs to open.

On completion, failure, or cancellation, save progress and wait for active file
operations to finish or stop safely before cleanup. Quit each desktop application
launched by this run using its normal Quit action, then verify it is no longer
running. Leave applications that were already running open, and close only the
windows or tabs this run created in them. Do not force-quit an app or discard
unsaved changes. If a save prompt or active operation prevents safe cleanup,
retain the app and report what needs attention. Perform cleanup before the final
response, including when some files remain pending.

## Import and match

1. Find the mounted SD card with a `DCIM` directory. `/Volumes/NIKON D7000` was the
   last card used, but verify the mounted volume each time. Do not scan unrelated
   external drives. Resolve this skill's directory as `camera_skill_dir`.
2. Run the read-only scan below. It hashes originals, reads EXIF metadata, and
   loads `camera-import-ledger.json`. On the first run, it seeds existing source,
   derivative, and upload records from this project's three legacy manifests.

   ```sh
   python3 "$camera_skill_dir/scripts/import_photos.py" scan \
     --card "$camera_card_dir/DCIM" --project "$camera_project_dir" \
     --plan "$camera_project_dir/camera-import-plan.json"
   ```

3. Inspect the plan and available disk space. Copy every new NEF, JPG, and JPEG
   accepted by the plan. Report rejected metadata rather than substituting file
   modification dates. SHA-256 identifies previously imported content even when
   a card filename or volume name has changed.

   ```sh
   python3 "$camera_skill_dir/scripts/import_photos.py" import \
     --project "$camera_project_dir" \
     --plan "$camera_project_dir/camera-import-plan.json"
   ```

4. Use the ledger's `matches` to decide which NEFs need JPEG conversion. A match
   requires the same capture second and camera model, agreeing serial numbers
   when available, and agreeing subseconds. Missing subseconds require the same
   original card filename stem and directory as well. Original filenames resolve
   burst ties. An ambiguous or unmatched NEF needs a generated JPEG. Do not choose
   an arbitrary JPEG or pair solely by the renamed timestamp.

Names use camera-local EXIF `DateTimeOriginal` as `yyyy-mm-dd hh.mm.ss`, followed
by the extension. Do not apply the computer's timezone. Distinct photos within
one second use `-1`, `-2`, and onward, following Camera Uploads' existing convention.
A verified NEF/JPEG pair shares its base name. Existing files are preserved.
The helper copies bytes, verifies their hashes, and checkpoints each source.

The ledger may also contain `historical_imports` for photos already verified in
the Dropbox archive and `review_imports` for local originals awaiting Adam's
review. Both collections are recognized by source SHA-256 and skipped on later
imports. Historical records do not require local NEFs. Review originals live in
`unverified/`; do not convert or upload them until Adam explicitly requests it.
For a requested import into that review folder, add `--review` to the scan
command, inspect its plan, then run the usual import command. This mode copies
originals and records them separately from the normal conversion sources.

## Convert and upload

Read [references/conversion.md](references/conversion.md) when conversions are
pending. Generate a full-resolution sRGB JPEG only for a NEF without a verified
camera JPEG or an existing verified generated JPEG. Convert every normally
imported NEF to a lossless mosaic DNG, reusing existing verified DNGs. Use
`JPEGs/` and `DNGs/` within the project, retaining each NEF's timestamp base name.

Read [references/ledger-and-dropbox.md](references/ledger-and-dropbox.md) before
recording new derivatives or uploading. Use the connected Dropbox plugin to:

- Upload every imported camera JPEG and each needed generated JPEG to
  `/Camera Uploads`.
- Upload DNGs to `/edited DNG Files/YYYY`, where `YYYY` comes from that photo's
  EXIF capture date. Create missing capture-year subfolders as part of the import.
- Reuse completed upload records, resume pending operations, preserve existing
  remote files, and record any additional filename suffix required by a collision.

An interrupted run must resume from the ledger. Verify source and derivative
hashes before reuse. Inspect a leftover `.importing` file or an unrecorded output
and reconcile it against its source before proceeding. A missing or changed
recorded file is an error to investigate, not evidence that the photo is new.
Continue independent files when one conversion or upload fails and retain its
pending state. Do not delete originals, install applications, change Brewfiles,
or replace existing Dropbox files as an import recovery step.

## Completion

Complete when all accepted new originals have verified local copies, NEF/JPEG
matches are recorded, every normally imported NEF has a verified DNG, all
required JPEGs exist, the required Dropbox uploads have completed with matching
byte counts, and
desktop application cleanup is verified. Record remote paths and file IDs.
Report counts for new originals, previously imported files, matched pairs,
generated JPEGs, DNGs, verified uploads, and any rejected or
pending files. A dry run reports its plan and performs no import or upload.
For a review-only import, completion requires verified copies in `unverified/`
and durable review records, with no conversion or Dropbox upload.
