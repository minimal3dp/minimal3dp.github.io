# Dev.to Cross-Posting Setup

This project supports manual Dev.to cross-posting via a GitHub Actions workflow and a Python helper script. Use this to selectively syndicate high‑value evergreen guides while preserving SEO authority through canonical URLs.

## Why Dev.to
- Active developer audience; tags aid discovery.
- API still supports authenticated publishing (unlike Medium tokens which were discontinued).
- Canonical link parameter ensures original site remains the SEO source of truth.

## Overview
Two components enable Dev.to posting:
1. `scripts/post_to_devto.py` – Parses Hugo front matter, simplifies certain shortcodes, builds canonical footer, and calls Dev.to API.
2. `.github/workflows/post-to-devto.yml` – Manually dispatched workflow that runs the script with chosen publish status (`draft`, `public`, or `unlisted`).

## Prerequisites
1. Dev.to account
2. API key (Personal) from Dev.to settings
3. GitHub repository secret: `DEVTO_API_KEY`
4. Existing Hugo post with front matter including at minimum:
   ```yaml
   ---
   title: "Flow Calibration Guide"
   date: 2025-01-12
   tags: ["klipper", "3dprinting", "calibration", "extrusion"]
   description: "Accurate flow calibration procedure for FDM printers"
   ---
   ```

## Creating a Dev.to API Key
1. Log in to Dev.to.
2. Navigate: `Settings` → `Account` → "DEV API Keys".
3. Generate a new key; copy it immediately.
4. Add to GitHub repo secrets as `DEVTO_API_KEY`.

## Allowed Tags Guidance
Dev.to permits up to 4 main tags (extra are ignored). Choose the most specific and high‑signal tags:
- General 3D printing: `3dprinting`
- Firmware: `klipper`
- Hardware builds: `3dprinter`
- Calibration topics: `calibration`, `tuning`
Prioritize: 1) Domain (3dprinting) 2) Firmware/Tool (klipper/orcaslicer) 3) Process (calibration/tuning) 4) Specific technique (pressureadvance, inputshaping). Adjust per post.

## Canonical URL Handling
The script infers the canonical URL from the site base + post path. Dev.to article is marked with `canonical_url` retaining search engine preference for original content.

## Workflow Dispatch Usage
1. Go to GitHub → `Actions` → `Post to Dev.to` workflow.
2. Click "Run workflow".
3. Inputs:
   - `post_path`: e.g. `content/blog/posts/flow-calibration/index.md`
   - `publish_status`: one of `draft`, `public`, `unlisted`
4. Run → On success you receive email notification (if SMTP secrets configured). Output includes Dev.to URL.

## Local Dry Run
You may test locally before public posting:
```bash
DEVTO_API_KEY=your_key_here uv run python scripts/post_to_devto.py \
  content/blog/posts/flow-calibration/index.md --publish draft
```
Expect output with created article URL. Remove the article from Dev.to if test only.

## Shortcode Conversion Notes
The script currently performs basic conversions for image and simple content blocks. Complex interactive shortcodes (e.g., calibration tools) are appended as plain markdown links. Review final Dev.to draft for formatting integrity before publishing.

## Error Handling
- Missing API key → script raises `ValueError`.
- Dev.to non-2xx response → script raises `RuntimeError` with status code.
- Workflow surfaces failures via email (subject starts with ❌) when SMTP is configured; otherwise check Actions logs.

## Recommended Cross-Post Criteria
Post only when ALL apply:
- Content is evergreen (expected to be valid ≥ 12 months).
- Original post has internal links established (retain user journey).
- Adds non-trivial value beyond already saturated topics (e.g., includes unique calibration data or methodology).

## Post-Publish Checklist
- Verify canonical link present (Dev.to UI under "...