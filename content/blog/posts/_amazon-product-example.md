---
title: "Amazon Product Shortcode - Usage Example"
date: 2025-11-12
draft: true
description: "Example of using the amazon-product shortcode"
---

# Amazon Product Shortcode Examples

## Example 1: Basic Usage

{{< amazon-product 
  asin="B0D123456" 
  title="FixDry Double NT1 Filament Dryer" 
  price="$159.99"
  image="/images/products/fixdry-nt1.jpg" >}}

Dual-chamber filament dryer with independent temperature control. Perfect for keeping multiple spools dry. Features:
- Holds 2x 1kg spools
- Temperature range: 35-70°C
- Built-in hygrometer
- Quiet operation

{{< /amazon-product >}}

## Example 2: Without Image

{{< amazon-product 
  asin="B0D789012" 
  title="Creality Ender 3 S1 Plus" 
  price="$469.99" >}}

Large-format FDM printer with 300x300x300mm build volume. Direct drive extruder and CR Touch auto-leveling included.

{{< /amazon-product >}}

## Example 3: Simple Product Link

{{< amazon-product 
  asin="B0D345678" 
  title="Premium PLA Filament 1kg" 
  price="$19.99" >}}
{{< /amazon-product >}}

---

**Note:** Replace the ASIN codes above with real Amazon product IDs. The affiliate tag is automatically pulled from `hugo.toml` (`affiliate_tag = "mwf064-20"`).

**GA4 Tracking:** Clicks are automatically tracked with the event name `affiliate_click` including the product title and ASIN.
