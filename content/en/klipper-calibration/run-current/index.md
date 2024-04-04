---
date: 2024-04-03
title: Run Current for TMC2208/2209
linkTitle: Run Current
description: >
  Calculate your Run Current for your Steppers
author: Mike Wilson (minimal3dp@gmail.com)
draft: false
weight: 30
---

# Run Current

## From the Voron Docs

> Calculating Currents - To calculate the maximum Klipper current settings for a given stepper, follow this process: Look up the specifications for the stepper motor and locate the peak current limits of the motor. Multiply the peak current by 0.707 to determine the maximum current in RMS. This is the maximum run current.

[Calculating Driver Current Settings](https://docs.vorondesign.com/community/howto/120decibell/calculating_driver_current.html#:~:text=Calculating%20Currents,is%20the%20maximum%20run%20current.)

## Steps

The maximum Klipper RUN current settings can be calculated via the following steps:

1. Use the peak current limit from the stepper specifications sheet for the stepper motor.
2. Multiply the peak current by 0.707 to determine the max run current in RMS.
3. Round down to the nearest .1
4. Verify settings for each motor. 

** maximum capacity of the 2209 driver is 1.2 Amps. **

## Run Current Calculator

{{< run-current >}}

## Edit Printer.cfg

Edit the run current for each motor. 

```

```
