# Enclosure Monitoring System

Dieses Projekt enthält mehrere Module zur Überwachung verschiedener Parameter in einem Gehäuse. Es verwendet verschiedene Sensoren, um Daten zu sammeln, und sendet diese Daten an einen MQTT-Broker.

## Module

Das Projekt besteht aus den folgenden Modulen:

### adxl345_module.py

Dieses Modul liest Beschleunigungsdaten von einem ADXL345-Sensor und sendet sie an den MQTT-Broker. Die Daten werden unter dem Topic "topic/acceleration" gesendet.

### camera_module.py

Dieses Modul nimmt Bilder mit einer Auflösung von 1920x1080 auf und sendet sie an den MQTT-Broker. Die Bilder werden unter dem Topic "image_topic" gesendet.

### dht11_module.py

Dieses Modul liest Temperatur- und Feuchtigkeitsdaten von einem DHT11-Sensor und sendet sie an den MQTT-Broker. Die Temperaturdaten werden unter dem Topic "topic/temperature" und die Feuchtigkeitsdaten unter dem Topic "topic/humidity" gesendet.

### hx711_module.py

Dieses Modul liest Gewichtsdaten von einem HX711-Sensor und sendet sie an den MQTT-Broker. Die Daten werden unter dem Topic "your_topic" gesendet.

### mqtt_connector.py

Dieses Modul stellt eine Verbindung zu einem MQTT-Broker her und stellt Funktionen zur Verfügung, um Nachrichten an den Broker zu senden.

## Hauptprogramm

Das Hauptprogramm (data_to_mqtt.py) führt alle Module aus und sammelt Daten von allen Sensoren.

## Installation

Um dieses Projekt zu verwenden, klonen Sie das Repository und installieren Sie die erforderlichen Abhängigkeiten. Sie müssen auch die MQTT-Broker-Anmeldeinformationen in der Datei mqtt_connector.py aktualisieren.

## Verwendung

Führen Sie das Hauptprogramm aus, um Daten von allen Sensoren zu sammeln und an den MQTT-Broker zu senden:

```bash
python3 data_to_mqtt.py 