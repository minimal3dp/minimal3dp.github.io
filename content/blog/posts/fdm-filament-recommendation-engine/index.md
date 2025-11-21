---
title: "Stop Guessing: Introducing the FDM Filament Recommendation Engine"
date: 2025-11-21T10:00:00-06:00
draft: true
author: "Mike Wilson"
description: "Discover the FDM Filament Recommendation Engine—a data-driven tool that helps you find the perfect 3D printing material for your project by filtering over 40 filaments by strength, printability, UV resistance, and more."
tags: ["3dprinting", "filament", "tools", "materials", "fdm", "engineering"]
categories: ["tutorials", "tools"]
---

One of the biggest problems I have in my 3D printing journey is simply trying to remember which filament is best for which scenario. If I need a UV-resistant filament for an outdoor part, or if I need to know if a specific engineering-grade material is actually printable on my current setup, digging through PDF Technical Data Sheets (TDS) takes forever.

To solve this, I've developed a new app: the **FDM Filament Recommendation Engine**.

You can watch my full video introduction here:

{{< youtube-embed id="JV84-dXgTk4" title="FDM Filament Recommendation Engine Introduction" >}}

## The Solution: A Data-Driven Filament Finder

**Link to Tool:** [filament.minimal3dp.com](http://filament.minimal3dp.com)

The goal of this application is to let you sort, query, and filter through over 40 different materials to find the one that fits your specific project needs.

I developed this by analyzing various manufacturer TDS records, but I know those aren't always perfectly accurate. To validate the data, I also cross-referenced peer-reviewed journal articles. I utilized AI to help extract and organize this massive amount of data into a usable format.

## Key Features and Updates

For those of you who saw the early version of this tool, I've made several updates based on my own testing and user feedback:

### Simplified Strength Metrics
I originally had three different choices for "strength," but they were all telling me the same thing. I have simplified this to just **General Strength** and **Compressive Strength** to make the data easier to read.

### Printability Scoring
You can filter by "Printability." If you back the slider off to an 8, you'll see familiar materials like PLA and PETG. If you look at engineering materials like PC or ASA, you'll see that score drop significantly—reflecting the real-world difficulty of printing those materials.

### Comparison Tool
This is probably the most useful feature. You can select multiple filaments (for example, UV-resistant materials like ASA, PC, and others) and hit "Compare." This gives you a side-by-side look at their cost score, heat compatibility, and stiffness.

### Processing Data
I've added information on whether a material can be annealed—the process of heating the print after printing to make the material stronger and more dimensionally stable.

## Feedback Welcome

I have added a feedback form to the site. If you have a better source of data than the TDS sheets or journal articles I have used, please feel free to submit it. My goal is to make this a complete repository of knowledge for us to use.

## Sponsor: PCBWay

This project is sponsored by **PCBWay**. I want to thank them for their continued support of the Minimal 3DP channel.

If you are working on a project that requires custom PCBs, I highly recommend checking out their design services. They have powerful tools on their website to get an instant quote, and their help with PCB design layout starts at just **$88.70 US**.

- **Check them out:** [pcbway.com](https://pcbway.com)
- **Discount Code:** [View on Instagram](https://www.instagram.com/p/DQ82COJDPv8/)

## Other Resources

Looking for more 3D printing tools and guides?

- **OrcaSlicer Expert Assistant:** [settings.minimal3dp.com](https://settings.minimal3dp.com)
- **Klipper Calibration & Calculators:** [minimal3dp.com/klipper-calibration](https://minimal3dp.com/klipper-calibration)
- **3D Print Cost Calculator:** [minimal3dp.com/tools/m3dp-fdm-cost-calculator](https://minimal3dp.com/tools/m3dp-fdm-cost-calculator)

---

## Support Minimal 3DP

If you found this tool helpful, you can support my work here:

- **Ko-Fi (One-time donation):** [ko-fi.com/minimal3dp](https://ko-fi.com/minimal3dp)
- **Facebook:** [facebook.com/minimal3dp](https://www.facebook.com/minimal3dp)
- **GitHub:** [github.com/minimal3dp](https://github.com/minimal3dp)

{{< cta type="youtube" location="blog-post" >}}
Subscribe for more 3D printing tools, tutorials, and calibration guides!
{{< /cta >}}
