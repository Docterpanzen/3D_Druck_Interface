import paho.mqtt.client as mqtt
import ssl
import time

def create_mqtt_client():
    # MQTT-Client erstellen
    client = mqtt.Client()

    # TLS-Verschlüsselung konfigurieren
    client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                tls_version=ssl.PROTOCOL_TLS, ciphers=None)
    client.tls_insecure_set(False)

    # MQTT-Broker Anmeldeinformationen setzen
    client.username_pw_set("Docterpanzen", "Start.123")

    # Verbindung zum MQTT-Broker herstellen
    while True:
        try:
            client.connect("d8b3f3da52c749dc9ca162ec9439e398.s2.eu.hivemq.cloud", 8883)
            break
        except ssl.SSLEOFError:
            print("Verbindung zum MQTT-Broker verloren, versuche erneut...")
            time.sleep(1)

    return client
