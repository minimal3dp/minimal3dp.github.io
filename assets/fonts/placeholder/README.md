Placeholder font directory
==========================

Add a TrueType font file named `placeholder-font.ttf` here to override the default font used for generated fallback thumbnails (`scripts/cache_fallback_thumbnails.py`).

Recommended small fonts (open license):
- DejaVu Sans (https://dejavu-fonts.github.io/) – SIL Open Font License
- Inter (https://github.com/rsms/inter) – Open Font License (use a subset to keep size small)

Keep font file size minimal (<200KB) to avoid repo bloat. The script will also attempt to auto-detect common system fonts if no local font is present.

No font committed by default to keep repository lean.
