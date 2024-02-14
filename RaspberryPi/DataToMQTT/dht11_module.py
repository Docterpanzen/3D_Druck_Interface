# In einer Datei namens dht11_module.py
import time
import board
import adafruit_dht
import mqtt_connector

# Initialisieren Sie den DHT, wobei der Datenpin mit Pin 16
# (GPIO 23) des Raspberry Pi verbunden ist:
dhtDevice = adafruit_dht.DHT11(board.D23)

def send_mqtt(client, temperature, humidity):
    # Formatieren Sie die Nachrichten
    temp_msg = f"{temperature}"
    humid_msg = f"{humidity}"
    
    # Senden Sie die Nachrichten an den MQTT-Broker
    client.publish("topic/temperature", temp_msg)
    client.publish("topic/humidity", humid_msg)

def run_dht11_module():
    print("Running DHT11 module...")  # Diese Zeile hinzufügen
    client = mqtt_connector.create_mqtt_client()

    while True:
        try:
            # Ausgabe der Werte über die serielle Schnittstelle
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            send_mqtt(client, temperature_c, humidity)
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(10.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        time.sleep(10.0)

    # Verbindung zum MQTT-Broker trennen
    client.disconnect()
