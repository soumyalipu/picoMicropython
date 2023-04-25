from machine import Pin
import time


led=Pin(0,Pin.OUT) #define GPIO 0 as OUTPUT
while True:
    
    led.value(1)           #turn on led
    print("Led is ON")
    time.sleep(1)
    led.value(0)			#turn off led
    print("Led is OFF")
    time.sleep(1)
