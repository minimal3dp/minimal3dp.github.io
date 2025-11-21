# Minimal 3DP

Based on Docsy template

## Update Template

```bash
hugo mod get -u github.com/google/docsy@v0.12.0
```

## Python Environment

This project uses [uv](https://docs.astral.sh/uv/) for Python dependency management.

```bash
# Install dependencies
uv sync

# Run scripts
uv run python scripts/fetch_ga4_popular.py
uv run python scripts/fetch_youtube_popular.py
```

## Run in Dev

```bash
hugo server -D
```

## Run in Prod

```bash
hugo
```
 - Dev.to Cross-Posting: Supported via manual dispatch workflow + script. See `docs/DEVTO-SETUP.md` for API key, tagging, canonical URL, and publishing guidance.
- Setup guides: see `docs/` folder for SMTP, recommendations, and archived notes.
- YouTube Popular Videos: see `docs/YOUTUBE-SETUP.md` for API key creation, secrets, workflow, and troubleshooting.
- Medium Cross-Posting (Deprecated): Medium removed integration tokens; automation disabled. See `docs/MEDIUM-SETUP.md` for manual cross-post guidance and alternatives.

## Workflow Notifications

All automated workflows now use email-only notifications (Slack removed). Success and failure emails are sent when full SMTP configuration is present. See below.

## Email Notifications

Email notifications are implemented for all data and deploy workflows (success + failure). Add these repository secrets:

- `SMTP_SERVER` (e.g. smtp.sendgrid.net)
- `SMTP_PORT` (e.g. 587)
 | `post-to-devto.yml` | Manual Dev.to cross-post (draft/public) | Manual dispatch | Dev.to article (canonical) |
- `SMTP_USERNAME` (SMTP auth user)
- `SMTP_PASSWORD` (SMTP auth password/token)
- `FROM_EMAIL` (sender address)
- `TO_EMAIL` (comma-separated recipients)

On success you receive a summary; on failure an alert with run URL. If any secret is missing the email step is skipped safely.

Detailed provider-specific instructions: see `docs/SMTP-SETUP.md`.
DEVTO_API_KEY=YOUR_KEY uv run python scripts/post_to_devto.py content/blog/posts/flow-calibration/index.md --publish draft

### Optional SMTP Smoke Test
If you maintain a separate test workflow, run it after setting secrets to verify connectivity. (The prior Slack section is deprecated and intentionally removed.)

## Automated Data Fetch Workflows

| Workflow | Purpose | Schedule | Output |
|----------|---------|----------|--------|
| `fetch-popular.yml` | GA4 page popularity (global + sections) | Daily 03:05 UTC | `data/popular.json` + `static/data/popular.json` |
| `fetch-youtube-popular.yml` | YouTube channel top videos (recent window) | Daily 03:15 UTC | `data/youtube_popular.json` + `static/data/youtube_popular.json` |
| `fetch-youtube-subscribers.yml` | Channel subscriber count | Weekly Mon 03:12 UTC | `data/youtube_channel.json` + `static/data/youtube_channel.json` |
| `deploy-site.yaml` | Build & publish Hugo site to `gh-pages` | On push to `main` | Public site |
| (Removed) `post-to-medium.yml` | Deprecated Medium cross-post (no API tokens) | N/A | N/A |

Each workflow includes an email config detection step; if any required secret is missing notification steps are skipped.

### Manual Dispatch
From GitHub Actions UI select the workflow → "Run workflow" → use defaults. Useful after editing scripts or adjusting secrets.

### Local Reproduction
```bash
uv run python scripts/fetch_ga4_popular.py
uv run python scripts/fetch_youtube_popular.py
YOUTUBE_API_KEY=YOUR_KEY YOUTUBE_CHANNEL_ID=UCM_8Mv-0S1LnnJpRJLjahaw \
	uv run python scripts/fetch_youtube_subscribers.py
hugo --minify
```
