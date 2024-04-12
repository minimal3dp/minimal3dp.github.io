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

## Steps

| Parameter    | Value | Notes             |
| ------------ | ----- | ----------------- |
| Layer Height | 0.2   | or .25            |
| Paerimeters  | 1     | 0r 2 0r Vase Mode |
| Line Width   | 0.5   |                   |
| Print Speed  | 100   | 0r 80             |
| Top Layer    | 0     |                   |
| Bottom Layer | 5     |                   |
| Infill       | 0%    |                   |

1. If square_corner_velocity parameter was changed, revert it back to 5.0.
2. Klipper Console Command:

```
SET_VELOCITY_LIMIT ACCEL_TO_DECEL=7000
```

3. Klipper Console Command:

```
SET_PRESSURE_ADVANCE ADVANCE=0
```

4. Klipper Console Command:

```
SET_INPUT_SHAPER SHAPER_FREQ_X=0 SHAPER_FREQ_Y=0
```

5. Klipper Console Command:

```
TUNING_TOWER COMMAND=SET_VELOCITY_LIMIT PARAMETER=ACCEL START=1500 STEP_DELTA=500 STEP_HEIGHT=5
```

6. Print with Settings Above
7. Count the "rings" on X and Y sides of ringing tower
8. Measure the distance between Rings

## Input Shaping Calculator

{{< input-shaping >}}

## Edit Printer.cfg

**Add Below to Printer.cfg with above X and Y Frequencies**

```
[input_shaper]
shaper_freq_x: <X Frequency>  # frequency for the X mark of the test model
shaper_freq_y: <Y Frequency>  # frequency for the Y mark of the test model
```

Then Run the following Steps in the Klipper Console:

1. Klipper Console Command:

```
RESTART
```

2. Klipper Console Command:

```
SET_VELOCITY_LIMIT ACCEL_TO_DECEL=7000
```

3. Klipper Console Command:

```
SET_PRESSURE_ADVANCE ADVANCE=0
```

4. Klipper Console Command:

```
SET_INPUT_SHAPER SHAPER_TYPE=MZV
```

5. Klipper Console Command:

```
TUNING_TOWER COMMAND=SET_VELOCITY_LIMIT PARAMETER=ACCEL START=1500 STEP_DELTA=500 STEP_HEIGHT=5
```

6. Print the Model as above

If you see no rings add the following to the [input_shaper] section

```
[input_shaper]
shaper_freq_x: <X Frequency>  # frequency for the X mark of the test model
shaper_freq_y: <Y Frequency>  # frequency for the Y mark of the test model
shaper_type: mzv
```

** Video Coming Soon **
