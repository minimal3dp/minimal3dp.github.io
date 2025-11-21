# Popular Posts Setup

This page describes how the "Popular posts" widget works and how to enable it on the site.

Server-side partial
- The site includes `layouts/partials/popular-posts.html` which reads from `data/popular.json` if present.
- If `data/popular.json` is not present, the partial falls back to a Hugo heuristic that sorts `blog` pages by `Params.popularity`.
- To render this partial at the end of each article, we included:

  `{{ partial "popular-posts.html" (dict "count" 5 "title" "Popular This Week") }}`

  in `layouts/blog/single.html`.

Client-side fallback
- A client-side script `assets/js/popular-posts.js` will try to fetch `/data/popular.json` and render a widget into an element with id `popular-posts-js`.
- This is useful if you want to load the widget asynchronously (no rebuild needed).

Automated updates
- The repo includes `scripts/fetch_ga4_popular.py` and a GitHub Action `/.github/workflows/fetch-popular.yml` to update `data/popular.json` periodically.
- You must provide two secrets in the repository's Settings → Secrets:
  - `GA4_PROPERTY_ID`: numeric GA4 property ID (like `1234567890`)
  - `GA4_SERVICE_ACCOUNT`: base64-encoded service account JSON with `analytics.data` permission.
  - `SECTIONS` (optional): comma-separated path prefixes to create per-section lists (default: `/blog/,/tools/,/projects/`). These will appear as keys in the output JSON (eg. `blog`, `tools`, `projects`).
- The Action will run daily and commit `data/popular.json` and `static/data/popular.json` so both server-side and client-side are updated.

GA4 Service Account Setup (step-by-step)
1. Create a service account
  - Open Google Cloud Console → IAM & Admin → Service Accounts
  - Create a new service account (name: minimal3dp-popular-fetch)
  - In the role, grant minimal access for analytics: "Viewer" is fine for the property, but restrict to Analytics Data API if available.

2. Enable the Analytics Data API
  - Go to APIs & Services → Library, search for "Google Analytics Data API" (not just "Analytics API") and enable it for your project
  - **Important**: This must be enabled for the same project that contains your service account
  - If you get a "SERVICE_DISABLED" error when testing, visit the activation URL provided in the error message

3. Add the service account to your GA4 property
  - In GA4: Admin → Property Access Management (the property you want analytics for)
  - Click the blue + button, add the service account email with "Viewer" or "Analyst" role

4. Create and download service account key
  - Back in Google Cloud → Service accounts → select account → Keys → Add Key → Create New Key → JSON
  - The browser downloads the JSON file. DO NOT commit this file to Git.

5. Create GitHub Secret(s)
  - Base64 encode the file:

```bash
# macOS
BASE64=$(base64 -i /path/to/service_account.json)
echo "$BASE64"

# Linux
BASE64=$(base64 -w 0 /path/to/service_account.json)
echo "$BASE64"
```

  - In GitHub repo: Settings → Secrets → Actions → New Repository Secret
    - Name: `GA4_SERVICE_ACCOUNT`, Value: base64 output from above
    - Name: `GA4_PROPERTY_ID`, Value: your GA4 property numeric id (found in Admin → Property Settings)

6. Optional: Test locally
  - First, install dependencies:
  
```bash
pip3 install -r scripts/requirements.txt
# or if you have a venv: .venv/bin/pip install -r scripts/requirements.txt
```

  - Export your credentials file path (for local testing):

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account.json
export GA4_PROPERTY_ID=123456789
python3 scripts/fetch_ga4_popular.py
# or if you have a venv: .venv/bin/python scripts/fetch_ga4_popular.py
```

  - After running, check `data/popular.json` is produced and looks correct
  - **Troubleshooting**: If you get "SERVICE_DISABLED" error, the Analytics Data API isn't enabled (see step 2)

  Per-section usage
  - The script now produces a map with keys for `global` and any `SECTIONS` you pass. For example:

  ```
  {
    "global": [ {title,url,views}, ... ],
    "blog": [ {title,url,views}, ... ],
    "tools": [ {title,url,views}, ... ]
  }
  ```

  - To show section-specific results in templates or shortcodes you can pass `section` like so:

    `{{ partial "popular-posts.html" (dict "count" 5 "section" "blog" "title" "Popular This Week") }}`

  Adding to Sidebar / Footer
  - Add the quick wrapper partials to the theme as follows:
    - Sidebar: `{{ partial "sidebar-popular.html" (dict "count" 5 "title" "Popular This Week" "section" "blog") }}`
    - Footer: `{{ partial "footer-popular.html" (dict "count" 3 "title" "Popular This Week") }}`

    Place these snippets into your theme partials (e.g., `layouts/partials/td-sidebar-menu.html` or `layouts/partials/footer.html`). Use the existing theme partials as the correct insertion point for the sidebar or footer. If you prefer a global footer insert, override `layouts/_default/baseof.html` and add the call near the end of `<footer>`.

Notes and tips
- If you prefer a SaaS-based approach, use a serverless endpoint or an external database to store counts; update `static/data/popular.json` there and partial will pick it up.
- If you only want a small, manually-curated list, keep `data/popular.json` locally and update when you like.
- The partial supports a `views` number; you can show it by configuring items in `data/popular.json` or by providing `.Params.popularity` in frontmatter.

Examples
- Add this shortcode to posts or templates: `{{< popular-posts count="3" title="Most read this week" >}}`

