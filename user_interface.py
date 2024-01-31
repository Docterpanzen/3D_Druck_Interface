import streamlit as st
import sqlite3
import pandas as pd
from io import StringIO



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




def main():
    st.title("3D-Drucker Überwachung")

    tab1, tab2 = st.tabs(["Druckerdaten", "Druck Informationen"])

    with tab1:

        with st.sidebar:
            with st.form("Form Zeitauswahl"):
                st.header("Wähle Daten aus: ")
                date = st.date_input("Tag", pd.to_datetime('today') - pd.DateOffset(days=7))        # Tag für Zeitbereich
                start_time = st.time_input("Start Time", pd.Timestamp('00:00:00').time())           # Startzeit (Uhrzeit)
                start_datetime = pd.to_datetime(str(date) + ' ' + str(start_time))                  # Erstelle Startdatum + Startuhrzeit
                end_time = st.time_input("End Time", pd.Timestamp('23:59:59').time())               # Endzeit (Uhrzeit)
                end_datetime = pd.to_datetime(str(date) + ' ' + str(end_time))                      # Erstelle Enddatum + Enduhrzeit
                submitted_button = st.form_submit_button("Ausführen!")
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
        st.balloons()
        st.title("Informationen zu dem Druck!")
        file = st.file_uploader("Suche File aus")

        if file is not None:
            stringio = StringIO(file.getvalue().decode("utf-8"))

            file_data = stringio.read()
            st.write(file_data)



if __name__ == "__main__":
    main()