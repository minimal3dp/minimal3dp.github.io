# Shortcodes & Partials Documentation

**Last Updated:** November 19, 2025  
**Purpose:** Reference guide for all custom Hugo shortcodes and partials used in the Minimal 3DP site.

---

## Table of Contents

- [Shortcodes](#shortcodes)
  - [Content Shortcodes](#content-shortcodes)
  - [Klipper Calibration Calculators](#klipper-calibration-calculators)
  - [Marketing & CTAs](#marketing--ctas)
- [Partials](#partials)
  - [Layout Partials](#layout-partials)
  - [GA4 Event Tracking](#ga4-event-tracking)

---

## Shortcodes

### Content Shortcodes

#### `imgproc`
**Function:** Process and display images from page resources with responsive sizing and captions.

**Parameters:**
- `0` (positional): Image filename/pattern
- `1` (positional): Processing command (`Fit`, `Fill`, `Resize`, `Crop`)
- `2` (positional): Dimensions (e.g., `500x500`, `800x600`)
- Inner content: Optional caption text

**Usage:**
```markdown
{{< imgproc my-image Fill "500x500" >}}
This is the image caption with optional **markdown**.
{{< /imgproc >}}
```

**Output:** Responsive card with processed image, width/height attributes, and styled caption.

---

#### `youtube-embed`
**Function:** Embed YouTube videos with subscribe CTA and privacy-enhanced mode.

**Parameters:**
- `id` (required): YouTube video ID
- `title` (optional): Video title for accessibility (default: "YouTube Video")

**Usage:**
```markdown
{{< youtube-embed id="v_cHEOeFav8" title="Mastering Bed Types in OrcaSlicer" >}}
```

**Output:** 16:9 responsive iframe with no-cookie domain, subscribe button, and GA4 tracking.

---

#### `alert`
**Function:** Display styled alert boxes with icons.

**Parameters:**
- `type` (optional): `info` (default), `warning`, `success`, `danger`, `tip`
- Inner content: Alert message (supports markdown)

**Usage:**
```markdown
{{< alert type="warning" >}}
**Important:** Always calibrate after hardware changes!
{{< /alert >}}
```

**Output:** Color-coded alert with icon and border accent.

---

#### `faq` + `faq-item`
**Function:** Create FAQ sections with Schema.org structured data for SEO.

**Parameters (faq):**
- Inner content: Multiple `faq-item` shortcodes

**Parameters (faq-item):**
- `question` (required): Question text
- Inner content: Answer (supports markdown)

**Usage:**
```markdown
{{< faq >}}
  {{< faq-item question="What is Klipper?" >}}
  Klipper is a 3D printer firmware that runs on a Raspberry Pi.
  {{< /faq-item >}}
  
  {{< faq-item question="Why use OrcaSlicer?" >}}
  OrcaSlicer offers advanced features like calibration tools and bed type automation.
  {{< /faq-item >}}
{{< /faq >}}
```

**Output:** Styled FAQ list + JSON-LD schema for rich snippets.

---

#### `tabpane`
**Function:** Create tabbed content sections (inherited from Docsy theme).

**Parameters:**
- `persist` (optional): `header`, `lang`, or `disabled` (controls tab persistence)
- `text` (optional, boolean): Render content as plain text instead of code
- `langEqualsHeader` (optional, boolean): Use header as language
- `right` (optional, boolean): Align tabs to the right

**Usage:**
```markdown
{{< tabpane persist="header" >}}
  {{< tab header="Python" lang="python" >}}
print("Hello World")
  {{< /tab >}}
  {{< tab header="JavaScript" lang="js" >}}
console.log("Hello World");
  {{< /tab >}}
{{< /tabpane >}}
```

**Output:** Bootstrap-styled tabs with syntax highlighting and optional persistence across page loads.

---

#### `product-compare`
**Function:** Display product comparison tables with affiliate links.

**Parameters:**
- Inner content: Markdown table

**Usage:**
```markdown
{{< product-compare >}}
| Feature | Product A | Product B |
|---------|-----------|-----------|
| Price | $100 | $150 |
| Quality | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Buy | [Amazon](link1) | [Amazon](link2) |
{{< /product-compare >}}
```

**Output:** Styled comparison table with hover effects.

---

### Klipper Calibration Calculators

#### `flow-calibration`
**Function:** Interactive calculator for flow rate calibration.

**Parameters:** None (self-contained form)

**Usage:**
```markdown
{{< flow-calibration >}}
```

**Inputs:**
- Nozzle diameter
- 4 wall thickness measurements

**Output:** Average measurement and calculated flow rate percentage.

---

#### `pressure-advance`
**Function:** Calculate pressure advance values for direct drive and Bowden extruders.

**Parameters:** None

**Usage:**
```markdown
{{< pressure-advance >}}
```

**Inputs:**
- Start value
- Measured height from test print
- Direct Drive Factor (0.005)
- Bowden Factor (0.02)

**Output:** Calculated pressure advance values for both extruder types.

---

#### `input-shaping`
**Function:** Calculate input shaping frequencies from ringing tower tests.

**Parameters:** None

**Usage:**
```markdown
{{< input-shaping >}}
```

**Inputs:**
- Print speed
- X/Y ring counts
- X/Y caliper measurements

**Output:** X and Y frequency values for `printer.cfg`.

---

#### `rotational-distance`
**Function:** Calculate extruder rotational distance.

**Parameters:** None

**Usage:**
```markdown
{{< rotational-distance >}}
```

**Inputs:**
- Initial mark distance (default 70mm)
- Requested extrude distance (default 50mm)
- Measured extrude distance
- Previous rotational distance

**Output:** New rotational distance value.

---

#### `lead-screw-rotation-distance`
**Function:** Calculate Z-axis lead screw rotation distance.

**Parameters:** None

**Usage:**
```markdown
{{< lead-screw-rotation-distance >}}
```

**Inputs:**
- Pitch (default 2mm)
- Number of threads (default 1)

**Output:** Lead screw rotation distance.

---

#### `max-volumetric-speed`
**Function:** Calculate maximum volumetric flow rate from calibration tower.

**Parameters:** None

**Usage:**
```markdown
{{< max-volumetric-speed >}}
```

**Inputs:**
- Start value
- Height measured
- Step value

**Output:** Max flow value at 100%, 95%, and 90%.

---

#### `run-current`
**Function:** Calculate stepper motor run current from peak current.

**Parameters:** None

**Usage:**
```markdown
{{< run-current >}}
```

**Inputs:**
- Peak current (from motor spec sheet)
- RMS Factor (0.707, disabled)

**Output:** Run current for `printer.cfg`.

---

#### `x-and-y-offsets`
**Function:** Calculate probe X/Y offsets from toolhead measurements.

**Parameters:** None

**Usage:**
```markdown
{{< x-and-y-offsets >}}
```

**Inputs:**
- Toolhead X/Y probe positions
- Toolhead X/Y nozzle positions

**Output:** X and Y offset values.

---

### Marketing & CTAs

#### `cta`
**Function:** Display call-to-action blocks (YouTube, calculator, email, support, app).

**Parameters:**
- `type` (required): `youtube`, `calculator`, `email`, `support`, `app`
- `location` (optional): Tracking label (default: `content`)
- `href` (optional, for calculator/app): Custom URL
- `btnText` (optional): Custom button text
- `title` (optional): Custom heading
- `ctaType` (optional): Override tracking type
- Inner content: Custom message text (supports markdown)

**Usage:**
```markdown
{{< cta type="youtube" location="blog-post" >}}
Subscribe for weekly Klipper tutorials!
{{< /cta >}}

{{< cta type="calculator" href="/tools/m3dp-fdm-cost-calculator/" btnText="Calculate Costs" >}}
Estimate your print costs accurately.
{{< /cta >}}
```

**Output:** Styled CTA box with icon, text, button, and GA4 tracking.

---

#### `cta-badge`
**Function:** Inline badge-style link with tracking (smaller than full CTA).

**Parameters:**
- `type` (optional): `app`, `calculator` (default: `calculator`)
- `href` (required): Link URL
- `label` (optional): Button text (default: "Open")
- `ctaType` (optional): Custom tracking type
- `location` (optional): Tracking label (default: `content`)

**Usage:**
```markdown
{{< cta-badge type="app" href="https://settings.minimal3dp.com" label="Open Settings Assistant" >}}
```

**Output:** Inline badge link with GA4 click tracking.

---

#### `amazon-product`
**Function:** Display affiliate product cards with Amazon Associates links.

**Parameters:**
- `asin` (required): Amazon product ASIN
- `title` (required): Product name
- `price` (optional): Display price
- `image` (optional): Product image path
- Inner content: Product description (supports markdown)

**Usage:**
```markdown
{{< amazon-product asin="B0XXXXXX" title="BTT SKR Mini E3 V3" price="$39.99" image="/images/products/skr-mini.jpg" >}}
Popular Klipper-compatible control board with TMC2209 drivers included.
{{< /amazon-product >}}
```

**Output:** Product card with image, description, affiliate button, and disclosure. Tracks clicks via GA4.

---

#### `popular-posts`
**Function:** Insert popular posts widget from GA4 data.

**Parameters:**
- `count` (optional): Number of posts (default: 5)
- `title` (optional): Widget heading (default: "Popular Posts")
- `section` (optional): Data section key (default: `global`)

**Usage:**
```markdown
{{< popular-posts count="3" title="Top Read This Week" >}}
```

**Output:** List of popular posts with view counts from `data/popular.json`.

---

#### `popular-videos`
**Function:** Display most popular YouTube videos from channel.

**Parameters:**
- `count` (optional): Number of videos (default: 3)

**Usage:**
```markdown
{{< popular-videos count="3" >}}
```

**Data Source:**
1. `data/youtube_popular.json` (live YouTube API data)
2. `data/popular.json` global posts (fallback)
3. `data/youtube_popular_fallback.json` (curated fallback)

**Output:** Responsive grid of video cards with thumbnails (WebP + LQIP for fallback images), titles, view counts, like counts, and play overlay. Auto-tracks clicks.

---

## Partials

### Layout Partials

#### `youtube-subscribe-cta.html`
**Function:** Display YouTube subscribe CTA box with dynamic subscriber count.

**Usage:**
```go-html-template
{{ partial "youtube-subscribe-cta.html" . }}
```

**Data Sources:**
- `site.Data.youtube_channel.subscriberCountDisplay` (dynamic, weekly refresh)
- `site.Params.youtube_subscribers` (fallback static count)

**Output:** Red gradient box with YouTube icon, subscriber count, subscribe button, and GA4 tracking.

---

#### `popular-posts.html`
**Function:** Render popular posts widget (backend for `popular-posts` shortcode).

**Parameters (via dict):**
- `count`: Number of posts
- `title`: Widget heading
- `section`: Data section key (`global`, `blog`, etc.)

**Data Format:**
```json
{
  "global": [
    {"title": "Post Title", "url": "/path/", "views": 1234}
  ]
}
```

**Output:** Unordered list of popular posts with view counts.

---

#### `head.html`
**Function:** Site-wide `<head>` section with meta tags, CSS, analytics, and hooks.

**Features:**
- SEO meta tags (robots, description, Open Graph, Twitter Cards)
- Schema.org markup
- Google Analytics (GA4) with cross-domain linker
- jQuery and Lunr.js (for offline search)
- Prism syntax highlighting (optional)
- Algolia DocSearch (optional)
- Favicon partial
- `head-end.html` hook for custom scripts

**Cross-Domain Tracking:**
Automatically links sessions between `minimal3dp.com` and `settings.minimal3dp.com` for unified GA4 reporting.

---

### GA4 Event Tracking

#### `hooks/head-end.html`
**Function:** Centralized GA4 event tracking library with automatic listeners.

**Manual Tracking Functions:**

```javascript
trackAffiliateClick(asin, title)
trackYouTubeSubscribe(source)
trackYouTubeVideo(videoId, title)
trackRelatedPostClick(postTitle, postUrl)
trackCalculatorUse(calculatorName, action)
trackEmailSignup(formLocation, listType)
trackVideoPlay(videoId, videoTitle)
trackCtaClick(ctaType, location)
trackSiteSearch(searchQuery, resultsCount)
trackOutboundLink(url, linkText)
trackFileDownload(fileName, fileType)
```

**Automatic Tracking:**
- Affiliate links (`rel="sponsored"`) → `affiliate_click`
- External links (`target="_blank"` or different domain) → `click` (outbound)
- File downloads (`.pdf`, `.stl`, `.gcode`, `.zip`, `.cfg`, `.json`, `.txt`, `.csv`) → `file_download`

**Event Categories:**
- Amazon (affiliate)
- YouTube (subscribe, video)
- Related Posts
- Tools (calculators)
- Lead Generation (email)
- Video Engagement
- CTA
- Download
- Outbound Link

**Usage:**
All shortcodes and partials automatically call these functions. Manual usage:

```html
<button onclick="trackCalculatorUse('fdm-cost', 'calculate')">Calculate</button>
```

**Console Logging:**
All events log to browser console for debugging in development.

---

## Shortcode Dependencies

### JavaScript Files (in `static/js/`)
- `flow-calibration.js`
- `pressure-advance.js`
- `input-shaping.js`
- `rotational-distance.js`
- `lead-screw-rotation-distance.js`
- `max-volumetric-speed.js`
- `run-current.js`
- `x-and-y-offsets.js`
- `tabpane-persist.js` (for tabpane persistence)

### Data Files (in `data/`)
- `popular.json` – GA4 popular pages data
- `youtube_popular.json` – YouTube Data API popular videos
- `youtube_popular_fallback.json` – Curated fallback videos
- `youtube_channel.json` – Subscriber count (weekly refresh)

### Site Parameters (in `hugo.toml`)
- `youtube_channel_id` – Channel ID for subscribe links
- `youtube_subscribers` – Static subscriber count fallback
- `affiliate_tag` – Amazon Associates tracking ID (default: `mwf064-20`)

---

## Best Practices

### Using Shortcodes
1. **Always provide required parameters** – Check documentation for mandatory fields.
2. **Use descriptive titles** – Improves accessibility and SEO.
3. **Leverage inner content** – Most shortcodes support markdown for rich formatting.
4. **Track CTAs properly** – Pass meaningful `location` params for analytics segmentation.

### Tracking Events
1. **Use consistent naming** – Keep `location` and `ctaType` params standardized across pages.
2. **Check console logs** – Verify events fire correctly during development.
3. **Avoid duplicate tracking** – Automatic listeners handle most cases; manual calls should be rare.

### Data Files
1. **Never edit manually** – Data files are generated by GitHub Actions workflows.
2. **Check freshness** – Workflows run daily/weekly; expect data lag.
3. **Provide fallbacks** – Design shortcodes to gracefully handle missing data.

---

## Maintenance Notes

### Adding New Shortcodes
1. Create `.html` file in `layouts/shortcodes/`
2. Add parameter validation and error handling
3. Include usage comment block at top of file
4. Create corresponding JS file if interactive
5. Add GA4 tracking if user action involved
6. Document here with examples

### Adding New Partials
1. Create `.html` file in `layouts/partials/`
2. Define expected parameters via dict or context
3. Add fallback logic for missing data
4. Document usage and data dependencies here

### Updating Calculators
1. Edit HTML form in `layouts/shortcodes/`
2. Update calculation logic in corresponding `static/js/` file
3. Add GA4 tracking call to submit button
4. Test with various input ranges
5. Update Klipper calibration docs if formula changes

---

## Related Documentation

- [README.md](../README.md) – Workflow automation and setup
- [YOUTUBE-SETUP.md](YOUTUBE-SETUP.md) – YouTube Data API configuration
- [SMTP-SETUP.md](SMTP-SETUP.md) – Email notification setup
- [UPTIME-MONITORING.md](UPTIME-MONITORING.md) – External monitoring guide
- [.github/copilot-instructions.md](../.github/copilot-instructions.md) – AI agent guidelines

---

**Questions or Issues?**  
Open an issue on GitHub or consult the Hugo/Docsy documentation for template syntax.

**Maintained by:** Mike Wilson + GitHub Copilot  
**Review Frequency:** Update after adding/modifying shortcodes or partials
