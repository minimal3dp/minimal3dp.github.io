---
title: "Shortcode Examples & Usage Guide"
date: 2025-11-13
draft: true
description: "Examples and usage guide for all custom shortcodes available on Minimal 3DP"
---

# Shortcode Usage Guide

This page demonstrates all available custom shortcodes for content creation.

## 1. YouTube Embed

Embed YouTube videos with automatic subscribe button:

```
{{</* youtube-embed id="dQw4w9WgXcQ" title="Example Video Tutorial" */>}}
```

{{< youtube-embed id="dQw4w9WgXcQ" title="Example Video Tutorial" >}}

---

## 2. Alert Boxes

### Info Alert
```
{{</* alert type="info" */>}}
This is important information you should know!
{{</* /alert */>}}
```

{{< alert type="info" >}}
This is important information you should know!
{{< /alert >}}

### Warning Alert
```
{{</* alert type="warning" */>}}
⚠️ Be careful with this setting - it can damage your printer!
{{</* /alert */>}}
```

{{< alert type="warning" >}}
Be careful with this setting - it can damage your printer!
{{< /alert >}}

### Success Alert
```
{{</* alert type="success" */>}}
Great! Your calibration is complete and ready to use.
{{</* /alert */>}}
```

{{< alert type="success" >}}
Great! Your calibration is complete and ready to use.
{{< /alert >}}

### Danger Alert
```
{{</* alert type="danger" */>}}
STOP! This will erase all your settings. Back up first!
{{</* /alert */>}}
```

{{< alert type="danger" >}}
STOP! This will erase all your settings. Back up first!
{{< /alert >}}

### Tip Alert
```
{{</* alert type="tip" */>}}
💡 Pro tip: Always clean your build plate with IPA before printing!
{{</* /alert */>}}
```

{{< alert type="tip" >}}
💡 Pro tip: Always clean your build plate with IPA before printing!
{{< /alert >}}

---

## 3. Call-to-Action (CTA) Boxes

### YouTube CTA (Default)
```
{{</* cta type="youtube" */>}}
Watch the full tutorial to see this in action!
{{</* /cta */>}}
```

{{< cta type="youtube" >}}
Watch the full tutorial to see this in action!
{{< /cta >}}

### Calculator CTA
```
{{</* cta type="calculator" */>}}
Calculate exactly how much this print will cost!
{{</* /cta */>}}
```

{{< cta type="calculator" >}}
Calculate exactly how much this print will cost!
{{< /cta >}}

### Email Newsletter CTA
```
{{</* cta type="email" */>}}
Get weekly 3D printing tips delivered to your inbox!
{{</* /cta */>}}
```

{{< cta type="email" >}}
Get weekly 3D printing tips delivered to your inbox!
{{< /cta >}}

### Support CTA
```
{{</* cta type="support" */>}}
Found this helpful? Support us by subscribing!
{{</* /cta */>}}
```

{{< cta type="support" >}}
Found this helpful? Support us by subscribing!
{{< /cta >}}

---

## 4. Product Comparison Tables

```
{{</* product-compare */>}}
| Feature | Bambu Lab P1S | Prusa MK4 | Creality K1 |
|---------|---------------|-----------|-------------|
| Price | $699 | $799 | $599 |
| Print Speed | 500mm/s | 200mm/s | 600mm/s |
| Build Volume | 256×256×256mm | 250×210×220mm | 220×220×250mm |
| Auto Leveling | ✅ | ✅ | ✅ |
| Enclosed | ✅ | ❌ | ✅ |
| Multi-Color | Optional AMS | MMU3 | ❌ |
| Rating | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐½ | ⭐⭐⭐⭐ |
| Best For | Speed & Ease | Reliability | Budget Speed |
{{</* /product-compare */>}}
```

{{< product-compare >}}
| Feature | Bambu Lab P1S | Prusa MK4 | Creality K1 |
|---------|---------------|-----------|-------------|
| Price | $699 | $799 | $599 |
| Print Speed | 500mm/s | 200mm/s | 600mm/s |
| Build Volume | 256×256×256mm | 250×210×220mm | 220×220×250mm |
| Auto Leveling | ✅ | ✅ | ✅ |
| Enclosed | ✅ | ❌ | ✅ |
| Multi-Color | Optional AMS | MMU3 | ❌ |
| Rating | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐½ | ⭐⭐⭐⭐ |
| Best For | Speed & Ease | Reliability | Budget Speed |
{{< /product-compare >}}

---

## Usage Tips

### When to Use Each Shortcode

**youtube-embed**: 
- Tutorial posts with video companions
- Video reviews
- Step-by-step guides with visual demonstrations

**alert**:
- `info`: General information or context
- `warning`: Cautions about common mistakes
- `success`: Confirmation messages or positive outcomes
- `danger`: Critical warnings about damage/safety
- `tip`: Pro tips and best practices

**cta**:
- `youtube`: At the end of tutorials
- `calculator`: When discussing costs or measurements
- `email`: Top-performing posts, end of tutorials
- `support`: Tutorial/guide conclusions

**product-compare**:
- Product reviews
- "Best of" roundups
- Buying guides
- Feature comparisons

### Best Practices

1. **Don't overuse**: 1-2 CTAs per post maximum
2. **Strategic placement**: Place CTAs after providing value
3. **Alert hierarchy**: Use danger sparingly for maximum impact
4. **Comparison tables**: Keep to 3-5 products for readability
5. **Custom text**: Always customize CTA text for context

---

## GA4 Tracking

All interactive shortcodes include GA4 tracking:

- **youtube-embed**: Tracks subscribe clicks (`subscribe_click`)
- **cta**: Tracks all CTA interactions (`cta_click`)
- **product-compare**: Links within tables tracked by amazon-product shortcode

View events in Google Analytics 4 under Events → All Events.
