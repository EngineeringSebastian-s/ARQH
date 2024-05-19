import network
import time
import ubinascii

def scan_network():
    nic = network.WLAN(network.STA_IF)
    nic.active(True)

    print("Escaneando redes WiFi disponibles...")
    networks = nic.scan()
    
    for net in networks:
        ssid = net[0].decode()
        bssid = ubinascii.hexlify(net[1]).decode()
        channel = net[2]
        RSSI = net[3]
        print("SSID: {}, BSSID: {}, Canal: {}, RSSI: {}".format(ssid, bssid, channel, RSSI))

def monitor_network():
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    
    print("Monitorizando la red, presione CTRL+C para detener...")
    while True:
        # Aquí se supone que implementas la lógica para leer paquetes
        # Esta es solo una simulación de la actividad de monitoreo
        time.sleep(5)
        print("Monitoreando actividad de red...")

try:
    scan_network()
    monitor_network()
except KeyboardInterrupt:
    print("Monitoreo detenido por el usuario.")

