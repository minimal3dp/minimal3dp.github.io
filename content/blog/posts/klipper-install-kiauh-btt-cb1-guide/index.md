---
title: "How to Install Klipper with KIAUH (Step-by-Step BTT CB1 Guide)"
description: "Complete guide to flashing a BigTreeTech CB1 compute module and installing Klipper with KIAUH. Perfect for CR10 Smart Pro upgrades or any Klipper build."
date: 2025-12-07
lastmod: 2025-12-07
draft: false
categories: ["klipper", "tutorials", "3d-printers"]
tags: ["klipper", "btt-cb1", "kiauh", "cr10-smart-pro", "firmware-flashing"]
---

<style>
  pre code {
    color: #1a202c !important;
    background-color: #f7fafc !important;
  }
</style>

## Part 1: The "Part 0" Setup for the CR10 Smart Pro Upgrade

If you are looking to unlock the full potential of your 3D printer, moving to Klipper is the ultimate upgrade. But before we can configure printer settings or tune input shapers, we need a solid foundation.

In this guide (Part 1 of my **CR10 Smart Pro Upgrade Series**), I'm walking you through the "Part 0" essential setup: flashing the operating system to a BigTreeTech CB1 and installing the full Klipper software stack using KIAUH (Klipper Installation And Update Helper).

While I am performing this on a CR10 Smart Pro, this guide applies to anyone setting up a **BigTreeTech CB1** for the first time.

### 🛠️ Hardware Used in This Build

Below are the key components I used for this build. These are affiliate links—if you purchase through them, I earn a small commission at no extra cost to you, which helps support the channel.

{{< m3dp-card >}}

#### BigTreeTech CB1 Setup

<div class="affiliate-product-card">
  <div class="product-image">
    <img src="https://m.media-amazon.com/images/I/41QL2CMjsZL._SX342_.jpg" alt="BigTreeTech CB1 Compute Module">
  </div>
  <div class="product-info">
    <h4 class="product-title">BigTreeTech CB1 Compute Module</h4>
    <div class="price">$30–$40</div>
    <div class="product-description">High-performance compute module for 3D printer control. Drop-in replacement for Raspberry Pi CM4.</div>
  </div>
</div>
<a href="https://amzn.to/4rIZMhQ" class="btn btn-amazon" data-location="klipper_install_guide_hardware">Buy on Amazon</a>

---

<div class="affiliate-product-card">
  <div class="product-image">
    <img src="https://m.media-amazon.com/images/I/51+h9h2vvAL._SX342_.jpg" alt="BigTreeTech M5P Board">
  </div>
  <div class="product-info">
    <h4 class="product-title">BigTreeTech M5P Board</h4>
    <div class="price">$50–$80</div>
    <div class="product-description">Motherboard for CB1 integration. Supports multiple stepper motors and sensors.</div>
  </div>
</div>
<a href="https://amzn.to/48uRaCw" class="btn btn-amazon" data-location="klipper_install_guide_hardware">Buy on Amazon</a>

---

<div class="affiliate-product-card">
  <div class="product-image">
    <img src="https://m.media-amazon.com/images/I/81g1H8s5YDL._SX342_.jpg" alt="Reliable MicroSD Card 32GB">
  </div>
  <div class="product-info">
    <h4 class="product-title">Reliable MicroSD Card (32GB)</h4>
    <div class="price">$10–$15</div>
    <div class="product-description">High-speed card for OS imaging. Look for Class 10 or UHS-II rated cards for reliability.</div>
  </div>
</div>
<a href="https://amzn.to/3MloTXS" class="btn btn-amazon" data-location="klipper_install_guide_hardware">Buy on Amazon</a>

<p class="affiliate-disclosure">As an Amazon Associate, I earn from qualifying purchases. This helps support the channel at no extra cost to you.</p>

{{< /m3dp-card >}}

---

### Step 1: Imaging the SD Card

The first step is getting the operating system onto your microSD card.

1. **Download the Raspberry Pi Imager:** You'll need this tool to flash the image file. Download it from the official Raspberry Pi website.
2. **Download the CB1 Image:** Head to the BigTreeTech GitHub page. I am using the **CB1 Debian 12 Minimal Kernel 6.6 image**.
3. **Flash the Card:**
   - Open Raspberry Pi Imager.
   - Under **Device**, select "No Filtering" from the dropdown.
   - Under **OS**, scroll down to "Use Custom" and select the CB1 image you just downloaded.
   - Select your SD card (ensure you don't have important files on it, as it will be erased!).
   - Hit **Write**. This usually takes 3 to 5 minutes.

### Step 2: Configuring Wi-Fi (The Critical Step)

Before putting the card into the printer, we need to tell it how to connect to the network. **Note:** You cannot do this step easily on a Mac; it is best done on Windows.

1. Re-insert the finished SD card into your computer.
2. Open the drive and look for a file named `system.cfg`.
3. **Important:** Open this file with **Notepad++** (do not use WordPad, as it can mess up the formatting).
4. **Edit the Hostname:** I changed my hostname to `CR10-Smart-Pro` so it is easy to find on the network.
5. **Edit Wi-Fi Settings:** Uncomment (remove the `#`) the `WIFI_SSID` and `WIFI_PASSWD` lines. Enter your router name and password.
6. Save the file and eject the card.

### Step 3: First Boot and SSH Access

Insert the SD card into your CB1/Printer and power it on. Give it a few minutes to boot up.

1. Open **PuTTY** (or your preferred terminal).
2. Connect to the printer using the hostname you set (e.g., `CR10-Smart-Pro`) or its IP address.
3. **Default Credentials:**
   - Username: `root`
   - Password: `root`
4. The system will prompt you to change the password immediately. I also recommend setting up a standard user account (I set mine up as "mike") so you aren't always running as root.

### Step 4: Installing Klipper with KIAUH

The OS image provided by BigTreeTech is often a bit old (mine was nearly a year old), so we need to update it and install the 3D printing software.

1. **Update System:** Run the update commands provided in the terminal to ensure packages are current.
2. **Install Git:** You need Git installed to clone the KIAUH repository.
3. **Run KIAUH:**
   Clone the repo and launch the script:
   ```bash
   git clone https://github.com/dw-0/kiauh.git
   cd kiauh
   ./kiauh.sh
   ```

From the KIAUH menu, select **Install** (Option 1) and install the following components in order:

- **Klipper:** Select Python 3.x. When asked about instances, select "1" (since this CB1 manages one printer).
- **Moonraker:** Install with default config.
- **Mainsail:** This is my preferred web interface. It will default to port 80.
- **KlipperScreen:** Essential if you plan on adding a touchscreen later.
- **Crowsnest:** Install this if you plan to use a webcam for monitoring.

### Summary & What's Next

Once KIAUH finishes, you have a CB1 that is fully loaded with the Klipper ecosystem. However, the printer itself isn't printing yet.

In **Part 2**, we will take the next step: flashing the firmware to the printer's mainboard and configuring the `printer.cfg` file.

---

## 🎯 Resources & Tools

### Minimal 3DP Web Applications (Beta)

Stop guessing and start printing with precision using my custom tools:

{{< m3dp-cta type="calculator" location="klipper_install_guide_tools" >}}
Explore the **FDM Cost Calculator** to optimize your print costs and material waste.
{{< /m3dp-cta >}}

**📊 Available Tools:**
- **Start Here (Docs & Guides):** [minimal3dp.github.io](https://minimal3dp.github.io)
- **OrcaSlicer Profile Database:** [settings.minimal3dp.com](https://settings.minimal3dp.com)
- **Filament Tuning Database:** [filament.minimal3dp.com](https://filament.minimal3dp.com)

### ☕ Support the Channel

Did this guide save you hours of troubleshooting?

{{< m3dp-badge type="support" href="https://ko-fi.com/minimal3dp" location="klipper_install_guide_footer" >}}
Buy Me a Coffee
{{< /m3dp-badge >}}

Your support helps me create more in-depth guides like this one.
