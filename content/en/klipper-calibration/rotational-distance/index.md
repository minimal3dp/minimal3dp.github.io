---
date: 2024-03-31
title: Rotational Distance
linkTitle: Rotational Distance
description: >
  Calculate your Rotational Distance for Klipper
author: Mike Wilson (minimal3dp@gmail.com)
draft: false
---

# Rotational Distance

## From the Klipper Documents

On an extruder, the rotation_distance is the amount of distance the filament travels for one full rotation of the stepper motor. The best way to get an accurate value for this setting is to use a "measure and trim" procedure.

First start with an initial guess for the rotation distance. This may be obtained from steps_per_mm or by inspecting the hardware.

Then use the following procedure to "measure and trim":

1. Make sure the extruder has filament in it, the hotend is heated to an appropriate temperature, and the printer is ready to extrude.
2. Use a marker to place a mark on the filament around 70mm from the intake of the extruder body. Then use a digital calipers to measure the actual distance of that mark as precisely as one can. Note this as <initial_mark_distance>.
3. Extrude 50mm of filament with the following command sequence: G91 followed by G1 E50 F60. Note 50mm as <requested_extrude_distance>. Wait for the extruder to finish the move (it will take about 50 seconds). It is important to use the slow extrusion rate for this test as a faster rate can cause high pressure in the extruder which will skew the results. (Do not use the "extrude button" on graphical front-ends for this test as they extrude at a fast rate.)
4. Use the digital calipers to measure the new distance between the extruder body and the mark on the filament. Note this as <subsequent_mark_distance>. Then calculate: actual_extrude_distance = <initial_mark_distance> - <subsequent_mark_distance>
5. Calculate rotation_distance as: rotation_distance = <previous_rotation_distance> * <actual_extrude_distance> / <requested_extrude_distance> Round the new rotation_distance to three decimal places.

## Console Commands

```
G91
G1 E50 F60
```
## Rotational Distance Calculator 

{{< rotational-distance >}}

## Edit Printer.cfg

The value calculated should be pasted into your printer.cfg file under "Extruder".

```
[extruder]
step_pin: PD15
dir_pin: PD14
enable_pin: !PC7
microsteps: 16
rotation_distance: <PASTE HERE>
nozzle_diameter: 0.400
filament_diameter: 1.750
heater_pin: PB3
sensor_type: EPCOS 100K B57560G104F
sensor_pin: PA2
#control: pid
#pid_Kp: 22.2
#pid_Ki: 1.08
#pid_Kd: 114
min_temp: 0
max_temp: 250
max_extrude_cross_section: 4

```

