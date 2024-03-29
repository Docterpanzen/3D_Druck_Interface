import streamlit as st
import sqlite3
import pandas as pd
from PIL import Image
import io



# Funktion zum Datenbank verbinden und verbindung trennen
def connect_to_database():
    conn = sqlite3.connect('Data_3D_printer.db')
    cur = conn.cursor()
    return conn, cur

def close_database_connection(conn):
    conn.close()


# Funktion zum holen der Daten aus der Datenbank
def get_data_temperature(start_datetime, end_datetime):
    conn, cur = connect_to_database()
    start_datetime_str = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
    end_datetime_str = end_datetime.strftime('%Y-%m-%d %H:%M:%S')
    
    query = "SELECT timestamp, temperature FROM temperature_data WHERE timestamp BETWEEN ? AND ?"
    cur.execute(query, (start_datetime_str, end_datetime_str))
    rows = cur.fetchall()
    close_database_connection(conn)
    return rows

def get_data_humidity(start_datetime, end_datetime):
    conn, cur = connect_to_database()
    start_datetime_str = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
    end_datetime_str = end_datetime.strftime('%Y-%m-%d %H:%M:%S')
    
    query = "SELECT timestamp, humidity FROM humidity_data WHERE timestamp BETWEEN ? AND ?"
    cur.execute(query, (start_datetime_str, end_datetime_str))
    rows = cur.fetchall()
    close_database_connection(conn)
    return rows

def get_data_acceleration(start_datetime, end_datetime):
    conn, cur = connect_to_database()
    start_datetime_str = start_datetime.strftime('%Y-%m-%d %H:%M:%S')
    end_datetime_str = end_datetime.strftime('%Y-%m-%d %H:%M:%S')
    
    query = "SELECT timestamp, acceleration_x, acceleration_y, acceleration_z FROM acceleration_data WHERE timestamp BETWEEN ? AND ?"
    cur.execute(query, (start_datetime_str, end_datetime_str))
    rows = cur.fetchall()
    close_database_connection(conn)
    return rows

def get_data_camera():
    conn, cur = connect_to_database()
    query = "SELECT timestamp, camera_byte_data FROM camera_data ORDER BY timestamp DESC LIMIT 1"
    cur.execute(query)
    row = cur.fetchone()
    close_database_connection(conn)
    return row

def get_average_weight_data():
    conn, cur = connect_to_database()
    query = "SELECT weight FROM weight_data ORDER BY timestamp DESC LIMIT 3"
    cur.execute(query)
    rows = cur.fetchall()
    close_database_connection(conn)
    if rows:
        total_weight = sum(row[0] for row in rows)
        average_weight = total_weight / len(rows)
        return average_weight
    else:
        return None


#----- Funktion um Gewicht aus G-Code zu bekommen
def extract_filament_used(file_content):
    try:
        lines = file_content.decode('utf-8').splitlines()
    except UnicodeDecodeError:
        st.error("Fehler beim Dekodieren der Dateiinhalte. Überprüfe das Dateiformat.")
        return None

    for line in lines:
        if '; filament used [g] =' in line:
            try:
                return float(line.split('=')[1].strip())
            except (IndexError, ValueError):
                st.error("Fehler beim Extrahieren des Filamentgewichts. Überprüfe das Dateiformat.")
                return None
    st.warning("Filamentgewicht nicht gefunden. Überprüfe das Dateiformat.")
    return None

def main():
    st.title("3D-Drucker Überwachung")

    tab1, tab2 = st.tabs(["Druckerdaten", "Druckinformationen"])

    with tab1:

        with st.sidebar:
            with st.form("Form Zeitauswahl"):
                st.header("Wähle Daten aus: ")
                date = st.date_input("Tag", pd.to_datetime('today') - pd.DateOffset(days=7))        # Tag für Zeitbereich
                start_time = st.time_input("Start Time", pd.Timestamp('00:00:00').time())           # Startzeit (Uhrzeit)
                start_datetime = pd.to_datetime(str(date) + ' ' + str(start_time))                  # Erstelle Startdatum + Startuhrzeit
                end_time = st.time_input("End Time", pd.Timestamp('23:59:59').time())               # Endzeit (Uhrzeit)
                end_datetime = pd.to_datetime(str(date) + ' ' + str(end_time))                      # Erstelle Enddatum + Enduhrzeit
                submitted_button = st.form_submit_button("Ausführen")
                if submitted_button:
                    st.success("Daten werden geladen")

                


        if submitted_button:

            st.header("")

            st.header("Temperatur")
            data = get_data_temperature(start_datetime, end_datetime)                                   # Hole Werte aus Datenbank für Zeitbereich
            st.write("Datum: ",date)
            df = pd.DataFrame(data, columns=['timestamp', 'temperature'])                               # Erstelle Panda Dataframe
            st.area_chart(df.set_index('timestamp').rename(columns={'temperature': 'Temperatur'}), width=12)      # Plot der daten

            st.divider()

            st.header("Feuchtigkeit")
            data = get_data_humidity(start_datetime, end_datetime)
            st.write("Datum: ",date)
            df2 = pd.DataFrame(data, columns=['timestamp', 'humidity'])
            st.line_chart(df2.set_index('timestamp').rename(columns={'humidity': 'Feuchtigkeit'}))

            st.divider()

            st.header("Beschleunigung")
            data = get_data_acceleration(start_datetime, end_datetime)
            st.write("Datum: ",date)
            df1 = pd.DataFrame(data, columns=['timestamp', 'acceleration_x', 'acceleration_y', 'acceleration_z'])
            st.line_chart(df1.set_index('timestamp').rename(columns={   'acceleration_x': 'Beschleunigung X',
                                                                        'acceleration_y': 'Beschleunigung Y',
                                                                        'acceleration_z': 'Beschleunigung Z'}))

    with tab2:
    
        st.title("Informationen zu dem Druck")

        # Anzeigen des neuesten Bildes
        row = get_data_camera()
        if row is not None:
            timestamp, camera_byte_data = row
            image = camera_byte_data
            st.image(image, caption='Aktueller Druckerstatus', use_column_width=True)
            if st.button('Aktualisieren'):
                st.rerun()
        else:
            st.write("Es sind keine Kameradaten verfügbar.")



        st.divider()

        max_weight = 1232  # Maximales Gewicht der Filamentrolle
        
        st.header("Filamentrolle")
        average_weight = get_average_weight_data()
        average_weight = round(average_weight, 2) if average_weight is not None else None
        if average_weight is not None:
            st.text(f" Vorhandene Menge an Filament: {average_weight} g")
            progress = st.progress(0)
            progress_value = average_weight / max_weight
            progress.progress(progress_value)
        else:
            st.warning("Es sind keine Gewichtsdaten verfügbar.")

        st.divider()

        st.header("Druckvorschau")
        uploaded_file = st.file_uploader("Lade hier deinen G-Code hoch", type=["gcode"])
        filament_weight = 0

        if uploaded_file is not None:
            st.info("Datei erfolgreich hochgeladen!")

            # Button zum Ausführen der Funktion
            if st.button("Gewicht aus G-Code extrahieren"):
                file_content = uploaded_file.getvalue()
                filament_weight = extract_filament_used(file_content)
                filament_weight = round(filament_weight, 2) if filament_weight is not None else None
                st.write(f"Vorraussichtlicher Filamentverbrauch: {filament_weight} g")
                if filament_weight is not None and average_weight is not None:
                    if filament_weight < average_weight:
                        st.success("Es ist genug Filament vorhanden.")
                        st.balloons()
                    else:
                        st.error("Es ist nicht genug Filament vorhanden. Bitte benutz eine neue Filamentrolle.")
                
        else:
            st.error("Bitte lade eine Datei hoch.")

if __name__ == "__main__":
    main()