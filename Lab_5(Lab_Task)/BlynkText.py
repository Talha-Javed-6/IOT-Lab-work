import BlynkLib as blynklib
import network
import uos
import utime as time
from machine import Pin, I2C, Timer
from neopixel import NeoPixel
import ssd1306

WIFI_SSID = 'Talha-Javed'
WIFI_PASS = '13023994'
BLYNK_AUTH = "0m9XRINprjWP1TPbAAy5YtG-4_pCjvjw"


print("Connecting to WiFi network '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig()[0])

print("Connecting to Blynk server...")
blynk = blynklib.Blynk(BLYNK_AUTH)


i2c = I2C(0, scl=Pin(8), sda=Pin(9), freq= 200000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


# Blynk Handlers for Virtual Pins
@blynk.on("V0")  
def v0_handler(value):
    try:
        # Parse the input text (expected format: "R,G,B")
        oled.fill(0)
        
        oled.text(value[0], 5,5)
        oled.show()
    except Exception as e:
        print("Invalid input:", e)
        
@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected!")
    blynk.sync_virtual(0)  # Sync RGB sliders from the app

@blynk.on("disconnected")
def blynk_disconnected():
    print("Blynk Disconnected!")

# Main Loop
while True:
    blynk.run()