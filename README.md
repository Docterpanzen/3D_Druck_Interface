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
  - Wählen Sie den Reiter "Druckerdaten", um die aktuellen Daten des Druckers anzuzeigen.
  - Wählen Sie das gewünschte Datum und den Zeitbereich aus, für den Sie die Daten anzeigen möchten.
  - Klicken Sie auf "Ausführen & Aktualisieren", um die Daten anzuzeigen oder zu aktualisieren.

- **Druckinformationen:** Anzeigen zusätzlicher Informationen zum Druckvorgang.
  - Wechseln Sie zum Reiter "Druckinformationen", um zusätzliche Informationen zum Druckvorgang zu erhalten.
  - Ein Live-Bild aus dem Druckraum wird alle 10 Sekunden aktualisiert.
  - Geben Sie Ihren G-Code in das entsprechende Feld ein, um ihn in das benötigte Filamentgewicht umzurechnen.
  - Vergleichen Sie das berechnete Gewicht mit dem tatsächlichen Gewicht Ihres Filaments mithilfe einer Filamentwaage.
  - Die App gibt Auskunft darüber, ob das Filament ausreicht oder ob Sie die Filamentspule erneuern sollten.

## Hinweis

Stellen Sie sicher, dass der MQTT-Abonnent im Hintergrund läuft, um kontinuierlich Daten zu speichern.
