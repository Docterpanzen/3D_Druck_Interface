import streamlit as st
import paho.mqtt.client as paho
from paho import mqtt
import time

#---------- settings ----------
#client = paho.Client(client_id="IoT Test", userdata=None, protocol=paho.MQTTv5)
#client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
#client.username_pw_set("Docterpanzen", "Start.123")
#client.connect("d8b3f3da52c749dc9ca162ec9439e398.s2.eu.hivemq.cloud", 8883)
#------------------------------

client = paho.Client("MQTT")
broker_address = "158.180.44.197"
port = 1883
user = "bobm"
password = "letmein"
client.username_pw_set(username=user, password=password)
client.connect(broker_address, port=port)



#---------- Testlauf publishing ----------
msg_count = 1
while True:
    time.sleep(1)
    topic = "test/publish"
    msg = f"message: {msg_count}"
    result = client.publish(topic, msg, qos=1)
    status = result[0]

    if status == 0:
        print(f"{msg} succesfully sent to topic: {topic}")
    else:
        print(f"Failed to send message to the topic {topic}")

    msg_count += 1

    if msg_count > 100:
        break
#------------------------------------------
    





