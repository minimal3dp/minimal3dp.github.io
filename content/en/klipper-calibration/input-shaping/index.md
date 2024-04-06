---
date: 2024-03-31
title: Input Shaping
linkTitle: Input Shaping
description: >
  Setup and Calculate Input Shaping Values
author: Mike Wilson (minimal3dp@gmail.com)
draft: false
weight: 50
---

# Input Shaping

## From the Klipper Documents

> "Klipper Input Shaping improves print quality by exorcising the ghosts caused by vibrations and resonances. Read on to learn all about it!"

[Klipper: Input Shaping – Simply Explained](https://all3dp.com/2/klipper-input-shaping-simply-explained/)

Basic tuning requires measuring the ringing frequencies of the printer by printing a test model.

According to the [Klipper docs](https://www.klipper3d.org/Resonance_Compensation.html), slice the ringing test model, which can be found in [docs/prints/ringing_tower.stl](https://www.klipper3d.org/prints/ringing_tower.stl), in the slicer:

- Use a layer height is 0.2 or 0.25 mm.
- Both the infill and top layers can be set to 0.
- Use eithet 1-2 perimeters, or vase mode with 1-2 mm base.
- Use a high speed that is around 80-100 mm/sec, for external perimeters.
- aThe minimum layer time is at most 3 seconds.
- Turn off any "dynamic acceleration control" controls in the slicer.
- Do not turn the model. It has X and Y marks at the back of the model. Note the unusual location of the marks vs. the axes of the printer - it is not a mistake. The marks can be used later in the tuning process as a reference, because they show which axis the measurements correspond to.

## Console Commands

## Input Shaping Calculator

{{< input-shaping >}}

## Edit Printer.cfg

```

```
