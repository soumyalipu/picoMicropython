from machine import Pin, PWM
import time
led=Pin(0)
pwm=PWM(led)
pwm.freq(1000)

while True:
    for duty in range(65536):
        pwm.duty_u16(duty)
        time.sleep(0.0001)
    for duty in range(65536,0,-1):
        pwm.duty_u16(duty)
        time.sleep(0.0001)
