# Name: Muhammad Talha Javed
# Reg:  22-NTU-CS-1366
# Home task: 2.1 Working with Neopixel and input button



print("Hello, ESP32!")


from machine import Pin
from neopixel import NeoPixel
import time

btn =Pin(0, Pin.IN, Pin.PULL_UP)    # same pin for physical esp32 s3 built in Boot buton
pin = Pin(33, Pin.OUT)              # set 48 for your physical esp32 s3  
neo = NeoPixel(pin, 1)              # create NeoPixel driver  for 1 pixel
while True:
    while(btn.value()==1):          # flashing of neopixel stopped when button is in pressed status
        neo[0] = (255, 0, 0)            # set the first pixel to red
        print("red")
    
        neo.write()                     # write data to all pixels
        time.sleep(.2)
        neo[0] = (0, 255, 0)            # set the first pixel to green
        print("green")
        
    
        neo.write()                     # write data to all pixels
        time.sleep(.2)       
        neo[0] = (0, 0, 255)            # set the first pixel to blue
        print("blue")
    
        neo.write()                     # write data to all pixels
        time.sleep(.2)
        
print("starting of neopixel flashing ")          # just checking printing output
from machine import Pin
from neopixel import NeoPixel
import time

# Pin configuration
btn = Pin(0, Pin.IN, Pin.PULL_UP)  # Built-in boot button on ESP32-S3
pin = Pin(33, Pin.OUT)             # Pin connected to the NeoPixel (use 48 for your setup)
neo = NeoPixel(pin, 1)             # Create NeoPixel driver for 1 pixel

# Interrupt Service Routine (ISR) for button press
def button_isr(pin):
    
    while(btn.value()==0):
        continue     

# Attach the ISR to the button pin
btn.irq(trigger=Pin.IRQ_FALLING, handler=button_isr)

# Main loop
while True:
    while(btn.value()==1):  # Flash NeoPixel only if the button is not pressed
        neo[0] = (255, 0, 0)  # Set the first pixel to red
        neo.write()           # Write data to the pixel
        print("Red")
        time.sleep(0.4)

        neo[0] = (0, 255, 0)  # Set the first pixel to green
        neo.write()           # Write data to the pixel
        print("Green")
        time.sleep(0.4)
        neo[0] = (0, 0, 255)  # Set the first pixel to green
        neo.write()           # Write data to the pixel
        print("Blue")
        time.sleep(0.4)

    
    
    
    
from machine import Pin
from neopixel import NeoPixel
import time

# Pin configuration
btn = Pin(0, Pin.IN, Pin.PULL_UP)  # Built-in boot button on ESP32-S3
pin = Pin(33, Pin.OUT)             # Pin connected to the NeoPixel
neo = NeoPixel(pin, 1)             # Create NeoPixel driver for 1 pixel

# Global variables
press_count = 0  # Counter for button presses
color_index = 0  # Index to cycle through colors

# Colors (Red → Green → Blue)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

while True:
    if btn.value() == 0:  # Button is pressed
        time.sleep_ms(150)  # Debounce
        if btn.value() == 0:  # Ensure it's still pressed
            press_count += 1
            print(f"Press count: {press_count}")

            while btn.value() == 0:  # Wait for button release
                time.sleep_ms(10)

    if press_count == 5:  # Change color after 5 presses
        press_count = 0  # Reset counter
        color_index = (color_index + 1) % 3  # Cycle through 3 colors
        neo[0] = colors[color_index]  # Set new color
        neo.write()
        print(f"Color changed to: {colors[color_index]}")

    time.sleep_ms(10)  # Small delay to avoid CPU overload

    

