from machine import Pin
import time
led=Pin(0,Pin.OUT) #define GPIO 0 as OUTPUT
switch=Pin(2,Pin.IN, Pin.PULL_UP)
while True:
    data=switch.value()
    print(data)
    time.sleep(.1)
    if data==0:
        print("Button pressed")
        led.value(1)
    else:
        print("Button release")
        led.value(0)