from machine import Pin
from time import sleep

pin = Pin(25, Pin.OUT)

while True:
    pin.value(1)
    sleep(10)