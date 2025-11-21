"""Download YouTube thumbnail images for fallback videos locally.

Outputs JPEG originals into assets/images/youtube-fallback/<video_id>.jpg
Run prior to Hugo build when updating fallback list.
Uses only stdlib (urllib) to avoid new dependencies.
"""
from __future__ import annotations
import json
import pathlib
import urllib.request
import sys
import hashlib
from typing import Optional

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # Pillow not installed yet; placeholder generation will be skipped
    Image = None  # type: ignore
    ImageDraw = None  # type: ignore
    ImageFont = None  # type: ignore

FALLBACK_JSON = pathlib.Path("data/youtube_popular_fallback.json")
OUT_DIR = pathlib.Path("assets/images/youtube-fallback")
FONT_HASH_FILE = OUT_DIR / ".font_hash"

def main() -> int:
    if not FALLBACK_JSON.exists():
        print(f"Fallback JSON not found: {FALLBACK_JSON}", file=sys.stderr)
        return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(FALLBACK_JSON.read_text())
    videos = data.get("videos", [])
    downloaded = 0
    current_font_hash: Optional[str] = None
    if ImageFont is not None:
        fobj = _load_font(raw=True)
        if fobj is not None:
            current_font_hash = hashlib.sha256(fobj[1]).hexdigest()
    previous_font_hash = FONT_HASH_FILE.read_text().strip() if FONT_HASH_FILE.exists() else None
    font_changed = current_font_hash and current_font_hash != previous_font_hash
    if font_changed:
        print(f"Font change detected (old={previous_font_hash}, new={current_font_hash}); placeholders will be regenerated.")

    for v in videos:
        vid = v.get("id") or v.get("videoId")
        thumb_url = v.get("thumbnail")
        if not vid or not thumb_url:
            continue
        dest = OUT_DIR / f"{vid}.jpg"
        if dest.exists() and not font_changed:
            print(f"Skip existing {dest}")
            continue
        if dest.exists() and font_changed:
            # Attempt fresh download first; overwrite on success/placeholder regen.
            print(f"Rebuilding due to font change: {dest}")
        try:
            print(f"Downloading {thumb_url} -> {dest}")
            with urllib.request.urlopen(thumb_url) as r, open(dest, "wb") as f:
                f.write(r.read())
            downloaded += 1
        except Exception as e:  # noqa: BLE001
            print(f"Failed download for {vid}: {e}", file=sys.stderr)
            if Image is None:
                print("Pillow not available; cannot generate placeholder.", file=sys.stderr)
                continue
            try:
                create_placeholder(vid, dest)
                print(f"Created placeholder {dest}")
                downloaded += 1
            except Exception as pe:  # noqa: BLE001
                print(f"Failed placeholder for {vid}: {pe}", file=sys.stderr)
    print(f"Downloaded {downloaded} new thumbnails.")
    if current_font_hash:
        FONT_HASH_FILE.write_text(current_font_hash)
    return 0

def create_placeholder(video_id: str, dest: pathlib.Path) -> None:
    """Create a simple branded placeholder image (480x270) deterministically colored.
    Attempts to use an embedded or system TrueType font for crisper text.
    If no font found falls back to default PIL bitmap font.
    """
    h = hashlib.sha256(video_id.encode()).hexdigest()
    r = (int(h[0:2], 16) % 128) + 64
    g = (int(h[2:4], 16) % 128) + 64
    b = (int(h[4:6], 16) % 128) + 64
    img = Image.new("RGB", (480, 270), (r, g, b))
    draw = ImageDraw.Draw(img)

    font = _load_font()
    title_text = "Minimal3DP"
    id_text = f"Video: {video_id[:10]}"

    # Center horizontally using textbbox when font available
    def center_y(base_y: int, text: str, f) -> tuple[int, int]:
        try:
            bbox = draw.textbbox((0, 0), text, font=f)
            w = bbox[2] - bbox[0]
            return ( (480 - w)//2, base_y )
        except Exception:
            return (20, base_y)

    x1, y1 = center_y(110, title_text, font)
    x2, y2 = center_y(150, id_text, font)
    draw.text((x1, y1), title_text, fill=(255, 255, 255), font=font)
    draw.text((x2, y2), id_text, fill=(255, 255, 255), font=font)
    img.save(dest, format="JPEG", quality=85)

def _load_font(raw: bool = False) -> Optional[ImageFont.FreeTypeFont]:  # type: ignore[name-defined]
    """Attempt to load a crisp TrueType font from local assets or system.
    If raw=True returns a tuple of (path_bytes, file_bytes) for hashing.
    Returns PIL default font if truetype not available.
    """
    if ImageFont is None:
        return None
    # Local project font override path
    local_paths = [
        pathlib.Path("assets/fonts/placeholder/placeholder-font.ttf"),
        pathlib.Path("assets/fonts/placeholder/DejaVuSans.ttf"),
    ]
    for p in local_paths:
        if p.exists():
            try:
                data = p.read_bytes()
                font = ImageFont.truetype(str(p), size=28)
                return (p, data) if raw else font
            except Exception:
                pass
    # Common system font locations (GitHub Actions runner, macOS)
    sys_candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for fp in sys_candidates:
        if pathlib.Path(fp).exists():
            try:
                data = pathlib.Path(fp).read_bytes()
                font = ImageFont.truetype(fp, size=28)
                return (pathlib.Path(fp), data) if raw else font
            except Exception:
                continue
    # Fallback to default bitmap font
    try:
        font = ImageFont.load_default()
        if raw:
            return (pathlib.Path("<default>"), b"bitmap-default")
        return font
    except Exception:
        return None

if __name__ == "__main__":
    raise SystemExit(main())
