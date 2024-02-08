import paho.mqtt.client as paho
import time
import sqlite3
import io

# SQLite Database connection
conn = sqlite3.connect('Data_3D_printer.db')
cur = conn.cursor()

# ----- MQTT functions -----
def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        print("Client is connected!")
        client.subscribe("topic/temperature")
        client.subscribe("topic/acceleration")
        client.subscribe("topic/humidity")
        client.subscribe("topic/camera")
        connected = True
    else:
        print("Client is not connected!")

def on_message(client, userdata, msg):
    try:
        if msg.topic == "topic/temperature":
            received_message = float(msg.payload.decode("utf-8"))
            print(f"Temperature Message received: {received_message}")
            save_temperature_to_database(received_message)
        elif msg.topic == "topic/acceleration":
            acceleration_data = [float(x) for x in msg.payload.decode("utf-8").split()]
            print(f"Acceleration Message received: {acceleration_data}")
            save_acceleration_to_database(acceleration_data)
        elif msg.topic == "topic/humidity":
            humidity_data = float(msg.payload.decode("utf-8"))
            print(f"Humidity Message received: {humidity_data}")
            save_humidity_to_database(humidity_data)
        elif msg.topic == "topic/camera":
            raw_camera_data = msg.payload
            byte_camera_data = io.BytesIO(raw_camera_data)
            save_camera_to_database(byte_camera_data)
    except ValueError:
        print("Failed to convert the message to a numeric format.")

def save_camera_to_database(camera_data):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO camera_data (timestamp, camera) VALUES (?, ?)", (timestamp, camera_data))
        conn.commit()
        print("Camera picture data successfully saved to database.")
    except Exception as e:
        print(f"Error saving camera data to database: {e}")
    finally:
        conn.close()


def save_temperature_to_database(temperature):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO temperature_data (timestamp, temperature) VALUES (?, ?)", (timestamp, temperature))
        conn.commit()
        print("Temperature data successfully saved to database.")
    except Exception as e:
        print(f"Error saving temperature data to database: {e}")
    finally:
        conn.close()

def save_acceleration_to_database(acceleration_data):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO acceleration_data (timestamp, acceleration_x, acceleration_y, acceleration_z) VALUES (?, ?, ?, ?)",
                    (timestamp, acceleration_data[0], acceleration_data[1], acceleration_data[2]))
        conn.commit()
        print("Acceleration data successfully saved to database.")
    except Exception as e:
        print(f"Error saving acceleration data to database: {e}")
    finally:
        conn.close()

def save_humidity_to_database(humidity):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO humidity_data (timestamp, humidity) VALUES (?, ?)", (timestamp, humidity))
        conn.commit()
        print("Humidity data successfully saved to database.")
    except Exception as e:
        print(f"Error saving humidity data to database: {e}")
    finally:
        conn.close()


# ---- MQTT-Einstellungen ----
connected = False
client = paho.Client("MQTT")
broker_address = "d8b3f3da52c749dc9ca162ec9439e398.s2.eu.hivemq.cloud"
port = 8883
user = "Docterpanzen"
password = "Start.123"
client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)
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
