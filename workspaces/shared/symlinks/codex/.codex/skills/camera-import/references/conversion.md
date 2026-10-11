# Conversion recipes

Use `scripts/convert_photo.py` for the tested Nikon D7000 workflow. The helper
converts one NEF into a temporary file, validates it, and publishes it without
replacing an existing output. Its JSON result is the derivative's ledger record.
Checkpoint each successful record before starting the next file.

## Python dependencies

The importer uses Python's standard library. Conversion validation needs
`numpy`, `Pillow`, and `rawpy`. Locate the configured Python runtime through
Codex's workspace dependency tool. The runtime last used was:

```text
~/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
```

Expand the home-relative path before assigning it to `camera_python`. Use that
runtime if it still exists and has the dependencies. If `rawpy` is
missing, install it into a temporary, isolated dependency directory using that
runtime's `pip --target`, then pass the directory through `PYTHONPATH`. Do not
install packages globally or assume last session's temporary directory survives.
The previous run used rawpy 0.27.1. Application installs belong in Adam's
dotfiles Brewfiles and require a separate request.

## Missing JPEGs

```sh
"$camera_python" "$camera_skill_dir/scripts/convert_photo.py" jpeg \
  --source "$camera_nef" --output "$camera_jpeg"
```

The helper uses installed RawTherapee's CLI with Auto-Matched Curve - ISO Low,
the bundled `assets/jpeg-export.pp3`, JPEG quality 95, 4:4:4 chroma, sRGB, and
resizing disabled. It isolates RawTherapee's settings and cache. It preserves
capture dates and subseconds, decodes the entire JPEG, checks the embedded color
profile, and verifies full-resolution dimensions. D7000 output is 4940×3272,
allowing rotation. LibRaw's 4948×3280 visible sensor includes the four-pixel
demosaic border that RawTherapee removes. For another camera, establish the
full-resolution crop before extending this dimension check.

Reuse an existing verified derivative rather than overwriting it. Check an
unrecorded candidate with the same command and `--verify-only`, then confirm
its source association before adding its evidence to the ledger. Metadata and
dimensions alone do not establish provenance.

## Lossless DNGs

```sh
"$camera_python" "$camera_skill_dir/scripts/convert_photo.py" dng \
  --source "$camera_nef" --output "$camera_dng"
```

The tested fallback calls the installed digiKam 9.1.0 DNGWriter conversion engine
because its GUI crashed during the earlier batch. It saves lossless mosaic RAW
data, a medium preview, and no embedded original NEF. The local NEF remains.
The adapter in `scripts/digikam_9_1_engine.cpp` uses exported C++ symbols without
installed development headers. It requires Apple Silicon, `clang++`, and exact
SHA-256 matches for the digiKam and Qt libraries recorded in the Python helper.
This is a version-specific fallback, not a stable public CLI.

If the library checks fail after an app update, use digiKam's supported batch
RAW-to-DNG tool with lossless compression, preserve originals, and disable
embedding the original RAW. Inspect the current app before selecting controls.
Do not blindly change the adapter's hashes or opaque allocation sizes. Reviewing
an adapter update requires current source/API evidence and a real conversion
comparison. Darktable exports processed images and is not this RAW-to-DNG path.

The helper restores IPTC, XMP, Nikon MakerNotes, and subsecond tags onto the new
DNG with ExifTool. digiKam's bundled ExifTool lives under
`Contents/bin/Image-ExifTool-*/exiftool`; locate it directly without modifying
the application. Validation requires unchanged NEF hashes, preserved capture
date, subseconds and orientation, a DNG version, and exactly equal decoded
visible sensor samples and CFA patterns using rawpy/numpy. Compare
`raw_image_visible`, because the NEF has extra storage padding columns. A JPEG
compression tag alone does not prove that DNG RAW data is lossless.

Supported GUI outputs can use `convert_photo.py dng --verify-only` for these same
checks. A failed validation must remain pending and must not be uploaded.

The adapter was reviewed against digiKam's
[9.1.0 DNGWriter header](https://invent.kde.org/graphics/digikam/-/blob/v9.1.0/core/libs/dngwriter/dngwriter.h)
and its conversion implementation in the same source directory. RawTherapee's
installed CLI help establishes the export arguments.
