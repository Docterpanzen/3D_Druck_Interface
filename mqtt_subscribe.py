import paho.mqtt.client as paho
import time
from paho import mqtt

#----- functions -----
def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        print("Client is connected!")
        client.subscribe("topic/*")
        connected = True
    else:
        print("Client is not connected!")

def on_message(client, userdata, msg):
    print("Message received: " + str(msg.payload.decode("utf-8")))

#---------------------

connected = False

#---------- settings ----------
client = paho.Client("MQTT")
broker_address = "d8b3f3da52c749dc9ca162ec9439e398.s2.eu.hivemq.cloud"
port = 8883
user = "Docterpanzen"
password = "Start.123"
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username=user, password=password)
#------------------------------

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port=port)
client.loop_start()

while not connected:
    time.sleep(1)
    print("Connected to MQTT Broker. Waiting for messages...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Disconnecting...")
    client.disconnect()
    client.loop_stop()
    print("Disconnected.")
