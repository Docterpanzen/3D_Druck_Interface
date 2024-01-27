import paho.mqtt.client as paho
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Client is connected!")
        client.subscribe("test")
    else:
        print("Client is not connected!")

def on_message(client, userdata, msg):
    print("Message received: " + str(msg.payload.decode("utf-8")))


#--- variables ---
connected = False
broker_address = "158.180.44.197"
port = 1883
user = "bobm"
password = "letmein"
#-----------------


client = paho.Client("MQTT")
client.username_pw_set(username=user, password=password)
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

