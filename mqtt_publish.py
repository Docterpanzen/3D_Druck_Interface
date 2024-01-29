import streamlit as st
import paho.mqtt.client as paho
from paho import mqtt
import time

#---------- settings ----------
client = paho.Client("MQTT")
broker_address = "d8b3f3da52c749dc9ca162ec9439e398.s2.eu.hivemq.cloud"
port = 8883
user = "Docterpanzen"
password = "Start.123"
client.username_pw_set(username=user, password=password)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.connect(broker_address, port=port)
#------------------------------





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
    





