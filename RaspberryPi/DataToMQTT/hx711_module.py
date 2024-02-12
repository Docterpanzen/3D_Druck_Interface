# In einer Datei namens hx711_module.py
import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711
import mqtt_connector

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)

def send_mqtt(client, weight):
    # Formatieren Sie die Nachricht
    msg = f"Weight: {weight} g"
    # Senden Sie die Nachricht an den MQTT-Broker
    client.publish("Weight", msg)

def run_hx711_module():
    client = mqtt_connector.create_mqtt_client()

    while True:
        try:
            # Ausgabe der Werte über die serielle Schnittstelle
            weight = hx.get_weight(1)
            send_mqtt(client, weight)
            time.sleep(10)
        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()

    # Verbindung zum MQTT-Broker trennen
    client.disconnect()
