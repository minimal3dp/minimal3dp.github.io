---
date: 2025-04-18
title: Extrusion Rate Smoothing in OrcaSlicer
linkTitle: extrusion-rate-smoothing-in-orcaslicer
description: >
  
author: Mike Wilson (minimal3dp@gmail.com)
resources:
  - src: "**.{png,jpg}"
    title: "Image #:counter"
    params:
      byline: "Photo: Minimal 3DP"
draft: true
---

## Extrusion Rate Smoothing in OrcaSlicer: A Comprehensive Guide

### Understanding and Optimizing Your 3D Prints

3D printing involves a lot of intricate settings to achieve the best possible results. One of the advanced features in [Orcaslicer](https://github.com/SoftFever/OrcaSlicer) that can significantly impact print quality is extrusion rate smoothing. This post will explore what it is, why it's important, and how to use it effectively.

### What is Extrusion Rate Smoothing?

Extrusion rate smoothing, similar to [Prusaslicer's](https://www.prusa3d.com/page/prusaslicer_424/) [pressure equalizer](https://help.prusa3d.com/article/pressure-equalizer_331504), is a feature that limits the rate of extrusion volume change below a certain threshold.  In simpler terms, it helps Orcaslicer manage how much plastic needs to be pushed out by the extruder.  Think of it as gently applying the brakes in a car rather than jamming them on.  It smooths out the start and stop of extrusion, especially during speed changes at corners and bridges.

### Why Use Extrusion Rate Smoothing?

- Consistent Extrusion: It leads to more consistent extrusion, particularly at high speeds.
- Reduced Inconsistencies: It helps eliminate inconsistencies during speed changes, such as at corners
- Aids Pressure Advance: It works in conjunction with pressure advance for better results.
- Smoother Finishes: Contributes to smoother surface finishes.

### The Mechanics Behind It

During printing, the printer constantly speeds up and slows down, especially at corners and overhangs.  These speed changes necessitate changes in the amount of plastic being pushed out.  Sudden changes can be difficult for the extruder and firmware to handle, leading to artifacts like bumps and bulges.  Extrusion rate smoothing creates speed ramps, gently slowing down before a change and gradually speeding up afterward.  This makes it easier for the extruder to keep up, reducing unwanted artifacts.

### Extrusion Rate Smoothing, Pressure Advance, and the Motion Planner

The printer's firmware has a motion planner that interprets speed change commands and translates them into motor movements.  Pressure advance calculates the necessary slowdown to reach the target speed.  Extrusion rate smoothing regulates the pressure changes, creating a smooth ramp-up and ramp-down of pressure.  Without it, sudden speed changes can cause blobs and artifacts.

### Using Extrusion Rate Smoothing in OrcaSlicer

In OrcaSlicer, the extrusion rate smoothing settings can be found in the speed section of the process parameters.  These settings include segment length and an option to apply it only to external features.

To determine the appropriate values, you can refer to the [OrcaSlicer wiki](https://github.com/SoftFever/OrcaSlicer/wiki/extrusion-rate-smoothing) or use my [Klipper Calibration spreadsheet(https://docs.google.com/spreadsheets/d/1LlSHsa86RuT_btswmDsmQp0LrTJ9U0HJcRhorsqz1ug/edit?usp=sharing)].  The spreadsheet helps calculate the maximum ERS value based on parameters like outer wall acceleration, line width, and layer height.  It's recommended to start with an experimental value between 60% and 80% of the maximum calculated ERS.

### Important Considerations

- A lower ERS value means more aggressive smoothing, and a higher value means less smoothing.
- If the ERS value exceeds the maximum, it won't be applied.
- Extrusion rate smoothing is most useful for high accelerations and large flow rates, such as on a Voron with a high flow hotend and when pressure advance is set.
- For Bowden printers, especially with flexible filaments, a lower ERS value is generally better.  Direct drive printers can typically use higher values.
- This value may need to be adjusted when changing acceleration or if you notice inconsistencies.
- It's a user-determined value, so experimentation is key.
- Potential downsides include increased print time (though this is rare) and a possible loss of fine detail in some cases.
- Crucially, extrusion rate smoothing won't solve problems caused by an improperly calibrated printer.

### Key Takeaways

- The ERS value sets the maximum rate of change for extruded plastic, not the extrusion speed itself.
- Start with recommended values (60-80% of the maximum) and increment by 10%.
- Use low rates for Bowden setups with flexible filaments and higher rates for direct drive.
- Pay close attention to overhangs to assess the effect of the setting.
- Don't exceed the maximum ERS value.
- If using Klipper, calibrate pressure advance before adjusting extrusion rate smoothing.

Extrusion rate smoothing is a powerful tool in OrcaSlicer for optimizing print quality. By understanding its mechanics and how to adjust the settings, you can achieve smoother, more consistent 3D prints.
