# 3D-Druckerüberwachung mit Streamlit

Dieses Python-Programm ermöglicht es Ihnen, Daten von Sensoren aus einem 3D-Drucker zu empfangen und sie mit Hilfe von Streamlit anzuzeigen.

## Inhaltsverzeichnis

- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Anleitung](#anleitung)
- [Hinweis](#hinweis)

## Voraussetzungen

- Python 3
- Internetverbindung
- Powershell (für Windows-Benutzer)

## Installation

1. Klonen Sie dieses Repository:

    ```bash
    git clone https://github.com/Docterpanzen/3D_Druck_Interface
    ```

2. Wechseln Sie in das Verzeichnis:

    ```bash
    cd 3D_Druck_Interface
    ```

3. Installieren Sie die erforderlichen Pakete:

    ```bash
    pip install -r requirements.txt
    ```

## Verwendung

1. Starten Sie den MQTT-Abonnenten, um Daten von Ihrem 3D-Drucker zu empfangen:

    ```bash
    python mqtt_subscribe.py
    ```

2. Starten Sie die Streamlit-App:

    ```bash
    streamlit run user_interface.py
    ```

3. Öffnen Sie Ihren Webbrowser und gehen Sie zu [http://localhost:8501](http://localhost:8501), um die Streamlit-App anzuzeigen.

## Anleitung

Die Streamlit-App bietet zwei Hauptfunktionen:

- **Druckerdaten:** Anzeigen von aktuellen Daten wie Temperatur, Feuchtigkeit und Beschleunigung im Druckraum.
  
- **Druckinformationen:** Anzeigen eines Live-Bilds aus dem Druckraum und Umrechnen des G-Codes in das benötigte Filamentgewicht.

Bitte beachten Sie die detaillierte Bedienungsanleitung in der [Anleitung](#anleitung)-Sektion.

## Hinweis

Stellen Sie sicher, dass der MQTT-Abonnent im Hintergrund läuft, um kontinuierlich Daten zu speichern.

