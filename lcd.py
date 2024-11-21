from machine import Pin
from time import sleep

class LCD:
    def __init__(self):
        # Define LCD GPIO pins
        self.RS = Pin(7, Pin.OUT)
        self.E = Pin(8, Pin.OUT)
        self.D4 = Pin(10, Pin.OUT)
        self.D5 = Pin(11, Pin.OUT)
        self.D6 = Pin(12, Pin.OUT)
        self.D7 = Pin(13, Pin.OUT)
        self.lcd_init()

    # Function to toggle the enable pin
    def lcd_toggle_enable(self):
        self.E.value(1)
        sleep(0.0005)  # Enable pulse must be > 450 ns
        self.E.value(0)
        sleep(0.0005)  # Commands need > 37 us to settle

    # Send a 4-bit command to the LCD
    def lcd_send_4bits(self, bits):
        self.D4.value((bits >> 0) & 1)
        self.D5.value((bits >> 1) & 1)
        self.D6.value((bits >> 2) & 1)
        self.D7.value((bits >> 3) & 1)
        self.lcd_toggle_enable()

    # Send a command to the LCD
    def lcd_command(self, cmd):
        self.RS.value(0)  # RS = 0 -> Command mode
        self.lcd_send_4bits(cmd >> 4)
        self.lcd_send_4bits(cmd & 0x0F)

    # Send a character to the LCD
    def lcd_write_char(self, char):
        self.RS.value(1)  # RS = 1 -> Data mode
        self.lcd_send_4bits(ord(char) >> 4)
        self.lcd_send_4bits(ord(char) & 0x0F)

    # Initialize the LCD
    def lcd_init(self):
        self.lcd_command(0x33)  # Initialize in 4-bit mode
        self.lcd_command(0x32)  # Set to 4-bit mode
        self.lcd_command(0x28)  # 2 lines, 5x7 matrix
        self.lcd_command(0x0C)  # Display on, cursor off
        self.lcd_command(0x06)  # Increment cursor
        self.lcd_command(0x01)  # Clear display
        sleep(0.005)

    # Clear the LCD screen
    def lcd_clear(self):
        self.lcd_command(0x01)  # Clear display
        sleep(0.005)

    # Set cursor position
    def lcd_set_cursor(self, line, position):
        if line == 0:
            self.lcd_command(0x80 + position)
        elif line == 1:
            self.lcd_command(0xC0 + position)

    # Display a string on the LCD
    def lcd_print(self, text, line=0):
        self.lcd_set_cursor(line, 0)
        for char in text:
            self.lcd_write_char(char)
