from machine import Pin
from time import sleep


key_down = const(1)
key_up = const(0)

keys = [
            ["1","2","3","A"],
            ["4","5","6","B"],
            ["7","8","9","C"],
            ["*","0","#","D"],
          ]

rows = [2,4,5,19]
cols = [15,27,26,25]

pin_rows = [Pin(pin_name, mode=Pin.OUT) for pin_name in rows]
pin_cols = [Pin(pin_name, mode =Pin.IN, pull=Pin.PULL_DOWN) for pin_name in cols]



def init():
    for row in range(0,4):
        for col in range(0,4):
            pin_rows[row].value(0)

def scan(row, col):
    pin_rows[row].value(1)
    key = None
    
    if pin_cols[col].value() == key_down:
        key = key_down
    if pin_cols[col].value() == key_up:
        key = key_up
        
    return key

print("Presiona una tecla: ")

init()

while True:
    for row in range(4):
        for col in range(4):
            key = scan(row, col)
            if key == key_down:
                print("Tecla:",keys[row][col])
                sleep(0.5)

        
    