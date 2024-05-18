from machine import Pin
import time

# Configuración de pines
trigger_pin = Pin(4, Pin.OUT)  # Pin para enviar la señal de activación
echo_pin = Pin(5, Pin.IN)       # Pin para recibir la señal de eco

def medir_distancia():
    # Enviar un pulso corto al pin de activación para iniciar la medición
    trigger_pin.value(0)
    time.sleep_us(2)
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)
    
    # Esperar hasta que el pin de eco se active
    while echo_pin.value() == 0:
        pulso_inicio = time.ticks_us()
    
    # Esperar hasta que el pin de eco se desactive
    while echo_pin.value() == 1:
        pulso_fin = time.ticks_us()
    
    # Calcular la duración del pulso de eco
    duracion = time.ticks_diff(pulso_fin, pulso_inicio)
    
    # Calcular la distancia en base a la duración del pulso (en microsegundos)
    # La velocidad del sonido es de aproximadamente 343 metros por segundo
    # y el pulso de eco recorre dos veces la distancia a medir
    distancia_cm = duracion / 58
    
    return distancia_cm

try:
    while True:
        distancia = medir_distancia()
        print("Distancia: {:.2f} cm".format(distancia))
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma detenido.")
