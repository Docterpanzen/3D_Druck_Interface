import paho.mqtt.client as paho
import time
import database_connection as dc

# ----- MQTT functions -----
def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        print("Client is connected!")
        client.subscribe("topic/temperature")
        client.subscribe("topic/acceleration")
        client.subscribe("topic/humidity")
        client.subscribe("topic/weight")
        client.subscribe("image_topic")
        connected = True
    else:
        print("Client is not connected!")

def on_message(client, userdata, msg):
    try:
        if msg.topic == "topic/temperature":
            received_message = float(msg.payload.decode("utf-8"))
            print(f"Temperature Message received: {received_message}")
            dc.save_temperature_to_database(received_message)
        elif msg.topic == "topic/acceleration":
            acceleration_data = [float(x) for x in msg.payload.decode("utf-8").split()]
            print(f"Acceleration Message received: {acceleration_data}")
            dc.save_acceleration_to_database(acceleration_data)
        elif msg.topic == "topic/humidity":
            humidity_data = float(msg.payload.decode("utf-8"))
            print(f"Humidity Message received: {humidity_data}")
            dc.save_humidity_to_database(humidity_data)
        elif msg.topic == "image_topic":
            raw_camera_data = msg.payload
            dc.save_camera_to_database(raw_camera_data)
        elif msg.topic == "topic/weight":
            weight_data = float(msg.payload.decode("utf-8"))
            print(f"Weight Message received: {weight_data}")
            dc.save_weight_to_database(weight_data)
    except ValueError:
        print("Failed to convert the message to a numeric format.")



# ---- MQTT Einstellungen ----
connected = False
client = paho.Client("MQTT")
broker_address = "d8b3f3da52c749dc9ca162ec9439e398.s2.eu.hivemq.cloud"
port = 8883
user = "Docterpanzen"
password = "Start.123"
client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)
client.username_pw_set(username=user, password=password)
# ----------------------------


client.on_connect = on_connect          # Schreibe Funktion welche ausgeführt werden soll wenn Verbindung hergestellt ist
client.on_message = on_message          # Schreibe Funktion welche ausgeführt werden soll wenn eine Nachricht kommt


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
