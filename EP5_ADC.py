from machine import Pin, ADC
import time

ldrPin=Pin(27)
ldr =ADC(ldrPin)

while 1:
    print(ldr.read_u16())
    time.sleep(1)