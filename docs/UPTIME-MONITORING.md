# Uptime & Performance Monitoring

This document outlines adding external uptime checks and how they complement Lighthouse CI performance audits.

## Uptime Monitoring Services

Recommended providers:
- UptimeRobot (free tier + 5‑min checks)
- Better Uptime (incident & on‑call features)
- Pingdom (paid, detailed RUM)

### What to Monitor
- Primary site URL (https://minimal3dp.com)
- JSON data endpoints (e.g. https://minimal3dp.com/data/popular.json)
- Redirect health (optional: legacy URLs → new paths)

### Steps (UptimeRobot Example)
1. Create account at https://uptimerobot.com
2. Add HTTP monitor: URL = site root, interval = 5 minutes.
3. Add secondary monitors for data endpoints (optional).
4. Configure alert contacts (email; match `TO_EMAIL` used in workflows if desired).
5. Enable status page (optional) and place link in README or footer if public.

### Alert Tuning
- Start with email only; SMS/phone escalation usually unnecessary at current scale.
- Add maintenance windows before planned downtime (e.g. major refactors).

## Integration With Repository
No code changes required; uptime checks operate externally.

Optional additions:
- Badge in `README.md` (link to status page)
- Monthly review: correlate downtime events with workflow runs.

## Performance Audits (Lighthouse CI)
The deploy workflow now runs Lighthouse CI against the built static site (`public/`). Scores are asserted (warn threshold 0.9). Reports are uploaded as an artifact (`lighthouse-report`).

### Improving Scores
- Optimize images (WebP + LQIP: implemented for fallback thumbnails).
- Minify/treeshake JS (Docsy assets already optimized; audit custom scripts).
- Reduce unused CSS (evaluate critical path extraction if scores dip).

## Quota / Error Considerations
If data endpoints fail (e.g., API quota exhausted) uptime remains green but Lighthouse may flag content shifts. Consider adding synthetic check ensuring JSON returns valid schema.

## Next Enhancements
- Add Lighthouse budgets (bundle size thresholds)
- Integrate status page badge
- Synthetic check for `youtube_popular.json` freshness
