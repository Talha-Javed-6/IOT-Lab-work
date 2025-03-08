import network 
import time 
WIFI_SSID = "Talha" 
WIFI_PASS = "_--_--_--" 
wifi = network.WLAN(network.STA_IF) 
wifi.active(True) 
wifi.connect(WIFI_SSID, WIFI_PASS) 
print("Connecting to Wi-Fi...") 
while not wifi.isconnected(): 
time.sleep(1) 
print("Retrying...") 
print("Connected! IP:", wifi.ifconfig()[0]) 