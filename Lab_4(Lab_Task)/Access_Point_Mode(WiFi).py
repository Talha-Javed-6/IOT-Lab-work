import network

# Create an Access point interface

ap = network.WLAN(network.AP_IF)
ap.active(True)


# Set AP Configuration
ap.config(essid='ESP-32-S3', password='123456789', authmode=network.AUTH_WPA2_PSK)


print("Access Point Created!!!")
print("IP Address:",ap.ifconfig())