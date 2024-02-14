# In einer Datei namens adxl345_module.py
import time
import board
import busio
import adafruit_adxl34x
import mqtt_connector

i2c = busio.I2C(board.SCL, board.SDA)

# Initialisieren Sie den ADXL345-Sensor
accelerometer = adafruit_adxl34x.ADXL345(i2c)

def send_mqtt(client, acceleration):
    # Formatieren Sie die Nachricht
    acc_msg = ' '.join(map(str, acceleration))
    
    # Senden Sie die Nachricht an den MQTT-Broker
    client.publish("topic/acceleration", acc_msg)

def run_adxl345_module():
    client = mqtt_connector.create_mqtt_client()

    while True:
        # Ausgabe der Werte über die serielle Schnittstelle
        acceleration = accelerometer.acceleration
        send_mqtt(client, acceleration)
        time.sleep(10)

    # Verbindung zum MQTT-Broker trennen
    client.disconnect()
