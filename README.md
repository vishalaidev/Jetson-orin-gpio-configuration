# Jetson Orin GPIO Configuration

## 🚨 Problem

Most GPIO pins on the Jetson Orin 40-pin header **do not work as GPIO out-of-the-box**.  
Users frequently experience issues such as:

- Pins cannot be toggled from Python or sysfs  
- Jetson.GPIO shows errors like **“pin not configured”** or **“resource busy”**  
- Pins stay stuck at 0V or remain floating  
- `jetson-io.py` does not expose all pins as GPIO  
- Incorrect pinmux settings can cause the board to **freeze or fail to boot**  
- Many header pins are internally mapped to **SPI, I2S, I2C, PWM, UART**  
- The JetPack 6.x pinmux overlay system is poorly documented  
- Many developers online report **GPIO failure**, **overlay confusion**, and **ignored pin settings**

Because of this, even a simple task like blinking an LED becomes difficult unless the user manually edits the **device-tree pinmux**, which is time-consuming and error-prone.

This repository solves that problem by providing a **tested, ready-to-use device-tree overlay** that correctly reconfigures **9 header pins** into reliable GPIOs.

---

## ✅ Solution: Jetson Orin Nano / Orin Super — 9 GPIO Pins Overlay

This repository includes a **working DTS overlay** and **Python test script** to enable 9 GPIO pins on the NVIDIA Jetson Orin 40-pin header.

Default JetPack (6.x) assigns many pins to other peripherals like SPI/I2S/UART.  
This overlay safely remaps them into **general-purpose digital GPIOs**.

---

## 🔌 Enabled GPIO Pins (9 Total)

The following header pins are converted to GPIO:

```
12, 16, 18, 22, 32, 33, 35, 38, 40

```

These are fully controllable using **Jetson.GPIO** in Python.

---

## 🛠️ Setup Instructions

### 1️⃣ Compile the DTS overlay

```bash
dtc -O dtb -o gpio_9pins_sucessfully_test.dtbo gpio_9pins_sucessfully_test.dts
```

### 2️⃣ Copy overlay to the boot directory

```bash
sudo cp gpio_9pins_sucessfully_test.dtbo /boot/
```

### 3️⃣ Apply via Jetson-IO

```bash
sudo /opt/nvidia/jetson-io/jetson-io.py
```

Select:

```
GPIO Enable for Pins 12,16,18,22,32,33,35,38,40
```
<img width="548" height="603" alt="Screenshot from 2025-11-13 13-47-59" src="https://github.com/user-attachments/assets/647f060f-b7e0-4d00-87b3-b1bc43f28e39" />




Save & reboot.

---

## 🧪 Testing All 9 GPIO Pins

Run the provided Python script:

```bash(Device-tree work + GPIO validation)

If this helped you, please ⭐ the repository!




sudo python3 scripts/test_9_gpio.py
```

This script:

- Toggles each pin one-by-one  
- Blinks all 9 pins together  
- Verifies correct GPIO mode  

---

## 📌 Notes

- Requires JetPack **6.2.1**  
- Must run all GPIO scripts with **sudo**  
- Do not use these pins for SPI/I2S/UART while GPIO overlay is active  

---

## 🧑‍💻 Author

Created by **Vishal Maddeshiya**  
contact : vishalaidev7426@gmail.com
