# YouTube Popular Videos Setup

This guide explains how to enable automated fetching of your **most popular YouTube videos** for display on the homepage via the `popular-videos` shortcode.

## Overview
The workflow `fetch-youtube-popular.yml` runs daily (or manually) and executes `scripts/fetch_youtube_popular.py` to:
- Query your channel uploads via **YouTube Data API v3** (API Key auth)
- Collect basic statistics (views, likes, comments)
- Select top videos in the last `DAYS_AGO` window (default 180 days)
- Write `data/youtube_popular.json` and copy to `static/data/youtube_popular.json`
- Hugo exposes this as `site.Data.youtube_popular` for the shortcode.

## What You Get
- Dynamic thumbnails
- View / like / comment counts
- Automatic nightly refresh
- Graceful fallback message if data not yet fetched

## Prerequisites
- Google account
- A YouTube channel (with uploaded videos)
- Access to GitHub repository settings (to add secrets)
- (For local testing) [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

## 1. Create / Select a Google Cloud Project
1. Visit: https://console.cloud.google.com/
2. Click project selector → "New Project" (or reuse an existing one).
3. Give it a name like `minimal3dp-youtube`.

## 2. Enable YouTube Data API v3
1. In Cloud Console: "APIs & Services" → "Library".
2. Search: "YouTube Data API v3".
3. Click → Enable.

## 3. Create an API Key
1. "APIs & Services" → "Credentials" → "Create credentials" → **API key**.
2. Copy the generated key.
3. (Recommended) Click the key → **Restrict Key**:
   - Application restrictions: `HTTP referrers` or `IP addresses` (optional for server-side GitHub; can leave unrestricted initially). Avoid exposing the key client-side.
   - API restrictions: Select **YouTube Data API v3** only.
4. Save.

## 4. Add GitHub Repository Secrets
Go to GitHub → Repo → Settings → Secrets and variables → Actions → **New repository secret**.

Create:
- `YOUTUBE_API_KEY` = (the API key from step 3)
- `YOUTUBE_CHANNEL_ID` = Your channel ID (already in `hugo.toml`: `UCM_8Mv-0S1LnnJpRJLjahaw`). If omitted the script uses default.
- Optionally re-use existing `SLACK_WEBHOOK_URL`, `SMTP_*` secrets for notifications.

### Finding Your Channel ID
If you need it again:
1. Visit your channel page.
2. URL format: `https://www.youtube.com/channel/<CHANNEL_ID>`.
3. Copy `<CHANNEL_ID>`.

## 5. Manual Local Test (Optional)
You can run the fetch script locally before relying on the workflow.

```bash
# From repo root (macOS / Linux)
# Install dependencies with uv
uv sync

# Run the script
export YOUTUBE_API_KEY="AIzaSyB1jQXhyGibolxvZGHNDbPIm0TwPeEBatg"
export YOUTUBE_CHANNEL_ID="UCM_8Mv-0S1LnnJpRJLjahaw"
uv run python scripts/fetch_youtube_popular.py

# Inspect output
sed -n '1,160p' data/youtube_popular.json
```

Open the site with `hugo server -D` and verify the homepage "Popular Videos" section now shows thumbnails.

## 6. Trigger Workflow
After secrets are added:
1. GitHub → Actions → "Fetch Popular YouTube Videos".
2. Click **Run workflow**.
3. Inspect logs → confirm:
   - "Wrote X videos" line
   - JSON committed under `data/` and `static/data/` paths
4. Visit production or local build; verify updated videos.

## 7. Configuration
Environment variables (defined in workflow YAML):
- `MAX_VIDEOS` (default 3) – how many to display.
- `DAYS_AGO` (default 180) – lookback window for candidate videos.
- `OUTPUT_PATH` (default `data/youtube_popular.json`) – internal data file.

Adjust by editing `.github/workflows/fetch-youtube-popular.yml`.

## 8. Shortcode Usage
Already embedded on homepage:
```go-html-template
{{< popular-videos count="3" >}}
```
You can use a different count elsewhere.

## 9. Data Format
Example (`data/youtube_popular.json`):
```json
{
  "videos": [
    {
      "id": "VIDEO_ID",
      "title": "Title",
      "description": "Truncated description...",
      "thumbnail": "https://i.ytimg.com/vi/VIDEO_ID/hqdefault.jpg",
      "url": "https://www.youtube.com/watch?v=VIDEO_ID",
      "publishedAt": "2025-03-01T12:00:00Z",
      "viewCount": 12345,
      "likeCount": 456,
      "commentCount": 78
    }
  ],
  "fetched_at": "2025-11-19T20:45:00Z"
}
```

## 10. Troubleshooting
| Symptom | Cause | Fix |
|---------|-------|-----|
| `ERROR: YouTube API error: HttpError 403` | API not enabled or key restricted incorrectly | Re-enable API, remove restriction temporarily |
| Empty `videos` array | No uploads in range `DAYS_AGO` | Increase `DAYS_AGO` (e.g. 365) |
| Thumbnail broken | Missing higher-res variant | Script falls back to `hqdefault`; check video availability |
| Workflow no commit | No changes to JSON | Increase lookback or verify videos present |
| Rate/Quota warnings | Too many manual runs | Keep daily schedule; avoid rapid re-runs |

## 11. Quotas & Optimization
- The Data API has default quotas (10k units/day). This script uses simple endpoints (channels, playlistItems, videos) – typically < 200 units per run.
- Avoid adding heavy endpoints unless needed.

## 12. Extending Further
Feature | Approach | Notes
--------|----------|------
Watch time sorting | Requires **YouTube Analytics API** (OAuth) | Not implemented (API key insufficient)
Playlist-specific highlights | Filter by playlist ID | Add env var for playlist override
Caching | Persist prior JSON if API fails | Add fallback logic in script

## 13. Security Notes
- Do **not** expose the API key client-side; keep fetch server-side in GitHub Actions.
- Restrict key to YouTube Data API only.
- Rotate key annually or if compromised.

## 14. Maintenance Checklist
Task | Frequency
-----|----------
Review quotas | Quarterly
Rotate API key | Yearly
Update MAX_VIDEOS | As needed
Verify workflow success | Weekly

## 15. Support
If the workflow repeatedly fails, capture the error log and verify each step above. For advanced analytics (watch time, RPM, audience retention) you would need an OAuth flow which is intentionally out of scope to keep things simple.

---
**Done** – after completing steps 1–5 and running the workflow, your homepage will show real YouTube popularity with thumbnails.
