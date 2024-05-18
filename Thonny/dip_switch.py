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

while True:
    A1led.value(A1button.value())
    A0led.value(A0button.value())
    B1led.value(B1button.value())
    B0led.value(B0button.value())
    sleep (0.1)
