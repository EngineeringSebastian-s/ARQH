import network
import time

def wifi_scan():
    wlan = network.WLAN(network.STA_IF)  # Crea una instancia de la interfaz WLAN en modo estación.
    wlan.active(True)  # Activa la interfaz WLAN.
    
    print("Scanning for Wi-Fi networks...")
    networks = wlan.scan()  # Escanea las redes Wi-Fi disponibles.

    for net in networks:
        ssid = net[0].decode('utf-8')  # Nombre de la red.
        bssid = net[1]  # Dirección MAC del punto de acceso.
        channel = net[2]  # Canal de Wi-Fi.
        RSSI = net[3]  # Intensidad de la señal.
        authmode = net[4]  # Modo de autenticación (ej., WEP, WPA, WPA2).
        hidden = net[5]  # Red oculta o no.
        
        print("SSID:", ssid)
        print("BSSID:", bssid)
        print("Canal:", channel)
        print("RSSI:", RSSI)
        print("Modo de Autenticación:", authmode)
        print("Es red oculta:", "Sí" if hidden else "No")
        print()

def main():
    while True:
        wifi_scan()
        print("Waiting 10 seconds for next scan...")
        time.sleep(10)

if __name__ == "__main__":
    main()
