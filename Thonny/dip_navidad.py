from machine import Pin
from time import sleep
A1led = Pin(22, Pin.OUT)
A0led = Pin(23, Pin.OUT)
B1led = Pin(0, Pin.OUT)
B0led = Pin(2, Pin.OUT)

A1button = Pin(26, Pin.IN)
A0button = Pin(27, Pin.IN)
B1button = Pin(32, Pin.IN)
B0button = Pin(33, Pin.IN)

def reset():
    A1led.value(0)
    A0led.value(0)
    B1led.value(0)
    B0led.value(0)

while True:
    if B1button.value():
        B1led.value(1)
        sleep (0.3)
        B0led.value(1)
        sleep (0.3)
        A1led.value(1)
        sleep (0.3)
        A0led.value(1)
        
        sleep (0.5)
        
        A0led.value(0)
        sleep (0.3)
        A1led.value(0)
        sleep(0.3)
        B0led.value(0)
        sleep(0.3)
        B1led.value(0)
        sleep (0.5)
    else:
        reset()
