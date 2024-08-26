"""
MicroPython IoT Weather Station Example for Wokwi.com

To view the data:

1. Go to http://www.hivemq.com/demos/websocket-client/
2. Click "Connect"
3. Under Subscriptions, click "Add New Topic Subscription"
4. In the Topic field, type "wokwi-weather" then click "Subscribe"

Now click on the DHT22 sensor in the simulation,
change the temperature/humidity, and you should see
the message appear on the MQTT Broker, in the "Messages" pane.

Copyright (C) 2022, Uri Shaked

https://wokwi.com/arduino/projects/322577683855704658
"""

import network
import time
import _thread
from machine import Pin
from umqtt.simple import MQTTClient

# MQTT Server Parameters
MQTT_CLIENT_ID = "esp2"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC1    = "PontoH"
MQTT_TOPIC2    = "PontoBe"

# Configurações de pinos
led = Pin(18, Pin.OUT)
buzzer = Pin(5, Pin.OUT)
slide_switch = Pin(15, Pin.IN, Pin.PULL_UP)  # Slide switch para desativar os alarmes

hum = False
alarme_ativo = False

# Função de callback para recebimento de mensagens MQTT
def callback(topic, msg):
    global hum
    if str(msg.decode()) == "HAlta":
        hum = True
    elif str(msg.decode()) == "HNormal":
        hum = False

# Função para controle do buzzer e LED com threads
def controle_alertas():
    global hum, alarme_ativo
    while True:
        if hum and not slide_switch.value():  # Slide switch desligado (valor 0)
            alarme_ativo = True
            led.on()
            buzzer.on()
            time.sleep(1)
            led.off()
            buzzer.off()
            time.sleep(1)
        else:
            led.off()
            buzzer.off()
            alarme_ativo = False
        time.sleep(0.1)

# Função principal
def main():
    print("Connecting to WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('PontoPe', 'milelinda')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.1)
    print(" Connected!")

    print("Connecting to MQTT server... ", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
    client.set_callback(callback)
    client.connect()
    client.subscribe(MQTT_TOPIC1)
    print("Connected!")

    # Inicia thread para controle de alertas
    _thread.start_new_thread(controle_alertas, ())

    while True:
        client.check_msg()
        time.sleep(1)

main()
