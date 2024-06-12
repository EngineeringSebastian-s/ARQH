from telegram.config import utelegram_config, wifi_config
from telegram import utelegram
import network
import utime
import machine
from machine import I2C,ADC, Pin
from time import sleep_ms, ticks_ms 
from lcd_I2C.i2c_lcd import I2cLcd
import dht

AddressOfLcd = 0x27
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) # connect scl to GPIO 22, sda to GPIO 21
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)


if __name__ == "__main__":
    # Configuración inicial de WiFi y pines
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(wifi_config['ssid'], wifi_config['password'])

    # Definir bot aquí pero no inicializar aún
    bot = None

    # Espera activa hasta 20 segundos para conectar
    for _ in range(20):
        if sta_if.isconnected():
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
        
        def message_lcd(message):
            chat_id = message['message']['chat']['id']
            msj = message['message']['text'].replace('/message','')
            try:
                lcd.clear()
                lcd.putstr(msj)
                bot.send(chat_id, f'El mensaje "{msj}" ha sido mostrado con exito')
            except OSError or NameError or TypeError as e:
                bot.send(chat_id, f'No se ha podido enviar tu mensaje por un error {e}')
        
        def water_off(message):
            pin_water_off = machine.Pin(2, machine.Pin.OUT)
            pin_water_off.value(0)
            bot.send(chat_id, f'El mensaje "{msj}" ha sido mostrado con exito')
            
        def water_on(message):
            pin_water_on = machine.Pin(2, machine.Pin.OUT)
            pin_water_on.value(1)
            
        def led_off(message):
            pin_x = machine.Pin(15, machine.Pin.OUT)
            pin_x.value(0)
            
        def led_on(message):
            pin_x = machine.Pin(15, machine.Pin.OUT)
            pin_x.value(1)
            
        def plant(message):
            chat_id = message['message']['chat']['id']
            adc_pin = ADC(Pin(34))
            adc_pin.atten(ADC.ATTN_11DB)
            # Configuración del pin D0 como entrada digital
            d0_pin = Pin(14, Pin.IN)  # D0 conectado a GPIO2
            def interpret_moisture():
                adc_value = adc_pin.read()
                voltage = adc_value * 3.3 / 4095
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
            bot.send(chat_id, "Estado del suelo:"+interpret_moisture())
            lcd.clear()
            lcd.putstr("Estado del suelo:"+interpret_moisture())
        
        def atmosphere(message):
            chat_id = message['message']['chat']['id']
            sensor = dht.DHT11(machine.Pin(13))
            try:
                sensor.measure()  # Toma una medición del sensor DHT11
                temp = sensor.temperature()  # Obtiene la temperatura en grados Celsius
                hum = sensor.humidity()  # Obtiene la humedad relativa en porcentaje
                lcd.clear()
                lcd.putstr("Temperatura: {}°C Humedad: {}%".format(temp, hum))
                bot.send(chat_id, "Temperatura: {}°C Humedad: {}%".format(temp, hum))
            except OSError as e:
                bot.send(chat_id, f'Error al leer del sensor DHT11: {e}')

            

        bot.register('/pin', control_pin)
        bot.register('/message', message_lcd)
        bot.register('/water_on', water_on)
        bot.register('/water_off', water_off)
        bot.register('/led_on', led_on)
        bot.register('/led_off', led_off)
        bot.register('/atmosphere', atmosphere)
        bot.register('/plant', plant)
        bot.set_default_handler(lambda message: bot.send(message['message']['chat']['id'], "Command not recognized."))

        bot.listen()
    else:
        print("Bot not initialized due to connection failure.")
