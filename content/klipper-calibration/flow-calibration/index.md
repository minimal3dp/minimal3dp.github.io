---
date: 2024-04-03
title: Flow Calibration
linkTitle: Flow Calibration
description: >
  Calibrate the Flow of your Extruder in your Slicer
author: Mike Wilson (minimal3dp@gmail.com)
draft: false
weight: 20
---

# Flow Calibration

## From 3D Print Beginner

> The flow rate calibration is done in order to fine tune the amount of plastic extruded by the printer. Also known as Extrusion Multiplier, by calibrating the flow rate you can fix issues caused by under-extrusion or over-extrusion. Besides this, flow rate calibration can also improve retraction values a bit and help with bulging corners and layer seam.
> If the extruder steps are properly calibrated, the flow rate value should be really close to a single digit value (1.00).

[Flow Rate Calibration – Improve Print Accuracy](https://3dprintbeginner.com/flow-rate-calibration/)

## Slicer Settings

| Slicer Settings  |     |
| ---------------- | --- |
| Layer Height     | 0.2 |
| Paerimeters      | 2   |
| Line Width       | 0.5 |
| Print Thin Walls | Off |
| Top Layer        | 0   |
| Bottom Layer     | 1   |
| Infill           | 0%  |

Cube STL File: [Flow Cube](https://drive.google.com/file/d/11vJEoea94jWu8c0bYwK1tcJ92S1TD9wj/view)

1. Print Cube with Settings Above
2. Measure the top of all 4 sides and place values below
3. Update Flow in Slicer with "FLOW" Value

## Flow Calibration Calculator

{{< flow-calibration >}}

## Update Your Slicer

{{< youtube qmEKuqc5gAU >}}
