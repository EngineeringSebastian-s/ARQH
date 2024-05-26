import machine
import dht
import time

# Configura el pin al que está conectado el DHT11
sensor = dht.DHT11(machine.Pin(0))  # G0 corresponde al Pin 0 en el ESP32

def read_sensor():
    try:
        sensor.measure()  # Toma una medición del sensor DHT11
        temp = sensor.temperature()  # Obtiene la temperatura en grados Celsius
        hum = sensor.humidity()  # Obtiene la humedad relativa en porcentaje
        print("Temperatura: {}°C Humedad: {}%".format(temp, hum))
    except OSError as e:
        print("Error al leer del sensor DHT11:", e)

while True:
    read_sensor()
    time.sleep(2)  # Espera 2 segundos antes de la próxima lectura
