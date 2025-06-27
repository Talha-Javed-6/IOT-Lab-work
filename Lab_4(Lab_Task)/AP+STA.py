import network
import time


# Station Mode Setup
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('Talha', '13023994')


# Access Point mode setup
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP-32-S3', password='12345678', authmode= network.AUTH_WPA2_PSK)

print("Connecting to a Wi-Fi...")

# Wait for Station mode Connection
while not sta.isconnected:
    print("Connecting to a Wi-Fi...")
    time.sleep(2)


print("Connected in STA Mode!")
print("STA IP Address:", sta.ifconfig()[0])
print("AP IP Address:", ap.ifconfig()[0])