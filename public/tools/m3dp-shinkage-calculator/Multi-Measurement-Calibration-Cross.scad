/*
 * OpenSCAD Script for a Multi-Measurement Calibration Cross
 *
 * This shape is designed to be a quick print (low height)
 * that provides multiple measurements for more
 * accurate shrinkage and hole compensation calculations.
 *
 * By averaging multiple measurements, you can
 * minimize the impact of any single small caliper error.
 */

// --- Main Parameters ---

total_length = 80;  // Total length/width of the cross
arm_width = 20;     // Width of each arm
height = 3;         // Height of the object (keeps print time low)
hole_diameter = 10; // Diameter of the small test holes
hole_position = 25; // Distance of holes from the center
smoothness = 100;   // $fn for cylinders (makes holes round)

// --- Main Body (Cross Shape) ---
module main_cross() {
    // Center the object at the origin
    translate([0, 0, height/2]) {
        union() {
            // X-Arm
            cube([total_length, arm_width, height], center = true);
            // Y-Arm
            cube([arm_width, total_length, height], center = true);
        }
    }
}

// --- Holes Module ---
module test_holes() {
    // Use height+2 as a "cutter" to ensure it goes all the way through
    cutter_height = height + 2; 
    
    // Hole in positive X-Arm
    translate([hole_position, 0, 0]) {
        cylinder(d = hole_diameter, h = cutter_height, center = true, $fn = smoothness);
    }
    
    // Hole in negative X-Arm
    translate([-hole_position, 0, 0]) {
        cylinder(d = hole_diameter, h = cutter_height, center = true, $fn = smoothness);
    }
    
    // Hole in positive Y-Arm
    translate([0, hole_position, 0]) {
        cylinder(d = hole_diameter, h = cutter_height, center = true, $fn = smoothness);
    }
    
    // Hole in negative Y-Arm
    translate([0, -hole_position, 0]) {
        cylinder(d = hole_diameter, h = cutter_height, center = true, $fn = smoothness);
    }
}

// --- Final Assembly ---
// Subtract the holes from the main cross
difference() {
    main_cross();
    test_holes();
}

/*
 * --- HOW TO USE THIS MODEL ---
 * 1. In OpenSCAD, press F6 to render, then export as STL.
 * 2. Print the new STL.
 * 3. With your calipers, take 8 measurements:
 *
 * Outer Measurements (for Shrinkage):
 * - A: Total X-length (Designed: 80mm)
 * - B: Total Y-length (Designed: 80mm)
 * - C: X-arm width (Designed: 20mm)
 * - D: Y-arm width (Designed: 20mm)
 *
 * Inner Measurements (for Hole Comp.):
 * - E: Hole 1 diameter (Designed: 10mm)
 * - F: Hole 2 diameter (Designed: 10mm)
 * - G: Hole 3 diameter (Designed: 10mm)
 * - H: Hole 4 diameter (Designed: 10mm)
 *
 * 4. Go to the web calculator:
 *
 * - In "1. Outer Dimensions":
 * - Set Designed Outer: (80+80+20+20) / 4 = 50
 * - Set Measured X: (A+B) / 2
 * - Set Measured Y: (C+D) / 2
 * - OR, even better:
 * - Set Designed Outer: 50
 * - Set Measured X: (A+B+C+D) / 4
 * - Set Measured Y: (A+B+C+D) / 4  <-- Use the same average
 *
 * - In "2. Inner Dimensions":
 * - Set Designed Hole: 10
 * - Set Measured Hole: (E+F+G+H) / 4
 *
 * 5. Click "Calculate". This will give you a very accurate,
 * statistically-sound result.
 */