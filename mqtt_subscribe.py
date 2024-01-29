import paho.mqtt.client as paho
import time
import sqlite3

# ----- Database -----
conn = sqlite3.connect('Data_3D_printer.db')
cur = conn.cursor()
cur.execute('''
                CREATE TABLE IF NOT EXISTS temperature_data (
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP PRIMARY KEY,
                    temperature REAL NOT NULL)''')
conn.commit()
conn.close()
#-------------------


# ----- MQTT functions -----
def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        print("Client is connected!")
        client.subscribe("topic/#")
        connected = True
    else:
        print("Client is not connected!")

def on_message(client, userdata, msg):
    try:
        received_message = float(msg.payload.decode("utf-8"))
        print(f"Numeric Message received: {received_message}")
        save_to_database(received_message)
    except ValueError:
        print("Failed to convert the message to a numeric format.")

def save_to_database(message):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO temperature_data (temperature) VALUES (?)", (message,))
        conn.commit()
        print("Data successfully saved to database.")
    except Exception as e:
        print(f"Error saving to database: {e}")
    finally:
        conn.close()
#---------------------------


# ----- MQTT settings -----
connected = False

client = paho.Client("MQTT")
broker_address = "d8b3f3da52c749dc9ca162ec9439e398.s2.eu.hivemq.cloud"
port = 8883
user = "Docterpanzen"
password = "Start.123"
client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)
client.username_pw_set(username=user, password=password)
#---------------------------



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
