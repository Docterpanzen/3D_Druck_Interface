# 3D-Drucker Überwachung

Dieses Projekt ermöglicht die Überwachung verschiedener Parameter eines 3D-Druckers in einer Umhasung mithilfe von verschiedenen Modulen. Diese Module erfassen Daten von unterschiedlichen Sensoren und übertragen sie an einen MQTT-Broker.

## Inhaltsverzeichnis
- [Hardwareliste](#hardware)
- [Module](#module)
- [Hauptprogramm](#hauptprogramm)
- [CAD-Dateien](#cad-dateien)
- [Installation](#installation)
- [Verwendung](#verwendung)

## Hardware
- **Raspberry Pi 4 Model B**

  Der Raspberry Pi ist das zentrale Bauteil dieser 3D-Drucküberwachung. Hier werden die Daten der einzelnen Sensoren und der Kamera gesammelt und an den MQTT-Broker weitergeleitet. Für die Einrichtung des Einplatinencomputers wurde der offiziellen Raspberry Pi Dokumentation unter folgendem Link gefolgt: [Raspberry Pi Dokumentation](https://www.raspberrypi.com/documentation/)

- **Raspberry Pi Camera Module 3 NoIR Wide**

  Um den Druckraum visuell zu überwachen, wurde eine Kamera in der Umhausung eingebaut. Mehrere Teile zur Befestigung im Inneren des Gehäuses sind wurden hierfür im 3D-Drucker gefertigt. Für die Einrichtung der Kamera wurde ebenfalls der offiziellen Raspberry Pi Dokumentation unter folgendem Link gefolgt: [Raspberry Pi Kamera Dokumentation](https://www.raspberrypi.com/documentation/accessories/camera.html)

- **DHT11**

  Der DHT11-Sensor liest Temperatur- und Feuchtigkeitsdaten im Druckraum und sendet sie an den Raspberry Pi, welcher sie dann an den MQTT-Broker weiterleitet. Die Temperaturdaten werden unter dem Topic "topic/temperature" und die Feuchtigkeitsdaten unter dem Topic "topic/humidity" gesendet. Weitere Informationen finden Sie im [Datenblatt des DHT11-Sensors](https://cdn-reichelt.de/documents/datenblatt/A300/SEN-KY015TF_ANLEITUNG_2023-08-24.pdf).

- **HX711 + Wägezelle**

  Der HX711-Sensor liest Gewichtsdaten von einer Wägezelle, die im Spulenhalter des Gehäuses verbaut ist, und gibt diese an den Raspberry Pi weiter. Dieser sendet sie an den MQTT-Broker. Die Daten werden unter dem Topic "topic/weight" gesendet. Eine Anleitung zur Einrichtung finden Sie in [diesem PDF](https://joy-it.net/files/files/Produkte/SEN-HX711-01/SEN-HX711_Anleitung_2023-09-15.pdf). Es ist wichtig, dass die Bibliothek im gleichen Ordner wie das Hauptprogramm und die Module gespeichert ist.

- **ADXL345**

  Der ADXL435 ist ein Beschleunigungssensor, der Beschleunigungsdaten der Gehäuses aufzeichnet und an den Raspberry Pi weitergibt, der diese dann an den MQTT-Broker weitergibt. Die Daten werden unter dem Topic "topic/acceleration" gesendet. Eine Anleitung zur Einrichtung finden Sie auf [dieser Website](https://pimylifeup.com/raspberry-pi-accelerometer-adxl345/).

## Module

Das Projekt besteht aus den folgenden Modulen:

- **adxl345_module.py**

  Dieses Modul liest Beschleunigungsdaten von einem ADXL345-Sensor und sendet sie an den MQTT-Broker.

- **camera_module.py**

  Dieses Modul nimmt Bilder mit einer Auflösung von 1920x1080 auf und sendet sie an den MQTT-Broker.

- **dht11_module.py**

  Dieses Modul liest Temperatur- und Feuchtigkeitsdaten von einem DHT11-Sensor und sendet sie an den MQTT-Broker.

- **hx711_module.py**

  Dieses Modul liest Gewichtsdaten von einer Wägezelle mit dem HX711-Sensor und sendet sie an den MQTT-Broker.

- **mqtt_connector.py**

  Dieses Modul stellt eine Verbindung zu einem MQTT-Broker her und ermöglicht das Senden von Nachrichten.

## Hauptprogramm

Das Hauptprogramm (`data_to_mqtt.py`) führt alle Module aus und sammelt Daten von allen Sensoren.

## CAD-Dateien

Die CAD-Dateien für die 3D-gedruckten Teile befinden sich im Ordner "CAD". Hier sind verschiedene CAD-Dateien für die Filamentwaage und die Kamerahalterung hinterlegt.

## Installation

Um dieses Projekt zu verwenden, klonen Sie das Repository und installieren Sie die erforderlichen Abhängigkeiten. Aktualisieren Sie außerdem die MQTT-Broker-Anmeldeinformationen in der Datei `mqtt_connector.py`.

## Verwendung

Führen Sie das Hauptprogramm aus, um Daten von allen Sensoren zu sammeln und an den MQTT-Broker zu senden:

```bash
python3 data_to_mqtt.py
