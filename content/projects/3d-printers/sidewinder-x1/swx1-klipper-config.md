---
title: Sidewinder X1 (SWX1) Klipper Config
description: >
  SWX1 with a BTT SKR 2
date: 2024-04-06
weight: 2
categories: [Klipper, Configs]
tags: [klipper, swx1]
draft: false
---

{{% pageinfo %}}
SWX1 with a BTT SKR 2
{{% /pageinfo %}}

[GitHub Backup](https://github.com/minimal3dp/swx1-skr2-klipper/tree/main)

```
[include shell_command.cfg]
[include fluidd.cfg]
[include mainsail.cfg]

# This file contains common pin mappings for the BigTreeTech SKR 2.
# To use this config, the firmware should be compiled for the
# STM32F407 with a "32KiB bootloader".

# In newer versions of this board shipped in late 2021 the STM32F429
# is used, if this is the case compile for this with a "32KiB bootloader"
# You will need to check the chip on your board to identify which you have.
#
# The "make flash" command does not work on the SKR 2. Instead,
# after running "make", copy the generated "out/klipper.bin" file to a
# file named "firmware.bin" on an SD card and then restart the SKR 2
# with that SD card.

# See docs/Config_Reference.md for a description of parameters.

# Note: The initial revision of this board has a flaw that can cause
# damage to itself and other boards. Be sure to verify the board is
# not impacted by this flaw before using it.

[stepper_x]
step_pin: PE2
dir_pin: !PE1
enable_pin: !PE3
microsteps: 16
rotation_distance: 40
endstop_pin: ^!PC1
position_endstop: 0
position_max: 300
homing_speed: 100

[tmc2209 stepper_x]
uart_pin: PE0
run_current: 0.800
diag_pin:

[stepper_y]
step_pin: PD5
dir_pin: !PD4
enable_pin: !PD6
microsteps: 16
rotation_distance: 40
endstop_pin: ^!PC3
position_endstop: 0
position_max: 300
homing_speed: 100

[tmc2209 stepper_y]
uart_pin: PD3
run_current: 0.800
diag_pin:

[stepper_z]
step_pin: PA15
dir_pin: PA8
enable_pin: !PD1
microsteps: 16
rotation_distance: 8
endstop_pin: probe:z_virtual_endstop
position_max: 400
homing_speed: 20
second_homing_speed: 1

[tmc2209 stepper_z]
uart_pin: PD0
run_current: 0.800
diag_pin:

[stepper_z1]
step_pin: PD11
dir_pin: PD10
enable_pin: !PD13
microsteps: 16
rotation_distance: 8

[tmc2209 stepper_z1]
uart_pin: PD12
run_current: 0.800
diag_pin:

[extruder]
step_pin: PD15
dir_pin: PD14
enable_pin: !PC7
microsteps: 16
rotation_distance: 33.500
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

[tmc2209 extruder]
uart_pin: PC6
run_current: 0.600
diag_pin:

[heater_bed]
heater_pin: PD7
sensor_type: EPCOS 100K B57560G104F
sensor_pin: PA1
#control: pid
min_temp: 0
max_temp: 130
#pid_kp: 42.365
#pid_ki: 0.545
#pid_kd: 822.940

[fan]
pin: PB7

[heater_fan fan1]
pin: PB6

#[heater_fan fan2]
#pin: PB5

# Due to BTT implementing a Marlin-specific safety feature,
# "anti-reversal stepper protection", this pin needs pulling
# high to pass power to stepper drivers and most FETs

[output_pin motor_power]
pin: PC13
value: 1

[mcu]
serial: /dev/serial/by-id/usb-Klipper_stm32f429xx_200044001450304738323420-if00

[printer]
kinematics: cartesian
max_velocity: 250
max_accel: 3000
max_z_velocity: 50
max_z_accel: 400
square_corner_velocity: 5.0

[bltouch]
## If these change, adjust coords in [z_tilt], [safe_z_home]
sensor_pin: ^PE4
control_pin: PE5
x_offset: 29
y_offset: -34
z_offset: 10
samples: 3
samples_result:average
probe_with_touch_mode: true
stow_on_each_sample: false

[safe_z_home]
home_xy_position: 122,183
speed: 150
z_hop: 10  # Move up 10mm
z_hop_speed: 5

[bed_screws]
screw1: 55,55
screw1_name: front left
screw2: 255,55
screw2_name: front right
screw3: 255,255
screw3_name: back right
screw4: 55,255
screw4_name: back left
speed: 100.0


[screws_tilt_adjust]
screw1: 22,83
screw1_name: front left
screw2: 222,83
screw2_name: front right
screw3: 22,283
screw3_name: back left
screw4: 222,283
screw4_name: back right
speed: 100.0
screw_thread: CW-M5

[bed_mesh]
speed: 800
mesh_min: 30,30
mesh_max: 270,270
probe_count: 5,5
mesh_pps: 2,2
algorithm: bicubic
bicubic_tension: 0.2
move_check_distance: 3.0
split_delta_z: .010
fade_start: 1.0
fade_end: 5.0

########################################
# EXP1 / EXP2 (display) pins
########################################

[board_pins]
aliases:
    # EXP1 header
    EXP1_1=PC5, EXP1_3=PB1, EXP1_5=PE10, EXP1_7=PE12, EXP1_9=<GND>,
    EXP1_2=PB0, EXP1_4=PE9, EXP1_6=PE11, EXP1_8=PE13, EXP1_10=<5V>,
    # EXP2 header
    EXP2_1=PA6, EXP2_3=PE7, EXP2_5=PB2, EXP2_7=PC4,   EXP2_9=<GND>,
    EXP2_2=PA5, EXP2_4=PA4, EXP2_6=PA7, EXP2_8=<RST>, EXP2_10=<NC>

# See the sample-lcd.cfg file for definitions of common LCD displays.

[gcode_macro update_git]
gcode:
    RUN_SHELL_COMMAND CMD=update_git_script

[gcode_shell_command update_git_script]
command: bash /home/wilsonm/printer_1_data/klipper-backup/script.sh
timeout: 90.0
verbose: True


```
