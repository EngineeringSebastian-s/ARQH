import network
from time import sleep

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

while True:
    ap_list = sta_if.scan()

    print("\nRedes WIFI disponibles")
    for ap in ap_list:
        ssid = ap[0].decode("utf-8")
        rssi = ap[3]
        print(f'SSID: {ssid}, potencia de señal {rssi}')
    sleep(10)
