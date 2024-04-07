---
date: 2024-04-06
title: Lead Screw Rotation Distance
linkTitle: Lead Screw Rotation Distance
description: >
  Calculate Lead Screw Rotation Distance
author: Mike Wilson (minimal3dp@gmail.com)
draft: false
weight: 80
---

# Setting Lead Screw Rotation Distance

## From the Klipper Documents

The rotational axes with a lead screw can be easily calculated with the following formula:

```
rotation_distance = <screw_pitch> * <number_of_separate_threads>
```

## Steps

|           | Pitch | # of Threads |      |
| --------- | ----- | ------------ | ---- |
| Variables | 2     | 4            | T8x8 |
|           | 2     | 2            | T8x4 |
|           | 2     | 1            | T8x2 |



## Lead Screw Rotation Distance Calculator

{{< lead-screw-rotation-distance >}}

