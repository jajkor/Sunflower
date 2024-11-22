# 🌻 Sunflower: A Heliotropic Solar Tracker

![20241122_162104c](https://github.com/user-attachments/assets/cda4e0fa-d941-4b97-a674-e8903f6aa09b)

## Overview

**Sunflower** is an embedded system project that was entered into the Penn State Abington Smart Systems Competition that mimics the heliotropic behavior of sunflowers by tracking the brightest light source using photoresistors and servos. The platform pans and tilts dynamically to optimize light exposure, demonstrating efficient and precise solar tracking.

- **Dynamic Solar Tracking:**
    - Adjusts pitch and yaw using photoresistor readings to follow the brightest light source.
- **Real-Time Feedback:**
    - Displays pan/tilt angles on an LCD screen.
- **Hardware Safety:**
    - Implements servo clamping to protect against over-rotation.
- **Heliotropic Design:**
    - Inspired by the natural movements of sunflowers.

## Hardware Requirements
- **Microcontroller:**
    - Raspberry Pi Pico
- **Sensors:**
    - 4 Photoresistors (one at each corner of the platform)
        - 3 ADC (using RPi ADC pins)
        - 1 Fake ADC (using an RC circuit)
- **Servos:**
    - 2 SG90 Servos (for pan and tilt)
- **Additional Components:**
    - PCA9685 Servo Driver
    - I2C LCD Display
    - Power Supply (5V)
- **Platform:**
    - Pan-tilt platform with photoresistors at each corner.

## How It Works
- **Photoresistor Readings:**
  - The system reads light intensity from photoresistors placed at the top, bottom, left, and right corners of the platform.

- **Light Intensity Calculation:**
  - Top vs. Bottom and Left vs. Right light differences are calculated.

- **Servo Adjustments:**
  - Based on the light differences, the servos incrementally adjust the platform's yaw and pitch to align with the brightest light source.
  - The movement is clamped between 0° and 180° to prevent damage.

- **Real-Time Pan/Titl Display:**
    - The current angle of the pan and tilt servos are displayed on the LCD.
