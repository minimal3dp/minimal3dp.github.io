# GA4 Event Tracking Guide

**Last Updated:** November 13, 2025  
**File Location:** `/layouts/partials/hooks/head-end.html`

## Overview

This site uses a centralized GA4 event tracking library that automatically tracks user interactions and provides manual tracking functions for custom events.

## Tracking Functions Available

### 1. **Affiliate Link Clicks**
```javascript
trackAffiliateClick(asin, title)
```

**Automatic:** All links with `rel="sponsored"` are automatically tracked.

**Manual Usage:**
```html
<a href="https://www.amazon.com/dp/B0XXXXX?tag=mwf064-20"
   onclick="trackAffiliateClick('B0XXXXX', 'Product Name')">
   Buy Now
</a>
```

**GA4 Event:**
- Event Name: `affiliate_click`
- Category: `Amazon`
- Label: Product title
- Product ID: ASIN

---

### 2. **YouTube Subscribe Clicks**
```javascript
trackYouTubeSubscribe(source)
```

**Usage:**
```html
<a href="https://www.youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw?sub_confirmation=1"
   onclick="trackYouTubeSubscribe('homepage')">
   Subscribe
</a>
```

**Already Implemented In:**
- ✅ `youtube-subscribe-cta.html` partial (blog-cta)
- ✅ Homepage hero section

**GA4 Event:**
- Event Name: `youtube_subscribe_click`
- Category: `YouTube`
- Label: Source location
- Value: 1

---

### 3. **YouTube Video Link Clicks**
```javascript
trackYouTubeVideo(videoId, title)
```

**Usage:**
```html
<a href="https://www.youtube.com/watch?v=ABC123"
   onclick="trackYouTubeVideo('ABC123', 'Tutorial Title')">
   Watch Video
</a>
```

**Already Implemented In:**
- ✅ `watch-on-youtube.html` partial

**GA4 Event:**
- Event Name: `youtube_video_click`
- Category: `YouTube`
- Label: Video title or ID
- Video ID: YouTube video ID
- Value: 1

---

### 4. **Related Post Clicks**
```javascript
trackRelatedPostClick(postTitle, postUrl)
```

**Usage:**
```html
<a href="/blog/post-url/"
   onclick="trackRelatedPostClick('Post Title', '/blog/post-url/')">
   Read More
</a>
```

**Already Implemented In:**
- ✅ `related-posts.html` partial

**GA4 Event:**
- Event Name: `related_post_click`
- Category: `Related Posts`
- Label: Post title
- Page Path: Destination URL
- Value: 1

---

### 5. **Calculator Usage** 🆕
```javascript
trackCalculatorUse(calculatorName, action)
```

**Usage in Calculator Pages:**
```html
<button onclick="calculateCost(); trackCalculatorUse('fdm-cost', 'calculate')">
  Calculate
</button>

<button onclick="resetForm(); trackCalculatorUse('fdm-cost', 'reset')">
  Reset
</button>

<button onclick="exportResults(); trackCalculatorUse('fdm-cost', 'export')">
  Export
</button>
```

**Calculator Names:**
- `fdm-cost` - FDM Cost Calculator
- `shrinkage` - Shrinkage Calculator
- `resin-cost` - Resin Print Cost (future)
- `filament-drying` - Filament Drying Time (future)

**GA4 Event:**
- Event Name: `calculator_use`
- Category: `Tools`
- Label: Calculator name
- Calculator Action: calculate/reset/export
- Value: 1

---

### 6. **Email Signups** 🆕
```javascript
trackEmailSignup(formLocation, listType)
```

**Usage:**
```html
<form onsubmit="trackEmailSignup('sidebar', 'newsletter'); return true;">
  <input type="email" name="email" required>
  <button type="submit">Subscribe</button>
</form>
```

**Form Locations:**
- `sidebar` - Sidebar widget
- `footer` - Footer CTA
- `blog-inline` - Inside blog posts
- `homepage` - Homepage hero
- `popup` - Modal popup

**List Types:**
- `newsletter` - Weekly newsletter
- `course` - Email course
- `ebook` - Free ebook download
- `updates` - Product updates

**GA4 Event:**
- Event Name: `email_signup`
- Category: `Lead Generation`
- Label: Form location
- List Type: Type of list
- Value: 5

---

### 7. **Video Plays** 🆕
```javascript
trackVideoPlay(videoId, videoTitle)
```

**Usage with YouTube IFrame API:**
```javascript
// When video starts playing
player.addEventListener('onStateChange', function(event) {
  if (event.data == YT.PlayerState.PLAYING) {
    trackVideoPlay('ABC123', 'Tutorial: Setting Up Klipper');
  }
});
```

**GA4 Event:**
- Event Name: `video_play`
- Category: `Video Engagement`
- Label: Video title or ID
- Video ID: YouTube video ID
- Value: 2

---

### 8. **CTA Button Clicks** 🆕
```javascript
trackCtaClick(ctaType, location)
```

**Usage:**
```html
{{< cta type="youtube" >}}
<a href="https://youtube.com/..." 
   onclick="trackCtaClick('youtube', 'blog-post')">
   Subscribe on YouTube
</a>
{{< /cta >}}
```

**CTA Types:**
- `youtube` - YouTube subscribe
- `calculator` - Calculator CTA
- `email` - Email signup
- `support` - Support/donate
- `product` - Product recommendation

**Locations:**
- `blog-post` - Within blog content
- `sidebar` - Sidebar widget
- `homepage` - Homepage
- `tutorial` - Tutorial page
- `footer` - Footer

**GA4 Event:**
- Event Name: `cta_click`
- Category: `CTA`
- Label: CTA type
- CTA Location: Where clicked
- Value: 1

---

### 9. **Site Search** 🆕
```javascript
trackSiteSearch(searchQuery, resultsCount)
```

**Usage:**
```javascript
// When search is executed
function performSearch(query) {
  const results = getSearchResults(query);
  trackSiteSearch(query, results.length);
  displayResults(results);
}
```

**GA4 Event:**
- Event Name: `search`
- Search Term: User's query
- Results Count: Number of results

---

### 10. **Outbound Links** 🆕
```javascript
trackOutboundLink(url, linkText)
```

**Automatic:** All links with `target="_blank"` or external domains are automatically tracked (except sponsored links).

**Manual Usage:**
```html
<a href="https://external-site.com"
   onclick="trackOutboundLink('https://external-site.com', 'External Resource')">
   Visit Site
</a>
```

**GA4 Event:**
- Event Name: `click`
- Category: `Outbound Link`
- Label: Destination URL
- Link Text: Text of the link

---

### 11. **File Downloads** 🆕
```javascript
trackFileDownload(fileName, fileType)
```

**Automatic:** Downloads of PDFs, STL files, GCODE, configs, etc. are automatically tracked.

**Manual Usage:**
```html
<a href="/files/klipper-config.cfg"
   onclick="trackFileDownload('klipper-config.cfg', 'cfg')">
   Download Config
</a>
```

**Tracked File Types:**
- `.pdf` - PDF documents
- `.stl` - 3D model files
- `.gcode` - G-code files
- `.zip` - Compressed archives
- `.cfg` - Configuration files
- `.json` - JSON data
- `.txt` - Text files
- `.csv` - CSV exports

**GA4 Event:**
- Event Name: `file_download`
- Category: `Download`
- Label: File name
- File Extension: File type
- Value: 1

---

## Automatic Tracking Features

### Already Tracking Automatically:
1. ✅ **Affiliate Links** - All `rel="sponsored"` links
2. ✅ **Outbound Links** - All external links
3. ✅ **File Downloads** - PDFs, STL, GCODE, configs, etc.

### Manual Implementation Required:
1. ⏳ **Calculator Usage** - Add to calculator JS files
2. ⏳ **Email Signups** - Add to email forms (when implemented)
3. ⏳ **Video Plays** - Add to YouTube embed shortcode (optional)

---

## Implementation Examples

### Example 1: Add Tracking to FDM Calculator

**File:** `/tools/m3dp-fdm-cost-calculator/index.html`

```javascript
// In the calculate function
function calculate() {
  // ... calculation logic ...
  
  // Track calculator usage
  trackCalculatorUse('fdm-cost', 'calculate');
  
  // Display results
  showResults();
}

// In the reset function
function resetCalculator() {
  // ... reset logic ...
  trackCalculatorUse('fdm-cost', 'reset');
}

// In the export function
function exportToPDF() {
  // ... export logic ...
  trackCalculatorUse('fdm-cost', 'export');
}
```

---

### Example 2: Add Tracking to Email Form (ConvertKit)

**When Form is Implemented:**

```html
<form id="newsletter-form" onsubmit="handleSubmit(event)">
  <input type="email" name="email" required>
  <button type="submit">Subscribe</button>
</form>

<script>
function handleSubmit(event) {
  // Track the signup
  trackEmailSignup('sidebar', 'newsletter');
  
  // Let form submit normally
  return true;
}
</script>
```

---

### Example 3: Add Video Play Tracking to YouTube Embed

**File:** `/layouts/shortcodes/youtube-embed.html`

```html
<script>
// YouTube IFrame API
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// Create player
function onYouTubeIframeAPIReady() {
  var player = new YT.Player('youtube-{{ .Get "id" }}', {
    events: {
      'onStateChange': onPlayerStateChange
    }
  });
}

// Track when video plays
function onPlayerStateChange(event) {
  if (event.data == YT.PlayerState.PLAYING) {
    trackVideoPlay('{{ .Get "id" }}', '{{ .Get "title" }}');
  }
}
</script>
```

---

## Testing in Browser Console

### Check if Tracking is Loaded:
```javascript
// Should see success message in console
✅ GA4 Event Tracking Library Loaded
```

### Test Individual Functions:
```javascript
// Test affiliate click
trackAffiliateClick('B0XXXXX', 'Test Product');

// Test YouTube subscribe
trackYouTubeSubscribe('console-test');

// Test calculator use
trackCalculatorUse('fdm-cost', 'calculate');

// Test email signup
trackEmailSignup('sidebar', 'newsletter');
```

### View Events in GA4:
1. Go to Google Analytics 4
2. Navigate to Reports → Realtime
3. Perform action on site
4. Event should appear within 5-10 seconds

---

## GA4 Event Summary

| Event Name | Category | Already Tracking | Manual Setup Needed |
|------------|----------|------------------|---------------------|
| `affiliate_click` | Amazon | ✅ Auto | No |
| `youtube_subscribe_click` | YouTube | ✅ Partials | No |
| `youtube_video_click` | YouTube | ✅ Partials | No |
| `related_post_click` | Related Posts | ✅ Partials | No |
| `calculator_use` | Tools | ❌ | **Yes - Add to calculators** |
| `email_signup` | Lead Generation | ❌ | **Yes - When form added** |
| `video_play` | Video Engagement | ❌ | Optional (nice-to-have) |
| `cta_click` | CTA | ❌ | Optional |
| `search` | Search | ❌ | When search added |
| `click` (outbound) | Outbound Link | ✅ Auto | No |
| `file_download` | Download | ✅ Auto | No |

---

## Priority Implementation

### Immediate (This Week):
1. ✅ Deploy centralized tracking library
2. ⏳ Add tracking to FDM Cost Calculator
3. ⏳ Add tracking to Shrinkage Calculator

### Short-term (This Month):
1. Add email signup form with tracking
2. Add CTA tracking to shortcodes
3. Test all events in GA4

### Long-term (Future):
1. Add video play tracking (YouTube IFrame API)
2. Add search tracking (when search is implemented)
3. Create custom GA4 dashboard with all events

---

## Debugging

### Events Not Showing in GA4?

1. **Check Console:**
   ```javascript
   // Should see log messages like:
   GA4 Event: affiliate_click { asin: 'B0XXXXX', title: 'Product' }
   ```

2. **Check gtag is Loaded:**
   ```javascript
   typeof gtag === 'function'  // Should return true
   ```

3. **Check GA4 Measurement ID:**
   - File: `hugo.toml`
   - Look for: `googleAnalytics = "G-VQ8RPWC2MK"`

4. **Test in Incognito Mode:**
   - Ad blockers can prevent GA4 tracking
   - Use incognito to test without extensions

5. **Check Realtime Reports:**
   - GA4 → Reports → Realtime
   - Events appear within 5-10 seconds

---

## File Locations

**Main Library:**
- `/layouts/partials/hooks/head-end.html` (centralized tracking)

**Partials Using Tracking:**
- `/layouts/partials/related-posts.html` (trackRelatedPostClick)
- `/layouts/partials/youtube-subscribe-cta.html` (trackYouTubeSubscribe)
- `/layouts/partials/watch-on-youtube.html` (trackYouTubeVideo)

**Shortcodes Using Tracking:**
- `/layouts/shortcodes/amazon-product.html` (trackAffiliateClick)
- `/layouts/shortcodes/cta.html` (trackCtaClick - optional)
- `/layouts/shortcodes/youtube-embed.html` (trackVideoPlay - optional)

---

## Next Steps

1. **Deploy Changes:**
   ```bash
   git add layouts/partials/hooks/head-end.html
   git commit -m "Add centralized GA4 event tracking library"
   git push
   ```

2. **Add Calculator Tracking:**
   - Update FDM Cost Calculator JS
   - Update Shrinkage Calculator JS
   - Test in browser console

3. **Monitor in GA4:**
   - Wait 24-48 hours for data
   - Create custom reports
   - Set up conversion tracking

4. **Document Results:**
   - Track which CTAs get most clicks
   - Measure calculator usage rates
   - Optimize based on data

---

**Questions?** Check the console logs or test functions in browser DevTools.

**Last Updated:** November 13, 2025
