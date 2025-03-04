# Without interrupts

import dht #For DHT Sensor
from machine import Pin, I2C # For Pin configuration
from ssd1306 import SSD1306_I2C # Library for OLED display
import time

# Setting up the DHT11 Sensor
sensor = dht.DHT11(Pin(4))

# Setting up OLED and I2C
i2c = I2C(0, scl=Pin(8), sda=Pin(9))
oled = SSD1306_I2C(128, 64, i2c)



# simple bitmaps for icons
hot_icon = [
    0b00011000,
    0b00111100,
    0b01111110,
    0b11111111,
    0b11111111,
    0b01111110,
    0b00111100,
    0b00011000
]

cold_icon = [
    0b00011000,
    0b00100100,
    0b01000010,
    0b10011001,
    0b10011001,
    0b01000010,
    0b00100100,
    0b00011000
]

water_drop = [
    0b00011000,
    0b00111100,
    0b01111110,
    0b11111111,
    0b11111111,
    0b01111110,
    0b00111100,
    0b00011000
]

dry_icon = [
    0b00011000,
    0b00100100,
    0b01000010,
    0b10000001,
    0b10000001,
    0b01000010,
    0b00100100,
    0b00011000
]

# Function to draw bitmap at a given position
def draw_bitmap(x, y, bitmap):
    for i in range(8):
        for j in range(8):
            if bitmap[i] & (1 << (7 - j)):
                oled.pixel(x + j, y + i, 1)

while True:
    try:
        # Measure temperature and humidity
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        
        print(f"Temp: {temperature} C , Humidity:{humidity} %")
        
        
        # Clear the Display
        oled.fill(0)
        
        
         # Display temperature with icon
        oled.text("Today's Weather", 4, 0)
        if temperature > 30:
            draw_bitmap(0, 20, hot_icon)   # Hot indicator
        else:
            draw_bitmap(0, 20, cold_icon)  # Cold indicator

        oled.text("Temp: {} C".format(temperature), 10, 20)

        # Display humidity with icon
        if humidity > 60:
            draw_bitmap(0, 40, water_drop)  # High humidity indicator
        else:
            draw_bitmap(0, 40, dry_icon)    # Low humidity indicator

        oled.text("Humidity: {} %".format(humidity), 10, 40)
        
        # Display Temp. And Humidity
        #oled.text("Today's Weather", 4, 0)
        #oled.text("Temp: {} C".format(temperature), 0, 20)
        #oled.text("Humidity: {} %".format(humidity), 0, 40)
        
        
    
        # Update Display
        oled.show()
    except OSError as e:
        oled.fill(0)
        oled.text("Sensor Error!", 16, 28)
        oled.show()
    
    
    time.sleep(3) # Delay for some second before next reading

