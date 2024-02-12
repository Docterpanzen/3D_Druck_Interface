import os
import time
import mqtt_connector

def run_camera_module():
    client = mqtt_connector.create_mqtt_client()

    while True:
        # Aufnahme des Bildes mit einer Auflösung von 1920x1080
        os.system('libcamera-still --timeout 2000 --output output.jpg --width 1920 --height 1080')

        # Lesen des Bildes
        with open("output.jpg", "rb") as image_file:
            image = image_file.read()

        # Bild an den MQTT-Broker senden
        client.publish("image_topic", image)

        # Warten für 10 Sekunden
        time.sleep(10)

    # Verbindung zum MQTT-Broker trennen
    client.disconnect()
