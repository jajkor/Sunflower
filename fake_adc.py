from machine import Pin
from time import sleep_ms

class Fake_ADC:
    def __init__(self, num):
        self.p = Pin(num, Pin.OUT)
        
    def read_light_level(self):
        # Step 1: Discharge the capacitor
        self.p.init(Pin.OUT)    # Set as output
        self.p.value(0)                 # Set low to discharge
        sleep_ms(10)            # Wait for discharge (adjust if necessary)

        # Step 2: Start charging by setting pin as input
        self.p.init(Pin.IN)     # Set as input to start charging

        # Step 3: Monitor the charge time
        count = 0
        while self.p.value() == 0:      # Loop until the capacitor reaches high voltage threshold (~2V)
            count += 1

        return count 
