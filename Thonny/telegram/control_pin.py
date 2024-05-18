from telegram.config import utelegram_config, wifi_config
from telegram import utelegram
import network
import utime
import machine

if __name__ == "__main__":
    # Configuración inicial de WiFi y pines
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(wifi_config['ssid'], wifi_config['password'])

    led_success = machine.Pin(0, machine.Pin.OUT)
    led_fail = machine.Pin(2, machine.Pin.OUT)

    # Definir bot aquí pero no inicializar aún
    bot = None

    # Espera activa hasta 20 segundos para conectar
    for _ in range(20):
        if sta_if.isconnected():
            led_success.value(1)
            led_fail.value(0)
            print('WiFi Connected - BOT LISTENING')
            bot = utelegram.ubot(utelegram_config['token'])
            break
        utime.sleep(1)
    else:
        led_success.value(0)
        led_fail.value(1)
        print('NOT CONNECTED - Aborting')

    if bot:
        # Funciones para manejar comandos de Telegram
        def control_pin(message):
            chat_id = message['message']['chat']['id']
            # Implementación de control de pin dependiendo del comando recibido
            pts_msj = message['message']['text'].split(' ')
            pin_x = machine.Pin(int(pts_msj[1]), machine.Pin.OUT)
            if pts_msj[2] == "on":
                pin_x.value(1)
                bot.send(chat_id, f'El pin {int(pts_msj[1])} fue encendido')
            elif pts_msj[2] == "off":
                pin_x.value(0)
                bot.send(chat_id, f'El pin {int(pts_msj[1])} fue apagado')
            elif pts_msj[2] == "invert":
                pin_x.value(not pin_x.value())
                bot.send(chat_id, f'El pin {int(pts_msj[1])} fue invertido')
            elif pts_msj[2] == "wink":
                pin_x.value(not pin_x.value())
                utime.sleep(1)
                pin_x.value(not pin_x.value())
                bot.send(chat_id, f'El pin {int(pts_msj[1])} parpadeo')
            else:
                bot.send(chat_id, f'Acción indefinida para el pin {int(pts_msj[1])}')
            

        bot.register('/pin', control_pin)
        bot.set_default_handler(lambda message: bot.send(message['message']['chat']['id'], "Command not recognized."))

        bot.listen()
    else:
        print("Bot not initialized due to connection failure.")
