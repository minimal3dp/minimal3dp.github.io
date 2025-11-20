# Medium Cross-Post Guide (Automation Deprecated)

**Purpose:** Cross-post Hugo blog content to Medium with canonical URLs pointing back to minimal3dp.com.

Medium has discontinued issuing new integration tokens / API keys for direct publishing. As a result, prior automation scripts and workflows have been **removed**. This guide now focuses on safe, manual cross-posting and viable alternatives (Dev.to, Hashnode) while preserving SEO via canonical links.

---

## Current Status

Previous components (script + workflow) were removed in November 2025 once token issuance was deprecated. Manual copy/paste is now required.

**Manual Cross-Post Advantages:**
- ✅ Full editorial control per platform
- ✅ Selective promotion of evergreen guides
- ✅ Opportunity to tailor intro and CTA for Medium audience
- ✅ Avoid accidental duplication of affiliate-heavy content

**Manual Limitations:**
- ❌ No automated publish pipeline
- ❌ Requires manual formatting adjustments (shortcodes, embeds)
- ❌ Higher time cost per post

---

## Manual Cross-Post Workflow

### 1. Choose Candidate Post
Select a post that is:
- Evergreen (e.g. calibration guide, tutorial)
- Useful to broad audience (not narrow printer-specific minutiae)
- Already indexed (wait 48–72h after publishing on minimal3dp.com)

### 2. Prepare Markdown
1. Open original `index.md`
2. Remove / simplify Hugo shortcodes:
    - `{{< youtube-embed id="..." >}}` → Raw YouTube link or Medium embed dialog
    - `{{< imgproc image.jpg Fit "800x" >}}` → `![Alt text](https://minimal3dp.com/blog/posts/slug/image.jpg)`
    - Remove calculators / dynamic blocks (popular-videos, cta, faq)
3. Keep headings, lists, code blocks

### 3. Add Canonical URL
At the bottom of the Medium editor, toggle advanced options and set:
```
Canonical link: https://minimal3dp.com/blog/posts/<slug>/
```
If Medium removes or ignores it, re-add after publish (sometimes a second save persists it).

### 4. Adapt Intro for Medium
Add 1–2 sentence platform-tailored intro, e.g.:
"This guide originally appeared on Minimal 3DP where we publish data-driven calibration workflows—here’s the distilled version for Medium readers."

### 5. Add End Footer
Append:
```
---
Originally published at Minimal 3DP: https://minimal3dp.com/blog/posts/<slug>/
Explore more Klipper & OrcaSlicer guides at https://minimal3dp.com/klipper-calibration/
```

### 6. Publish Strategy
- First publish as **Draft**
- Proof formatting (images, embeds, spacing)
- Switch to **Public** once canonical confirmed
- Promote selectively (avoid simultaneous Reddit & Medium blasts to measure channel value)

### Optional: Semi-Structured Conversion
Use a local helper script (not committed) to strip shortcodes:
```bash
grep -v '{{<' content/blog/posts/<slug>/index.md > /tmp/medium.md
```
Then manually restore images and embeds.

## Shortcode Handling (Manual)

### 4. Test Locally (Optional)

```bash
# Set your Medium token
export MEDIUM_API_TOKEN="your_token_here"

# Test posting a draft
python scripts/post_to_medium.py content/blog/posts/orcaslicer-bed-types/index.md
```

This will post to Medium as a draft. Check your Medium drafts to verify.

---

## How to Use

### Embeds
- **YouTube:** Paste raw URL; Medium auto-converts.
- **Amazon / affiliate links:** Consider omitting—Medium may suppress or reduce distribution.

### Via Command Line (Local)

```bash
# Make sure token is set
export MEDIUM_API_TOKEN="your_token_here"

# Post as draft (default)
python scripts/post_to_medium.py content/blog/posts/my-post/index.md

# The script automatically detects if post is published on your site
# and uses that to determine Medium publish status
```

---

## What Gets Converted

### Shortcodes → HTML/Markdown

| Hugo Shortcode | Medium Output |
|---|---|
| `{{< youtube-embed id="..." >}}` | `<iframe>` embed |
| `{{< imgproc ... >}}` | `![Image](absolute-url)` |
| `{{< alert >}}...{{< /alert >}}` | `> Blockquote` |
| `{{< popular-videos >}}` | Removed (replaced with note) |
| `{{< cta >}}...{{< /cta >}}` | Removed |
| `{{< faq >}}...{{< /faq >}}` | Removed |

### Front Matter Handling

- **Title:** Used as Medium post title
- **Tags:** First 5 tags transferred to Medium
- **Draft:** If `draft: true`, posts as draft on Medium
- **Featured image:** Not transferred (Medium uses first image in content)
- **Description:** Not used (Medium generates excerpt)

### Automatic Additions

Every post gets:

1. **Canonical URL** pointing to `https://minimal3dp.com/blog/posts/{slug}/`
2. **Footer** with link: *"Originally published at minimal3dp.com"*

---

## Best Practices

### When to Cross-Post to Medium

✅ **Good candidates:**
- Tutorial/how-to posts with broad appeal
- Beginner-friendly content
- Posts without heavy affiliate links
- Content that can stand alone without site-specific features

❌ **Avoid cross-posting:**
- Product review posts (affiliate revenue stays on your site)
- Posts heavily using custom shortcodes/calculators
- Time-sensitive content (deals, announcements)
- Posts with complex layouts

### Publishing Strategy

1. **Publish on your site first** - Let it index and rank for a few days
2. **Cross-post as draft** - Review formatting on Medium
3. **Publish on Medium** - Only after your site has indexed
4. **Monitor canonical tag** - Ensure Medium respects it

### SEO Considerations

- ✅ Canonical URL protects your site from duplicate content penalties
- ✅ Medium readers discover your site via footer link
- ❌ Medium may rank higher than your site for some queries (even with canonical)
- ❌ You lose affiliate click opportunities on Medium version

**Recommendation:** Start with 1-2 evergreen posts and monitor traffic impact before scaling.

---

## Alternatives & Recommended Priorities

| Platform | Automation | API Available | Recommended Use |
|----------|------------|---------------|-----------------|
| Dev.to   | ✅ (API tokens) | Yes | Technical tutorials & config guides |
| Hashnode | ✅ (GitHub sync) | Yes | Broader developer audience & series |
| Medium   | ❌ (tokens removed) | Limited | Select evergreen, brand awareness |
| Reddit   | ❌ | N/A | Community engagement & feedback |
| Discord  | ❌ | N/A | Real-time Q&A and support |

**Suggested Order (2025):** 1) Dev.to selective cross-post → 2) Hashnode experiments → 3) Medium only for top evergreen guides.

### Workflow Inputs

| Input | Type | Description | Default |
|---|---|---|---|
| `post_path` | string | Path to markdown file | *required* |
| `publish_status` | choice | `draft`, `public`, or `unlisted` | `draft` |

---

## Troubleshooting

### "Medium removed canonical link"
Re-add it, save twice. If still missing, wait several hours; Medium sometimes delays propagation.

### "Error: File not found"

**Solution:** Check the path. Use tab-completion or copy from file tree. Example:
```
content/blog/posts/orcaslicer-bed-types/index.md
```

### "Error parsing front matter"

**Solution:** Ensure post has valid YAML front matter between `---` delimiters:
```yaml
---
title: "My Post Title"
date: 2025-11-20
---
```

### "Should I re-publish old posts?"
Only if they are still evergreen and not heavily affiliate-driven. Prioritize calibration and foundational workflow guides.

### "Post appears on Medium but canonical URL not working"

**Solution:** 
- Wait 24-48 hours for Medium to process
- Check Medium post source HTML for `<link rel="canonical">`
- Contact Medium support if it persists

### "Images not showing on Medium"

**Solution:** 
- Images must use absolute URLs
- Host images on your Hugo site (not local relative paths)
- Medium caches images on first load

---

## Platform Considerations

**Medium Pros:** Large built-in audience, occasional virality potential.
**Medium Cons:** Algorithm opacity, potential affiliate suppression, canonical sometimes flaky.

**Dev.to Pros:** Developer-focused, API posting possible, tags improve discovery.
**Hashnode Pros:** Custom domains, series organization, built-in newsletter tools.
**Reddit Pros:** Direct feedback loop; validates demand before deep content investment.

---

## Example Usage

### Example Selection Criteria

| Post | Cross-Post? | Reason |
|------|-------------|--------|
| Bed Types in OrcaSlicer | ✅ | Broad slicer audience |
| Pressure Advance Fine-Tuning | ✅ | Evergreen calibration |
| Affiliate-heavy printer review | ❌ | Revenue retention on site |
| Time-limited deal roundup | ❌ | Ephemeral value |

### Post K2 Plus Series (3 posts)

```bash
# Run workflow 3 times with different paths
content/blog/posts/k2-plus-upgrade-series-part-1/index.md
content/blog/posts/k2-plus-upgrade-series-part-2/index.md
content/blog/posts/k2-plus-upgrade-series-part-3/index.md

# All set to "public" after reviewing drafts
```

---

## Monitoring & Analytics

### Track Medium Traffic

In GA4, create custom report:

- **Dimension:** Medium referrer traffic
- **Metric:** Sessions, conversions from Medium
- **Goal:** Track how many Medium readers visit your site

### Medium Stats Dashboard

Medium provides built-in analytics:

- Views per post
- Read time
- Reader engagement
- Follower growth

**Access:** [Medium Stats](https://medium.com/me/stats)

---

## Advanced: Customizing Content Conversion

Automation code was removed; adjust content manually instead.

### Add Custom Shortcode Handler

```python
# Around line 60, add new regex replacement
content = re.sub(
    r'{{\s*<\s*my-shortcode[^>]*>\s*}}(.*?){{\s*</\s*my-shortcode\s*>\s*}}',
    r'Custom HTML or markdown here',
    content,
    flags=re.DOTALL
)
```

### Change Footer Format

```python
# Around line 90, modify footer text
footer = f"""
---
*Read more 3D printing guides at [minimal3dp.com]({canonical_url})*
"""
```

### Add Custom Tags

```python
# In main(), after line 240
# Force-add specific tags
if not tags:
    tags = []
tags.extend(['3D Printing', 'Klipper'])
```

---

## Ethical & Brand Notes

### Content Review

Before posting:

1. Check for personal information in post
2. Verify affiliate links are allowed by Medium ToS
3. Ensure images have proper permissions
4. Review that canonical URL is correct

---

## Alternatives Considered

### Why Not RSS Auto-Import?

- ❌ No control over timing
- ❌ Can't customize per-post
- ❌ No notification on success/failure

### Why Not Zapier/Make?

- ❌ Monthly subscription cost ($20+)
- ❌ Additional service to maintain
- ❌ Rate limits more restrictive

### Why Not Rebuild Automation?
Current options would require brittle scraping or unofficial libraries—high maintenance and risk of ToS violation. Manual publishing preserves stability and focus.

---

## Future Enhancements

Potential additions:

- [ ] Dev.to automated posting workflow (API token)
- [ ] Hashnode GitHub sync experiments
- [ ] Internal related-content generator for cross-linking hubs
- [ ] Post-performance tracking (referrer source segmentation)

---

## References

*Medium API docs retained for historical reference; functionality limited as of late 2025.*
- [Canonical URLs and SEO](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [GitHub Actions workflow_dispatch](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch)

---

**Questions or issues?** Open an issue in the repository.

**Maintained by:** Mike Wilson + GitHub Copilot  
**Last Updated:** November 20, 2025
