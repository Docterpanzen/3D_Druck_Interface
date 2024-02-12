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
    # Aufteilen der Beschleunigung in X-, Y- und Z-Komponenten
    x, y, z = acceleration
    # Formatieren Sie die Nachricht
    msg = f"Acceleration: X={x} m/s^2, Y={y} m/s^2, Z={z} m/s^2"
    # Senden Sie die Nachricht an den MQTT-Broker
    client.publish("Acceleration", msg)

def run_adxl345_module():
    client = mqtt_connector.create_mqtt_client()

    while True:
        # Ausgabe der Werte über die serielle Schnittstelle
        acceleration = accelerometer.acceleration
        send_mqtt(client, acceleration)
        time.sleep(10)

    # Verbindung zum MQTT-Broker trennen
    client.disconnect()
