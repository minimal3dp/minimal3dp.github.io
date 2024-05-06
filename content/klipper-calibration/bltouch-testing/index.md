---
date: 2024-05-06
title: Testing a Bltouch, CRTouch, ora clone in Klipper
linkTitle: Bltouch Testing
description: >
  Testing a BLTOUCH or a clone in Klipper
author: Mike Wilson (minimal3dp@gmail.com)
draft: false
weight: 100
---

Testing a BLTouch with Klipper involves several steps to ensure that the probe is functioning correctly. Here's a simplified process:

1. **Initial Setup**: Make sure the BLTouch is correctly mounted and the pin is about 2 mm above the nozzle when retracted (1).

2. **Self-Test**: Power on the printer; the BLTouch should perform a self-test, moving the pin up and down. After this, the pin should retract, and the red LED should light up (1).

3. **Control Pin Test**:
   - Send `BLTOUCH_DEBUG COMMAND=pin_down` in the printer terminal to move the pin down.
	 
	 ```
	 BLTOUCH_DEBUG COMMAND=pin_down
	 ```
	 
   - Verify that the red LED turns off.
   - Send `BLTOUCH_DEBUG COMMAND=pin_up` to retract the pin and ensure the red LED turns on (1).
	 
	 ```
	 BLTOUCH_DEBUG COMMAND=pin_up
	 ```
	
4. **Sensor Pin Test**:
   - With the pin down, send `BLTOUCH_DEBUG COMMAND=touch_mode`, then `QUERY_PROBE` and check for "probe: open".
	 
	 ```
	 BLTOUCH_DEBUG COMMAND=touch_mode
	 ```
	 &
	 ```
	 QUERY_PROBE
	 ```
	 
   - Gently push the pin up with your finger, send `QUERY_PROBE` again, and look for "probe: TRIGGERED".
	 
	 ```
	QUERY_PROBE	
	```
	 
   - If the responses are incorrect, check your wiring and configuration (1).
	 
5. **Probing Test**: Move the print head away from the bed and repeat the control and sensor pin tests to confirm the probe's response when not near the bed surface (1).

Remember to handle the BLTouch probe gently and avoid touching the pin with your fingers, as it's sensitive to grease and pressure. If you encounter any issues during these tests, it's usually a sign to double-check your wiring and configuration settings¹. Always refer to the official Klipper documentation for detailed instructions and troubleshooting tips. Happy printing!

References:
(1) [BL-Touch - Klipper documentation.](https://www.klipper3d.org/BLTouch.html)
(2) [Klipper & BLTouch: How to Make Them Work Together | All3DP.](https://all3dp.com/2/klipper-bltouch-simply-explained)
(3) [Testing the BLTouch - MatterHackers Knowledge Base](https://help.matterhackers.com/article/196-testing-bltouch)
(4) [klipper/docs/BLTouch.md at master · Klipper3d/klipper · GitHub](https://github.com/Klipper3d/klipper/blob/master/docs/BLTouch.md)