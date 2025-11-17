# Copilot Instructions (Minimal 3DP)

Purpose: enable AI agents to be productive quickly in this Hugo + Docsy site by following repo-specific patterns and workflows.

## Architecture
- Static site built with Hugo Extended + Docsy. Do not edit generated outputs in `public/` or `resources/_gen/`.
- Content lives under `content/` (Markdown). Features are implemented via shortcodes and partials in `layouts/`.
- Global analytics helpers are centralized in `layouts/partials/hooks/head-end.html` (GA4 + auto-listeners). Do not duplicate tracking code in pages.
- Styles are authored in SCSS under `assets/scss/`; avoid inline styles. Utility class `img-fluid` prevents image overflow.

## Workflows
- Dev server: `hugo server -D` (drafts enabled).
- Production build: `hugo --gc --minify`.
- Update Docsy: `hugo mod get -u github.com/google/docsy@v0.12.0` (see `README.md`).

## Local Development
- Check Hugo: `hugo version` (use Hugo Extended).
- Run with drafts: `hugo server -D` then open the local URL.
- Production-like build: `hugo --gc --minify` (outputs to `public/`).
- Do not edit `public/` or `resources/_gen/` — those are generated.

## Conventions
- Prefer shortcodes over raw HTML for common blocks: `imgproc`, `faq/faq-item`, `amazon-product`, `tabpane`, etc.
- Images: use `{{< imgproc >}}`; ensure alt text; rely on responsive classes instead of fixed sizes.
- CTAs/affiliates: use existing shortcodes and wire clicks to global GA helpers (e.g., `trackCtaClick`, `trackAffiliateClick`).
- JS: place feature code in `static/js/` or Hugo pipeline; keep bundles small and avoid duplicate listeners.

## Integration Points
- Analytics: GA4 helpers and auto-listeners in `head-end.html` handle outbound/download/affiliate events.
- Styling: extend `assets/scss/_styles_project.scss` for reusable component classes (e.g., affiliate cards, responsive images).
- Schema/SEO: use shortcode-based FAQs on key pages; centralized head partials add schema when needed.

## Examples (this repo)
- Responsive images: `layouts/shortcodes/imgproc.html` adds `img-fluid` for mobile.
- Affiliate product card: `layouts/shortcodes/amazon-product.html` uses class-based styles (no inline), tracked via global GA.
- Central tracking: `layouts/partials/hooks/head-end.html` defines event helpers and auto-binding.

## Prompt Efficiency & Cost-Awareness
- Goal: Minimize heavy/expensive model calls and token usage while preserving result quality.
- Feasibility: Flag prompts that request any of the following:
	- Complete dumps of large files or entire datasets
	- Extremely long code reviews (e.g., >2,000 lines) or multi-file refactors in one prompt
	- Full dataset transformations on millions of rows without a sample
	- Output of enormous binary blobs or large base64 content
- Actionable behavior when such prompts appear:
	- Politely notify the user the prompt appears expensive and explain the heuristic
	- Suggest concrete, lower-cost alternatives: split into steps, provide a small sample, generate a POC, or ask to confirm before proceeding
	- Include a succinct example of a more efficient prompt the user can copy/paste
- Example: If a user says “process 1M rows and return the full CSV”, recommend returning a small sample + code to run locally, or run an on-disk transformation script that writes a CSV instead of printing it.

### Example Efficient Prompts
- "Review only `layouts/shortcodes/cta.html` (~120 lines) for GA tracking compliance; propose minimal changes."
- "Generate a proof-of-concept that processes 1,000 rows from `data/sample.csv` and writes `out.csv` without printing the entire file."
- "Summarize only the public functions in `assets/js/main.js` and list potential event tracking hooks."

## Guardrails
- Do not modify `public/` outputs or `resources/_gen/` artifacts.
- Keep diffs surgical and scoped; include a brief rationale in PR descriptions.
- After template/partial changes, ensure `hugo --gc --minify` succeeds locally.
