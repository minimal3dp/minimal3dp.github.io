"""Fetch YouTube channel subscriber count and expose it to Hugo.

Outputs:
  data/youtube_channel.json        (Hugo .Site.Data access)
  static/data/youtube_channel.json (Client-side fetch, optional)

Environment Variables:
  YOUTUBE_API_KEY      (required)
  YOUTUBE_CHANNEL_ID   (defaults to channel ID if unset)

Usage:
  YOUTUBE_API_KEY=XXXX uv run python scripts/fetch_youtube_subscribers.py

Exit codes:
  0 success
  1 error (missing config or API failure)
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID", "UCM_8Mv-0S1LnnJpRJLjahaw")
DATA_PATH = "data/youtube_channel.json"
STATIC_PATH = "static/data/youtube_channel.json"

def fetch_subscribers(api_key: str, channel_id: str) -> int:
    youtube = build("youtube", "v3", developerKey=api_key)
    resp = youtube.channels().list(part="statistics", id=channel_id).execute()
    items = resp.get("items", [])
    if not items:
        raise RuntimeError(f"Channel not found: {channel_id}")
    stats = items[0].get("statistics", {})
    subs = stats.get("subscriberCount")
    if subs is None:
        raise RuntimeError("Subscriber count hidden or unavailable")
    return int(subs)

def write_json(path: str, payload: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

def main() -> int:
    if not API_KEY:
        print("ERROR: YOUTUBE_API_KEY not set", file=sys.stderr)
        return 1
    if not CHANNEL_ID:
        print("ERROR: YOUTUBE_CHANNEL_ID not set", file=sys.stderr)
        return 1
    try:
        count = fetch_subscribers(API_KEY, CHANNEL_ID)
    except HttpError as e:
        print(f"ERROR: YouTube API error: {e}", file=sys.stderr)
        return 1
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    rounded_thousands = (count // 1000) * 1000 if count >= 1000 else count
    display = f"{rounded_thousands}+" if count >= 1000 else str(count)
    payload = {
        "channelId": CHANNEL_ID,
        "subscriberCount": count,
        "subscriberCountRounded": rounded_thousands,
        "subscriberCountDisplay": display,
        "fetchedAt": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "updateFrequency": "weekly",
    }
    write_json(DATA_PATH, payload)
    write_json(STATIC_PATH, payload)
    print(
        "✓ Subscriber count: "
        f"{count:,} (rounded display: {display}) "
        f"(written to {DATA_PATH} & {STATIC_PATH})"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
