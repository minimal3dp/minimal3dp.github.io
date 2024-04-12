---
date: 2024-04-07
title: Pressure Advance
linkTitle: Pressure Advance
description: >
  Calculate the ideal Pressure Advance
author: Mike Wilson (minimal3dp@gmail.com)
draft: false
weight: 40
---

# Pressure Advance

## From the Klipper Documents

> Pressure advance does two useful things - it reduces ooze during non-extrude moves and it reduces blobbing during cornering. This guide uses the second feature (reducing blobbing during cornering) as a mechanism for tuning.

[Klipper Documents](https://www.klipper3d.org/Pressure_Advance.html)

## Slicer Settings

| Paramenter      | Value |
| --------------- | ----- |
| Nozzle Diameter | 0.4   |
| Layer Height    | 0.3   |
| Infill          | 0     |

Test Model: [Square Tower](https://www.klipper3d.org/prints/square_tower.stl)

## Console Commands

1. Setup

```
SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500
```

2. Select command based on drive:

Direct Drive:

```
TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.005
```

Bowden Tube:

```
TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.020
```

## Pressure Advance Calculator

{{< pressure-advance >}}

## Edit Your Slicer or Printer.cfg

** Video Coming Soon **
