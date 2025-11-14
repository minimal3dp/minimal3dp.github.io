# YouTube Integration Usage Guide

## Overview

This guide explains how to use the YouTube integration elements created for Minimal 3DP.

## Files Created

1. `/content/_templates/youtube-description.txt` - Template for YouTube video descriptions
2. `/layouts/partials/youtube-subscribe-cta.html` - Full CTA box for blog posts
3. `/layouts/partials/watch-on-youtube.html` - Compact badge for tutorials

---

## 1. YouTube Video Description Template

**Location:** `/content/_templates/youtube-description.txt`

**Usage:**
1. Copy the template content
2. Replace `[page-url]` with the actual blog post URL
3. Add your timestamps
4. Add product affiliate links if applicable
5. Paste into YouTube video description

**Example:**
```
🎯 Learn how to calibrate pressure advance in Klipper for perfect prints

📖 FULL WRITTEN GUIDE: https://minimal3dp.com/klipper-calibration/pressure-advance/

Get step-by-step instructions, additional tips, and downloadable resources on the website.

[... rest of template ...]

⏱️ TIMESTAMPS
━━━━━━━━━━━━━━━━━━━━━

0:00 - Introduction
1:30 - Finding your printer's settings
3:45 - Running the test
6:20 - Analyzing results
8:15 - Final calibration
```

---

## 2. YouTube Subscribe CTA (Full Box)

**Location:** `/layouts/partials/youtube-subscribe-cta.html`

**When to Use:**
- At the end of blog posts
- After tutorials
- In "About" pages
- Anywhere you want maximum visibility

**Usage in Markdown:**
```html
{{ partial "youtube-subscribe-cta.html" . }}
```

**What it looks like:**
- Red gradient background box
- YouTube icon
- "Watch on YouTube" heading
- Subscriber count (from hugo.toml)
- Large "Subscribe Now" button
- GA4 tracking included

**Requirements:**
- `youtube_channel_id` must be set in hugo.toml
- Optional: `youtube_subscribers` for display

---

## 3. Watch on YouTube Badge (Compact)

**Location:** `/layouts/partials/watch-on-youtube.html`

**When to Use:**
- At the top of tutorials
- Quick links to video versions
- Compact alternative to full CTA

**Usage in Markdown:**
```html
{{ partial "watch-on-youtube.html" (dict "videoId" "VIDEO_ID" "title" "Watch Tutorial") }}
```

**Parameters:**
- `videoId` (required): The YouTube video ID (e.g., "DJZnYB0IVCY")
- `title` (optional): Custom link text (default: "Watch on YouTube")

**Example:**
```html
{{ partial "watch-on-youtube.html" (dict "videoId" "DJZnYB0IVCY" "title" "Watch Full Tutorial") }}
```

**What it looks like:**
- Compact red badge
- YouTube icon
- Video title as link
- GA4 tracking included

---

## 4. YouTube Embed Shortcode (Already Created)

**Location:** `/layouts/shortcodes/youtube-embed.html`

**Usage in Markdown:**
```
{{< youtube-embed id="VIDEO_ID" title="Video Title" >}}
```

**What it includes:**
- Responsive 16:9 iframe
- YouTube nocookie domain (privacy-friendly)
- Automatic subscribe button below video
- GA4 tracking

**Example:**
```
{{< youtube-embed id="DJZnYB0IVCY" title="Professional Firmware for Ender 3 v2" >}}
```

---

## Recommended Content Structure

### For Tutorial Posts (with video):

```markdown
---
title: "Tutorial: Klipper Pressure Advance Calibration"
---

<!-- Top of post: Link to full video -->
{{ partial "watch-on-youtube.html" (dict "videoId" "ABC123" "title" "Watch Full Tutorial") }}

## Introduction
[Your tutorial content...]

## Step 1: Setup
[Content...]

<!-- Mid-post: Embed the actual video -->
{{< youtube-embed id="ABC123" title="Klipper Pressure Advance Tutorial" >}}

## Step 2: Running the Test
[Content...]

## Conclusion
[Content...]

<!-- End of post: Subscribe CTA -->
{{ partial "youtube-subscribe-cta.html" . }}
```

### For Blog Posts (without video):

```markdown
---
title: "The Ultimate 3D Printing Filament Guide (2025)"
---

## Introduction
[Your content...]

## Main Content
[Content...]

## Conclusion
[Content...]

<!-- End of post: Encourage YouTube subscription -->
{{ partial "youtube-subscribe-cta.html" . }}
```

---

## GA4 Event Tracking

All YouTube integration elements include automatic GA4 tracking:

### Events Tracked:

1. **youtube_subscribe_click**
   - Category: YouTube
   - Label: Source (e.g., "blog-cta", "embed")
   - Value: 1

2. **youtube_video_click**
   - Category: YouTube
   - Label: Video title
   - video_id: YouTube video ID
   - Value: 1

### View in GA4:
- Go to Reports → Engagement → Events
- Look for `youtube_subscribe_click` and `youtube_video_click`

---

## Homepage Integration

The homepage (`content/_index.md`) already includes:
- YouTube subscribe button in the hero section
- YouTube channel link in the features section
- Popular videos section

**No additional changes needed for homepage.**

---

## Best Practices

### 1. Always Link to Written Content
- Every YouTube video should have a corresponding blog post
- Include the blog post URL in video description
- This drives traffic back to your site

### 2. Use CTAs Strategically
- **Top of tutorial**: Use compact badge (`watch-on-youtube.html`)
- **Middle of post**: Embed full video (`youtube-embed` shortcode)
- **End of post**: Use full CTA box (`youtube-subscribe-cta.html`)

### 3. Update Video Descriptions
- Use the template for consistency
- Always include:
  - Link to written guide
  - Link to tools
  - Timestamps
  - Hashtags

### 4. Track Performance
- Monitor GA4 events weekly
- Check which CTAs drive most subscriptions
- Adjust placement based on data

---

## Quick Reference

| Component | File | Use Case | Size |
|-----------|------|----------|------|
| Video Description Template | `content/_templates/youtube-description.txt` | YouTube video descriptions | N/A |
| Subscribe CTA | `layouts/partials/youtube-subscribe-cta.html` | End of blog posts | Large box |
| Video Badge | `layouts/partials/watch-on-youtube.html` | Quick video links | Compact badge |
| Video Embed | `layouts/shortcodes/youtube-embed.html` | Inline video | Responsive iframe |

---

## Testing

After implementing, test:
1. ✅ Build site: `hugo --gc --minify`
2. ✅ Check GA4 events fire (use browser console)
3. ✅ Test subscribe buttons redirect correctly
4. ✅ Verify video embeds load on mobile
5. ✅ Check hover effects on CTA buttons

---

## Future Enhancements

Potential additions:
- YouTube playlist embed shortcode
- Latest videos widget for sidebar
- Video gallery page
- Automated video thumbnail generation
- Shorts integration

---

**Last Updated:** November 13, 2025  
**Maintained by:** Minimal 3DP
