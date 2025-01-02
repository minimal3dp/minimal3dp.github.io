---
date: 2025-01-01
title: 3D Printing and Max Volumetric Speed
linkTitle: M3DP Max Flow Rate
description: > 
  
author: Mike Wilson (minimal3dp@gmail.com)
resources:
  - src: "**.{png,jpg}"
    title: "Image #:counter"
    params:
      byline: "Photo: Minimal 3DP"
draft: false
categories: [3D Printers, videos]
tags: [How-To, slicers]
---

## Finding Your 3D Printer's Sweet Spot - A Guide to Maximizing Print Speed

Have you ever wondered how fast your 3D printer can truly go? When I get a new printer or see a new model released, the first question that pops into my head is always, "How fast can I print with this thing?"

This post will explore how to determine the optimal print speed for your 3D printer, ensuring both speed and quality.

## Factors Influencing Print Speed

### Print Parameters

- **Infill**: While not a major time-saver, adjusting infill patterns and density can slightly reduce print time.
- **Wall Thickness**: Reducing the number of walls can significantly decrease print time, but it can also compromise the model's strength.
- **Layer Height**: Increasing layer height generally speeds up printing, but it can also affect print quality and part strength.
- **Other Parameters**: Factors like print speed, infill density, and layer height also impact the mechanical properties of the printed part, according to research. Finding the balance between speed and strength is crucial.

### Extruder Limitations

- **Max Flow Rate**: Each extruder has a maximum flow rate, which determines how much filament it can push out per second. Exceeding this limit leads to inconsistent extrusion, poor print quality, and weaker parts.

### Determining Max Flow Rate

[Ellis's Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/articles/determining_max_volumetric_flow_rate.html) provides valuable information and equations to calculate your extruder's max flow rate. A simple test involves extruding a known length of filament at increasing speeds until you observe a noticeable drop in extrusion quality.

One of the key points that Ellis' guide points out is that using approximate values (Table 1) is possible.

| Hotend                               | Flow Rate (mm3/s) |
|--------------------------------------|-------------------|
| E3D V6                               | 11                 |
| E3D V6 Volcano                        | 20                 |
| E3D Revo                               | 11                 |
| Dragon SF                               | 15                 |
| Sailfish                        | 20                 |
| Dragon HF                               | 24                 |
| Dragonfly BMO                               | 13              |
| Rapido HF                               | 24                 |
| Rapido UHF                              | 30                 |
| Mosquito                               | 20                 |
| Mosquito Magnum                        | 30                 |
| Bambu X1                       | 35                 |

### Finding the Sweet Spot

Determine Max Flow Rate: Conduct tests as described above to find your extruder's maximum volumetric flow rate.
Set Volumetric Speed: Adjust the volumetric speed setting in your slicer software to match your calculated max flow rate.
Optimize Print Profiles: Experiment with different print speed settings for various parts of the model, ensuring that the speeds for visible features do not exceed the calculated safe limit.
Test and Iterate: Print test parts and adjust parameters based on the results. Observe print quality, part strength, and overall print time.

### Important Considerations

- Model Size: Smaller models may not allow the printer to reach maximum speed due to acceleration and deceleration times.

- Part Complexity: Complex models with intricate details may require slower print speeds to ensure accurate and high-quality results.

By carefully considering these factors and conducting thorough testing, you can optimize your 3D printer's print speed while maintaining excellent print quality and part strength.

**Disclaimer**: This information is for general guidance only. Always refer to your printer's manual and manufacturer's recommendations for specific instructions and safety guidelines.

I hope this guide helps you unlock your 3D printer's full potential!
