---
title: Ender 3 S1 Plus (e3s1p) Klipper Config
description: >
  Ender 3 S1 Plus with the default Creality Board
date:
weight: 2
categories: [Klipper, Configs]
tags: [klipper, Ender 3, s1 plus]
draft: false
---

{{% pageinfo %}}
Ender 3 S1 Plus with the default Creality Board
{{% /pageinfo %}}

```
# !Ender-3 S1 Plus
# printer_size: 300x300x300
# version: 3.6
# This file contains pin mappings for the stock 2021 Creality Ender 3
# S1 & S1 Pro. To use this config, check the STM32 Chip on the
# Mainboard, during "make menuconfig" select accordingly either the
# STM32F103 with "28KiB bootloader" or the STM32F401 with
# "64KiB bootloader" and serial (on USART1 PA10/PA9) for both.

# For a direct serial connection, in "make menuconfig" select
# "Enable extra low-level configuration options" and  Serial
# (on USART2 PA3/PA2), which is on the 10 pin IDC cable used

# Flash this firmware by copying "out/klipper.bin" to a SD card and
# turning on the printer with the card inserted. The filename
# must be changed to "firmware.bin"

# With STM32F401, you might need to put "firmware.bin" in a
# folder on the SD card called "STM32F4_UPDATE" in order to flash.

# See docs/Config_Reference.md for a description of parameters.


###fluidd set
[include cx_printer.cfg]

[display_status]

[pause_resume]

[gcode_macro PAUSE]
description: Pause the actual running print
rename_existing: PAUSE_BASE
# change this if you need more or less extrusion
variable_extrude: 1.0
gcode:
  ##### read E from pause macro #####
  {% set E = printer["gcode_macro PAUSE"].extrude|float %}
  ##### set park positon for x and y #####
  # default is your max posion from your printer.cfg
  {% set x_park = printer.toolhead.axis_maximum.x|float - 5.0 %}
  {% set y_park = printer.toolhead.axis_maximum.y|float - 5.0 %}
  ##### calculate save lift position #####
  {% set max_z = printer.toolhead.axis_maximum.z|float %}
  {% set act_z = printer.toolhead.position.z|float %}
  {% if act_z < (max_z - 2.0) %}
      {% set z_safe = 2.0 %}
  {% else %}
      {% set z_safe = max_z - act_z %}
  {% endif %}
  ##### end of definitions #####
  PAUSE_BASE
  G91
  {% if printer.extruder.can_extrude|lower == 'true' %}
    G1 E-{E} F2100
  {% else %}
    {action_respond_info("Extruder not hot enough")}
  {% endif %}
  {% if "xyz" in printer.toolhead.homed_axes %}
    G1 Z{z_safe} F900
    G90
    G1 X{x_park} Y{y_park} F6000
  {% else %}
    {action_respond_info("Printer not homed")}
  {% endif %}

[gcode_macro RESUME]
description: Resume the actual running print
rename_existing: RESUME_BASE
gcode:
  ##### read E from pause macro #####
  {% set E = printer["gcode_macro PAUSE"].extrude|float %}
  #### get VELOCITY parameter if specified ####
  {% if 'VELOCITY' in params|upper %}
    {% set get_params = ('VELOCITY=' + params.VELOCITY)  %}
  {%else %}
    {% set get_params = "" %}
  {% endif %}
  ##### end of definitions #####
  {% if printer.extruder.can_extrude|lower == 'true' %}
    G91
    G1 E{E} F2100
  {% else %}
    {action_respond_info("Extruder not hot enough")}
  {% endif %}
  RESUME_BASE {get_params}

[gcode_macro CANCEL_PRINT]
description: Cancel the actual running print
rename_existing: CANCEL_PRINT_BASE
gcode:
  TURN_OFF_HEATERS
  {% if "xyz" in printer.toolhead.homed_axes %}
    G91
    G1 Z4.5 F300
    G90
  {% else %}
    {action_respond_info("Printer not homed")}
  {% endif %}
    G28 X Y
  {% set y_park = printer.toolhead.axis_maximum.y|float - 5.0 %}
    G1 Y{y_park} F2000
    M84
  CANCEL_PRINT_BASE

[stepper_x]
step_pin: PC2
dir_pin: PB9
enable_pin: !PC3
rotation_distance: 40
microsteps: 16
endstop_pin: !PA5
position_min: -5
position_endstop: -5
position_max: 305
homing_speed: 80

[stepper_y]
step_pin: PB8
dir_pin: PB7
enable_pin: !PC3
rotation_distance: 40
microsteps: 16
endstop_pin: !PA6
position_min: -2
position_endstop: -2
position_max: 305
homing_speed: 80

[stepper_z]
step_pin: PB6
dir_pin: !PB5
enable_pin: !PC3
rotation_distance: 8
microsteps: 16
endstop_pin: probe:z_virtual_endstop           #enable to use bltouch
#endstop_pin: !PA15                #disable to use bltouch
#position_endstop: -0.1
position_min: -10
position_max: 305
homing_speed: 4
second_homing_speed: 1
homing_retract_dist: 2.0

[extruder]
max_extrude_only_distance: 1000.0
step_pin: PB4
dir_pin: PB3
enable_pin: !PC3
rotation_distance: 7.74
microsteps: 16
nozzle_diameter: 0.400
filament_diameter: 1.750
heater_pin: PA1
sensor_type: EPCOS 100K B57560G104F
sensor_pin: PC5
#control: pid
# tuned for stock hardware with 200 degree Celsius target
#pid_Kp: 23.904
#pid_Ki: 1.476
#pid_Kd: 96.810
min_temp: 0
max_temp: 265

[idle_timeout]
timeout: 172800

[heater_bed]
heater_pin: PA7
sensor_type: EPCOS 100K B57560G104F
sensor_pin: PC4
#control: pid
# tuned for stock hardware with 50 degree Celsius target
#pid_Kp: 74.000
#pid_Ki: 1.965
#pid_Kd: 696.525
min_temp: 0
max_temp: 130


[verify_heater extruder]
check_gain_time: 200
hysteresis: 5

[fan]
pin: PA0
kick_start_time: 0.5

#set heater fan runnig with temperature over 60;
[heater_fan my_nozzle_fan]
pin: PC0
max_power: 0.8
shutdown_speed : 0
heater:extruder
heater_temp : 60
fan_speed : 1.0


[mcu]
serial: /dev/serial/by-id/usb_serial_1
restart_method: command

# [mcu rpi]
# serial: /tmp/klipper_host_mcu

# [adxl345]
# cs_pin: rpi:None
# spi_speed: 2000000
# spi_bus: spidev2.0

# [resonance_tester]
# accel_chip: adxl345
# accel_per_hz: 70
# probe_points:
#     150,150,10

[input_shaper]
shaper_type_x = mzv
shaper_freq_x = 59.2
shaper_type_y = mzv
shaper_freq_y = 30.0

[filament_switch_sensor filament_sensor]
pause_on_runout: true
switch_pin: ^!PC15


[bltouch]
sensor_pin: ^PC14       #signal check port ^stand for pull up
control_pin: PC13       #singal control prot
x_offset: -30.0
y_offset: -40.0
#z_offset: 0          #z off_set configuration
stow_on_each_sample = false #high speed for bltoch,
speed: 3.0
samples: 2
samples_result: median
sample_retract_dist: 6.0
samples_tolerance: 0.01
samples_tolerance_retries: 3

[safe_z_home]
home_xy_position:185,195
speed: 200
z_hop: 10
z_hop_speed: 10

[bed_mesh]
speed: 150
mesh_min: 25,30         #need to handle head distance with bl_touch
mesh_max: 273,250       #max probe range
probe_count: 5,5
fade_start: 1
fade_end: 10
algorithm: bicubic

[bed_screws]
screw1: 25, 33
screw2: 262, 33
screw3: 262, 272
screw4: 25, 272


[gcode_arcs]
#resolution: 1.0

[printer]
kinematics: cartesian
max_velocity: 300
max_accel: 4000
max_z_velocity: 10
max_z_accel: 1000
square_corner_velocity: 5.0

[exclude_object]

[include timelapse.cfg]
[include cx_gmcro.cfg]


