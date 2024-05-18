from machine import Pin
import time

# Define los pines GPIO conectados al LCD
PIN_RS = 4
PIN_RW = 5
PIN_E = 6
PIN_D0 = 12
PIN_D1 = 13
PIN_D2 = 14
PIN_D3 = 15
PIN_D4 = 16
PIN_D5 = 17
PIN_D6 = 18
PIN_D7 = 19

# Inicializa los pines GPIO como pines de salida
pin_rs = Pin(PIN_RS, Pin.OUT)
pin_rw = Pin(PIN_RW, Pin.OUT)
pin_e = Pin(PIN_E, Pin.OUT)
pin_d0 = Pin(PIN_D0, Pin.OUT)
pin_d1 = Pin(PIN_D1, Pin.OUT)
pin_d2 = Pin(PIN_D2, Pin.OUT)
pin_d3 = Pin(PIN_D3, Pin.OUT)
pin_d4 = Pin(PIN_D4, Pin.OUT)
pin_d5 = Pin(PIN_D5, Pin.OUT)
pin_d6 = Pin(PIN_D6, Pin.OUT)
pin_d7 = Pin(PIN_D7, Pin.OUT)

# Función para enviar un comando al LCD
def lcd_command(cmd):
    pin_rs.value(0)  # Configura el pin RS como LOW para indicar un comando
    pin_rw.value(0)  # Configura el pin RW como LOW para escritura
    pin_d0.value(cmd & 0x01)
    pin_d1.value((cmd >> 1) & 0x01)
    pin_d2.value((cmd >> 2) & 0x01)
    pin_d3.value((cmd >> 3) & 0x01)
    pin_d4.value((cmd >> 4) & 0x01)
    pin_d5.value((cmd >> 5) & 0x01)
    pin_d6.value((cmd >> 6) & 0x01)
    pin_d7.value((cmd >> 7) & 0x01)
    pulse_enable()

# Función para enviar un carácter al LCD
def lcd_data(data):
    pin_rs.value(1)  # Configura el pin RS como HIGH para indicar datos
    pin_rw.value(0)  # Configura el pin RW como LOW para escritura
    pin_d0.value(data & 0x01)
    pin_d1.value((data >> 1) & 0x01)
    pin_d2.value((data >> 2) & 0x01)
    pin_d3.value((data >> 3) & 0x01)
    pin_d4.value((data >> 4) & 0x01)
    pin_d5.value((data >> 5) & 0x01)
    pin_d6.value((data >> 6) & 0x01)
    pin_d7.value((data >> 7) & 0x01)
    pulse_enable()

# Función para pulsar el pin Enable
def pulse_enable():
    pin_e.value(1)
    time.sleep_us(1)
    pin_e.value(0)
    time.sleep_us(100)

# Inicialización del display LCD
def lcd_init():
    lcd_command(0x38)  # Modo de 8 bits, 2 líneas, matriz de caracteres 5x7
    lcd_command(0x0C)  # Encender el LCD, desactivar el cursor y el parpadeo
    lcd_command(0x06)  # Desplazar el cursor a la derecha

# Inicialización del display LCD
lcd_init()

# Escribir un mensaje en el display LCD
lcd_data(ord("H"))
lcd_data(ord("e"))
lcd_data(ord("l"))
lcd_data(ord("l"))
lcd_data(ord("o"))
