from time import sleep_ms, ticks_ms 
from machine import I2C, Pin 
from lcd_I2C.i2c_lcd import I2cLcd 

AddressOfLcd = 0x27
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) # connect scl to GPIO 22, sda to GPIO 21
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)

if __name__ == '__main__':
    lcd.move_to(3,0)
    lcd.putstr("Holaaa")
    lcd.move_to(0,1)
    lcd.putstr("DONDE ESTASSS")
    sleep_ms(10000)
