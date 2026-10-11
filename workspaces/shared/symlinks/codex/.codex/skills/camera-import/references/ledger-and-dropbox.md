# Ledger and Dropbox

`camera-import-ledger.json` is the durable record in the project. The importer
creates it after copying and verifying sources. On first use, it loads the
existing `photo-import-manifest.json`, `jpeg-conversion-manifest.json`, and
`dng-conversion-manifest.json` without changing them. Preserve inherited upload
records and evidence, including remote names that differ from local names.

## Checkpoint evidence

The schema has `version: 1`, `sources`, `derivatives`, and `matches`, with optional
`historical_imports` and `review_imports` collections.

- Sources contain SHA-256, bytes, source/local paths, EXIF capture time,
  subseconds, camera identity, original card filename/directory, extension, and
  `verified: true` after the copy passes its hash check.
- Derivatives contain the conversion helper's JSON result: `kind` of `jpeg` or
  `dng`, `source_sha256`, `local_path`, `sha256`, `bytes`, `verified`, capture
  metadata, and either JPEG dimensions or DNG sensor comparison evidence.
- Matches contain `nef_sha256`, `status`, `jpeg_sha256`, and candidate hashes.
  Only `status: matched` permits using a camera JPEG for that NEF.
- Historical imports contain the source SHA-256, original capture metadata,
  `status: archive_verified`, a Dropbox path/file ID, and verification evidence.
  They identify photos already archived without claiming a local original copy.
  For the 2018 reconciliation, evidence compares capture date, camera model,
  camera serial number, shutter count, and file number, with agreeing subseconds
  when present. It establishes photo identity, not pixel equality or a full-file
  integrity check. Keep the verification method explicit and do not mark a photo
  verified merely because its timestamp filename exists.
- Review imports contain source/local paths, source SHA-256, capture metadata,
  `verified: true` after byte comparison, and `status: awaiting_user_review`.
  They live in `unverified/` and are held out of conversion and upload until Adam
  explicitly asks to process them. Later scans verify their local hashes and
  report them as `already_in_review`.
- Add upload fields to the asset's own record: `dropbox_path`, `upload_status`,
  opaque `operation_id` while pending, `dropbox_file_id`, saved path, remote byte
  count, and `dropbox_size_verified`. Keep failure/attempt history when retrying.

Use the import helper's `load_ledger()` and atomic `save_json()` functions when
checkpointing from Python. Reload the current ledger, append each verified
derivative or update its existing record, then save. Identify a derivative by
source hash and kind. Do not start simultaneous ledger writers or overwrite the
ledger with an old plan after conversion/upload progress has been recorded.
Keep the source association when resuming a partial run. Validate hashes before
trusting any record. Do not infer a successful upload from a local filename.

## Destinations and collisions

Use Dropbox `get_file_metadata` to resolve `/Camera Uploads` and
`/edited DNG Files`. Resolve or create each necessary year folder under the
returned DNG folder. Prefer returned `path_display` and retain namespace paths
verbatim when it is absent. Recheck the current tool schema rather than assuming
a prior namespace ID is still applicable.

Preflight each intended destination using exact-path metadata. Dropbox paths are
case-insensitive. A different existing photo keeps its name; allocate the next
free `-N` suffix and checkpoint the mapping before upload. Use the unsuffixed
capture timestamp followed by the next available integer, not nested suffixes.
For a previously completed upload, verify its recorded ID/path and byte count
and reuse it. Equal size alone does not establish that an unrecorded remote file
is the same photo. Verify content where supported or choose a free name.

Exact checks are preferable to paging a large Camera Uploads library. If using
`list_folder`, request `recursive: false`, and treat listings as partial until
all cursor pages are read. Search results are not a complete collision inventory.
Only an explicit NOT_FOUND result means a path is free. Permission, network,
and other errors must not be interpreted as absence.

## Upload and resume

Use the connected Dropbox plugin, not a filesystem sync-folder assumption.
The adapter used here accepts an absolute local path as `source_file`:

```text
dropbox_upload_file({destination_path: exact_remote_path,
                     source_file: absolute_local_photo_path})
```

Follow the available schema if the adapter changes. Before invoking the upload,
checkpoint `dropbox_path` and an uploading state. Limit active uploads to two.
For `status: in_progress`, save the operation token unchanged and resume with
`dropbox_check_upload_file_status`. Respect its recommended poll interval and
use wait budgets up to 30 seconds. Pending does not mean completed.

After `completed`, save the returned file ID and path, then call
`dropbox_get_file_metadata` and require the remote size to match the local file.
Mark `dropbox_size_verified: true` only after that check. Previous manifests may
record byte counts as `dropbox_bytes`, `dropbox_size`, or `dng_size`.

After interruption, poll a saved token first. If the token expired or an upload
started before its token could be saved, inspect the recorded destination.
Verify content identity through a supported download/hash check before adopting
an unrecorded remote result. If identity cannot be established, leave that asset
pending and ask for a decision. Do not upload another copy under a new suffix
merely because an operation's outcome is unknown.

`FETCH_FAILED` was transient in the prior batch. After an explicit terminal
failure, check that the destination is absent before retrying. Allow at most
two retries per file and record each attempt. An `ALREADY_EXISTS` error requires
reconciliation rather than retrying the same path. Pause affected uploads for
quota or permission errors. Continue unrelated local work and report remaining
pending files. Error text can contain the actual Dropbox reason even when the
outer code is a generic INVALID_ARGUMENT.

Report new folders and successful uploads using their returned paths. Reverting
an upload would require deleting the corresponding Dropbox file after a
separate explicit deletion request. Never delete files during import.
