from machine import Pin
import utime

from dht import DHT11, InvalidChecksum


# Wait 1 second to let the sensor power up
utime.sleep(1)

pin = Pin(0, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)
while 1:
    try:
        print("Temperature: {}".format(sensor.temperature))
        print("Humidity: {}".format(sensor.humidity))
        utime.sleep(5)
    except InvalidChecksum:
        print("Checksum from the sensor was invalid")
