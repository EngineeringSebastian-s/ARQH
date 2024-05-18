import network

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # Crea una instancia de la interfaz WLAN en modo cliente (STA)
    if not wlan.isconnected():  # Verifica si ya está conectado
        wlan.active(True)  # Activa la interfaz WLAN
        wlan.connect(ssid, password)  # Intenta conectar con el SSID y contraseña
        print('Conectando a la red', ssid)
        while not wlan.isconnected():
            pass  # Espera hasta que esté conectado

    print('Configuración de red (IP/netmask/gw/DNS):', wlan.ifconfig())

# Llama a la función con tus credenciales de red
connect_wifi('tu_ssid', 'tu_contraseña')
