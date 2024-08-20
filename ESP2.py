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
from machine import Pin
from umqtt.simple import MQTTClient

# MQTT Server Parameters
MQTT_CLIENT_ID = "icaro"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC1    = "PontoH"
MQTT_TOPIC2    = "PontoBe"


led = Pin(18, Pin.OUT)

# Função de callback para recebimento de mensagens MQTT
def callback(topic, msg):
    #print("Mensagem recebida: ", msg.decode())
    global status
    if((str(msg.decode()) == "HAlta")):
        hum = True
    elif(str((msg.decode()) == "HNormal")):
        hum = False



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
#Lembrem-se sempre é necessário ter um callback para receber informações.
client.set_callback(callback)
client.connect()
client.subscribe(MQTT_TOPIC1)
print("Connected!")

teste = False


status = 0
while True:
    client.check_msg()
    time.sleep(1)
    if hum and not teste:
        
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)











