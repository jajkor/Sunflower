from pca9685 import PCA9685
from machine import I2C, Pin, ADC
from lcd import LCD
from servo import Servos
from fake_adc import Fake_ADC
import time

# Read voltage from solar panel
fakeVolt = Fake_ADC(17)

# Read voltage from photoresistors
photoTL = ADC(26)
fakeBL = Fake_ADC(16)
photoTR = ADC(27)
photoBR = ADC(28)

# Threshold value between sides
threshold = 1000

# Servos
yaw = 90
pitch = 90

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id=id, sda=sda, scl=scl)
pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)

servo.position(index=0, degrees=yaw)
servo.position(index=1, degrees=pitch)

# LCD
lcd = LCD()

while True:
    # Read values from photoresistors
    read_tl = photoTL.read_u16()
    read_bl = fakeBL.read_light_level()
    read_tr = photoTR.read_u16()
    read_br = photoBR.read_u16()
    
    # Top
    read_top = read_tl + read_tr
    # Bottom
    read_bot = read_bl + read_br
    # Left
    read_left = read_tl + read_bl
    # Right
    read_right = read_tr + read_br

    print("TOP: " + str(read_top))
    print("BOT: " + str(read_bot))
    print("LEFT: " + str(read_left))
    print("RIGHT: " + str(read_right))
    print()

    # Adjust pitch
    diff_tb = read_top - read_bot
    if abs(diff_tb) > threshold:
        if diff_tb < 0:
            pitch += 5
        else:
            pitch -= 5
        pitch = clamp(pitch, 0, 180)  # Ensure pitch stays in bounds
        servo.position(index=1, degrees=pitch)
        print(f"Adjusted PITCH to {pitch}")
    else:
        print("PITCH STABLE")

    # Adjust yaw
    diff_lr = read_right - read_left
    if abs(diff_lr) > threshold:
        if diff_lr < 0:
            yaw += 5
        else:
            yaw -= 5
        yaw = clamp(yaw, 0, 180)  # Ensure yaw stays in bounds
        servo.position(index=0, degrees=yaw)
        print(f"Adjusted YAW to {yaw}")
    else:
        print("YAW STABLE")

    print("YAW: " + str(yaw))
    print("PITCH: " + str(pitch))
        
    # Print voltage from solar panel on LCD
    #volt_SP = fakeVolt.read_light_level()
    #volt_SP_str = "SP: " + str(volt_SP)
    #lcd.lcd_print(volt_SP_str, 0)

    time.sleep(0.5)                # Add delay between readings
