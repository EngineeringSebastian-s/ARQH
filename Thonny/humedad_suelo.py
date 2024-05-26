from machine import ADC, Pin
import time

# Configuración del pin ADC para A0
adc_pin = ADC(Pin(34))  # Sustituye 34 por el pin ADC conectado a A0
adc_pin.atten(ADC.ATTN_11DB)  # Configura la atenuación para máxima escala (3.3V)

# Configuración del pin D0 como entrada digital
d0_pin = Pin(2, Pin.IN)  # D0 conectado a GPIO2

def read_voltage():
    adc_value = adc_pin.read()
    voltage = adc_value * 3.3 / 4095
    return voltage

def interpret_moisture():
    voltage = read_voltage()
    digital_status = d0_pin.value()  # Leer estado digital

    # Usar D0 para confirmar estados extremos
    if digital_status == 0:
        return f"Tierra muy húmeda con {voltage}V"
    elif digital_status == 1:
        # Interpretar la salida analógica para condiciones menos extremas
        if voltage > 2.0:
            return f"Tierra seca con {voltage}V"
        elif voltage > 1.5:
            return f"Suelo medio húmedo con {voltage}V"
        else:
            return f"Suelo húmedo con {voltage}V"
    else:
        return f"Condición incierta, revisión manual necesaria, con {voltage}V"

while True:
    moisture_status = interpret_moisture()
    print("Estado del suelo:", moisture_status)
    time.sleep(2)
