import network
import time

# Create a station interface
sta = network.WLAN(network.STA_IF)
sta.active(True)

# Connect to Wi-Fi
ssid = 'Talha'
password = '_--_--_--'
print("Connecting to Wi-Fi...")
sta.connect(ssid, password)

# Wait for connection

while not sta.isconnected():
    
    time.sleep(1)

print("Connected!")
print("IP Address:", sta.ifconfig()[0])
