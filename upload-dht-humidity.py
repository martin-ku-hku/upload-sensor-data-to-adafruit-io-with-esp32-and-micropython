import network
import urequests as requests
from machine import Pin
from dht import DHT11
from time import sleep

wifi_ssid = "YOUR_WIFI_SSID"
wifi_password = "YOUR_WIFI_PASSWORD"
aio_key = "YOUR_ADAFRUIT_IO_KEY"
username = "YOUR_ADAFRUIT_USERNAME"
feed_name = "humidity"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_password)
while not sta_if.isconnected():
    print(".", end = "")
    
dht11 = DHT11(Pin(15))

while True:
    dht11.measure()
    humidity = dht11.humidity()
    url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'
    body = {'value': str(humidity)}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
    except Exception as e:
        print(e)
    sleep(60)