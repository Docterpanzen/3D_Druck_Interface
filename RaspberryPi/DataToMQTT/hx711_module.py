import time
import RPi.GPIO as GPIO
import sys
from hx711 import HX711
import mqtt_connector

# Initialisieren Sie den HX711, wobei die Datenpins mit Pin 5 und 6
# des Raspberry Pi verbunden sind:
hx = HX711(5, 6)

def send_mqtt(client, weight):
    # Formatieren Sie die Nachricht
    weight_msg = f"{weight}"
    
    # Senden Sie die Nachricht an den MQTT-Broker
    client.publish("topic/weight", weight_msg)

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

def setup():
    """
    code run once
    """
    hx.set_offset(8020039.5625)
    hx.set_scale(-487.96915584415586)

def run_hx711_module():
    print("Running HX711 module...")
    setup()
    client = mqtt_connector.create_mqtt_client()

    while True:
        try:
            val = hx.get_grams()
            val = round(val)
            send_mqtt(client, val)

            hx.power_down()
            time.sleep(.001)
            hx.power_up()

            time.sleep(10)
        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()
            continue
        except Exception as error:
            hx.power_down()
            raise error

    # Verbindung zum MQTT-Broker trennen
    client.disconnect()
