import network
import time
from machine import Pin
import dht
import ujson
import _thread
from umqtt.simple import MQTTClient
from servo import Servo

# MQTT Server Parameters
MQTT_CLIENT_ID = "icaro"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC1    = "PontoA"
MQTT_TOPIC2    = "PontoBe"
sensor = dht.DHT22(Pin(15))
sensor = dht.DHT22(Pin(20))

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
client.connect()

print("Connected!")

prev_weather = ""

temp1 = False
temp2 = False

def TempOne():
    lastread = ""
    global temp1
    while True:
        sensor.measure()
        temp = sensor.temperature()
        if temp != lastread:
            lastread = temp
            print("Updated!")
            client.publish(MQTT_TOPIC1, str(temp))
            if temp >= 60:
                client.publish(MQTT_TOPIC2, "Liga")
                temp1 = True
            else:
                client.publish(MQTT_TOPIC2, "Desliga")
                temp1 = False
                
                
def compOne():
    while not teste:
        if temp1:
            motor.move(50)
        else:
            motor.move(0)
            
            
def TempTwo():
    lastread = ""
    global temp2
    while True:
        sensor2.measure()
        temp = sensor2.temperature()
        if temp != lastread:
            lastread = temp
            print("Updated!")
            client.publish(MQTT_TOPIC1, str(temp))
            if temp >= 60:
                client.publish(MQTT_TOPIC2, "Liga")
                temp2 = True
            else:
                client.publish(MQTT_TOPIC2, "Desliga")
                temp2 = False
                
                
def compTwo():
    while not teste:
        if temp2:
            motor.move(180)
        else:
            motor.move(0)
                
        
        
_thread.start_new_thread(TempOne,())
_thread.start_new_thread(TempTwo,())



while True:
  print("Measuring weather conditions... ", end="")
  sensor.measure() 
  message = ujson.dumps({
    "temp": sensor.temperature(),
    "humidity": sensor.humidity(),
  })
  
  temp = sensor.temperature()
  hum = sensor.humidity()
  
  print(hum, " -> H\n", temp, " -> T")
  
  if message != prev_weather:
    print("Updated!")
    client.publish(MQTT_TOPIC1, str(temp))
    if temp > 28:
        client.publish(MQTT_TOPIC2, "Liga")
    elif temp < 29:
        client.publish(MQTT_TOPIC2, "Desliga")
    prev_weather = message
  else:
    print("No change")
  time.sleep(1)
  
  
def thread_func():
    a = 0
    b = 0
    while a==0:
        
        if chave.value() == 0:
            led.value(0)
        else:
            led.value(1)


