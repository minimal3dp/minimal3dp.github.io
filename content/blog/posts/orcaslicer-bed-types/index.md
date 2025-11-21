---
date: 2025-11-19
title: "Mastering Bed Types in OrcaSlicer: Automate Z-Offsets and Temperatures"
linkTitle: Mastering Bed Types in OrcaSlicer
description: >
  Learn how to automate Z-offset and temperature adjustments when swapping build plates using OrcaSlicer's bed type feature. Perfect for users running multiple PEI sheets or specialized plates.
author: Mike Wilson (minimal3dp@gmail.com)
resources:
  - src: "**.{png,jpg}"
    title: "Image #:counter"
    params:
      byline: "Photo: Minimal 3DP"
draft: false
categories: [3D Printers, videos]
tags: [How-To, slicers, OrcaSlicer]
featured_image: "https://i.ytimg.com/vi/v_cHEOeFav8/hqdefault.jpg"
featured_image_alt: "Mastering Bed Types in OrcaSlicer video thumbnail"
images:
  - "https://i.ytimg.com/vi/v_cHEOeFav8/hqdefault.jpg"
---

I found a feature that is incredibly powerful for anyone running multiple build plates on a single printer: **specifying bed types**.

If you swap between a smooth PEI sheet, a textured plate, or a cool plate, you usually have to manually adjust your Z-offset or run a bed level every time. However, OrcaSlicer allows you to automate this process, saving your Z-offset and temperature settings based on the specific bed you select. For broader slicer tuning, visit the [OrcaSlicer Tutorials Hub](/projects/tutorials/orca-slicer/).

{{< youtube-embed id="v_cHEOeFav8" title="Mastering Bed Types in OrcaSlicer" >}}

## Enabling Multiple Bed Types

OrcaSlicer generally supports four standard bed definitions: Cool Plate, Engineering Plate, High Temp Plate, and Textured PEI Plate. Even if your specific brand of plate isn't listed, you can use these presets as placeholders to trigger specific settings.

To enable this feature:

1. Open OrcaSlicer and go to **Printer Settings**.
2. Check the box for **"Support multiple bed types"**.
3. Once enabled, you will see a dropdown menu allowing you to select your active bed type directly in the main interface.

## Automating Bed Temperatures

One immediate benefit of this feature is temperature management. Different bed materials require different surface temperatures.

For example, I typically use a smooth PEI high-temp plate at 60°C. However, I recently started using the **BigTreeTech MENT BQ Cryo Grip ProGlacial beds**. These are double-sided (smooth and textured), but they run best about 5 to 10 degrees cooler than standard PEI.

By utilizing the bed type settings in the **Filament** tab, I can assign specific temperatures to specific plate types (e.g., setting the "Cool Plate" slot to 55°C). This allows me to "set it and forget it"—the slicer handles the temp change automatically based on the bed I select.

## Automating Z-Offsets with Start G-Code

The most powerful application of this feature is automating your Z-offset. To make this work, you need to pass the bed type variable from OrcaSlicer to your printer's start code. After implementing this, refine extrusion consistency using [Flow Calibration](/klipper-calibration/flow-calibration/) and ringing reduction with [Input Shaping](/klipper-calibration/input-shaping/).

### 1. Update Slicer Start G-Code

In your OrcaSlicer machine start G-code, you need to add a specific variable so the printer knows which bed is selected. The code looks like this:

```gcode
{if curr_bed_type=="Textured PEI Plate"}
  SET_GCODE_OFFSET Z=-0.05
{else}
  SET_GCODE_OFFSET Z=0.0
{endif}
```

Available bed types are:
```bash
"Cool Plate"
"Engineering Plate"
"High Temp Plate"
"Textured PEI Plate"
```

This line sends the current bed selection to your printer's configuration. For more macro examples see the [Klipper Calibration Hub](/klipper-calibration/).

### 2. Configure Printer Logic (Macros)

Once the printer receives the variable, you can use conditional logic (If/Else statements) in your printer's configuration (like Klipper macros) to adjust the Z-offset.

Based on examples found on the Creality K2 Plus forums and AI-generated code, the logic works as follows:

* **Capture the Variable:** The macro grabs the uppercase variable `CURR_BED_TYPE`.
* **If/Else Statements:** The printer checks which bed is active and applies a specific offset.
    * *Example:* If using a glass plate, set Z-offset to 0.
    * *Example:* If using Textured PEI, set Z-offset to -0.03.
* **Fallback:** You can include an `else` statement to handle any unknown bed types.

## Conclusion

This feature adds a layer of convenience and optimization to your workflow. Whether you are looking to automate temperature changes for Cryo Grip plates or swap between smooth and textured sheets without releveling, specifying bed types in OrcaSlicer is a game changer.

Thanks for stopping by! I'm still recovering, so I appreciate your patience if this wasn't up to my usual standards, but I look forward to talking to you again soon.

**Have questions about your start G-code? Leave a comment on the video!**

## Related Guides
- [OrcaSlicer Expert Assistant Launch](/blog/posts/orcaslicer-expert-assistant-launch/)
- [OrcaSlicer Tutorials Hub](/projects/tutorials/orca-slicer/)
- [Klipper Calibration Hub](/klipper-calibration/)
- [Flow Calibration](/klipper-calibration/flow-calibration/)
- [Input Shaping](/klipper-calibration/input-shaping/)
