import time
import machine
import network
import urequests
import dht

# Sensor Pin Definitions
npk_pin = machine.ADC(0)  # Example: NPK sensor connected to ADC pin
ph_pin = machine.ADC(1)   # Example: pH sensor connected to ADC pin
moisture_pin = machine.ADC(2)  # Example: Moisture sensor connected to ADC pin

# WiFi credentials
wifi_ssid = "Your_WiFi_SSID"
wifi_password = "Your_WiFi_Password"

# API URL (Replace with your Flask API endpoint)
api_url = "http://<server-ip>:5000/api"

# Initialize the WiFi connection
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(wifi_ssid, wifi_password)
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to WiFi:', wifi_ssid)

# Function to read sensor values (simplified for example)
def read_sensors():
    npk_value = npk_pin.read()  # Reading NPK sensor value
    ph_value = ph_pin.read()    # Reading pH sensor value
    moisture_value = moisture_pin.read()  # Reading moisture sensor value
    return npk_value, ph_value, moisture_value

# Function to send data to server
def send_data(npk, ph, moisture):
    data = {
        'npk': npk,
        'ph': ph,
        'moisture': moisture
    }
    try:
        response = urequests.post(api_url, json=data)
        print("Data sent:", response.status_code)
    except Exception as e:
        print("Error sending data:", e)

# Main loop
connect_wifi()
while True:
    npk, ph, moisture = read_sensors()
    send_data(npk, ph, moisture)
    time.sleep(60)  # Send data every 60 seconds
