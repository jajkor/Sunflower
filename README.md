🌻 Sunflower: A Heliotropic Solar Tracker

Sunflower is an embedded system project that mimics the heliotropic behavior of sunflowers by tracking the brightest light source using photoresistors and servos. The platform pans and tilts dynamically to optimize light exposure, demonstrating efficient and precise solar tracking.
🚀 Features

    Dynamic Solar Tracking: Adjusts pitch and yaw using photoresistor readings to follow the brightest light source.
    Real-Time Feedback: Displays solar panel voltage on an LCD screen.
    Hardware Safety: Implements servo clamping to protect against over-rotation.
    Heliotropic Design: Inspired by the natural movements of sunflowers.

🛠️ Hardware Requirements

    Microcontroller: Raspberry Pi Pico
    Sensors:
        4 Photoresistors (one at each corner of the platform)
        Fake_ADC module (for simulation purposes)
    Servos: 2 SG90 Servos (for pan and tilt)
    Additional Components:
        PCA9685 Servo Driver
        I2C LCD Display
        Power Supply (5V)
    Platform: Pan-tilt platform with photoresistors at each corner.

💻 Software Requirements

    Python (MicroPython)
    Libraries:
        pca9685 for servo control
        lcd for LCD interaction
        machine and time for microcontroller-specific functionality
        Fake_ADC for simulating ADC inputs during testing

📜 How It Works

    Photoresistor Readings:
        The system reads light intensity from photoresistors placed at the top, bottom, left, and right of the platform.

    Light Intensity Calculation:
        Top vs. Bottom and Left vs. Right light differences are calculated.

    Servo Adjustments:
        Based on the light differences, the servos incrementally adjust the platform's yaw and pitch to align with the brightest light source.
        The movement is clamped between 0° and 180° to prevent damage.

    Real-Time Voltage Display:
        The current solar panel voltage is displayed on the LCD.
