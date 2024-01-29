import streamlit as st
import sqlite3
import pandas as pd



# Funktion zum Datenbank verbinden und verbindung trennen
def connect_to_database():
    conn = sqlite3.connect('Data_3D_printer.db')
    cur = conn.cursor()
    return conn, cur

def close_database_connection(conn):
    conn.close()


# Funktion zum Daten holen aus der Datenbank
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

    with st.sidebar:
        add_selectbox = st.selectbox("Optionen", ("Temperatur", "Beschleunigung", "Feuchtigkeit"))

        if add_selectbox == "Temperatur":
            with st.form("My form"):
                st.write("Wähle Daten aus: ")
                # Zeitbereich für Werte
                start_date = st.date_input("Start Date", pd.to_datetime('today') - pd.DateOffset(days=7))
                start_time = st.time_input("Start Time", pd.Timestamp('00:00:00').time())
                start_datetime = pd.to_datetime(str(start_date) + ' ' + str(start_time))

                end_date = st.date_input("End Date", pd.to_datetime('today'))
                end_time = st.time_input("End Time", pd.Timestamp('23:59:59').time())
                end_datetime = pd.to_datetime(str(end_date) + ' ' + str(end_time))
                submitted_button_temperatur = st.form_submit_button("Ausführen!")
                if submitted_button_temperatur:
                    st.success("Daten werden geladen")

        if add_selectbox == "Beschleunigung":
            with st.form("My form"):
                st.write("Wähle Daten aus: ")
                # Zeitbereich für Werte
                start_date = st.date_input("Start Date", pd.to_datetime('today') - pd.DateOffset(days=7))
                start_time = st.time_input("Start Time", pd.Timestamp('00:00:00').time())
                start_datetime = pd.to_datetime(str(start_date) + ' ' + str(start_time))

                end_date = st.date_input("End Date", pd.to_datetime('today'))
                end_time = st.time_input("End Time", pd.Timestamp('23:59:59').time())
                end_datetime = pd.to_datetime(str(end_date) + ' ' + str(end_time))
                submitted_button_acceleration = st.form_submit_button("Ausführen!")
                if submitted_button_acceleration:
                    st.success("Daten werden geladen")       
                
        if add_selectbox == "Feuchtigkeit":
            with st.form("My form"):
                st.write("Wähle Daten aus: ")
                # Zeitbereich für Werte
                start_date = st.date_input("Start Date", pd.to_datetime('today') - pd.DateOffset(days=7))
                start_time = st.time_input("Start Time", pd.Timestamp('00:00:00').time())
                start_datetime = pd.to_datetime(str(start_date) + ' ' + str(start_time))

                end_date = st.date_input("End Date", pd.to_datetime('today'))
                end_time = st.time_input("End Time", pd.Timestamp('23:59:59').time())
                end_datetime = pd.to_datetime(str(end_date) + ' ' + str(end_time))
                submitted_button_humidity = st.form_submit_button("Ausführen!")
                if submitted_button_humidity:
                    st.success("Daten werden geladen")  

    if add_selectbox == "Temperatur":
        if submitted_button_temperatur:
            # Werte von Datenbank für ausgewählten Zeitraum
            data = get_data_temperature(start_datetime, end_datetime)

            # Erstelle panda dataframe
            df = pd.DataFrame(data, columns=['timestamp', 'temperature'])
            st.dataframe(df)
            print(df)

            # Aktueller Wert live anzeigen
            #latest_value = df.iloc[-1]['temperature'] if not df.empty else None
            #st.text(f"Aktueller Wert: {latest_value}")

            # Plot der Daten
            st.area_chart(df.set_index('timestamp').rename(columns={'temperature': 'Temperatur'}))

    elif add_selectbox == "Beschleunigung":
        if submitted_button_acceleration:
            data = get_data_acceleration(start_datetime, end_datetime)

            # Erstelle panda dataframe
            df1 = pd.DataFrame(data, columns=['timestamp', 'acceleration_x', 'acceleration_y', 'acceleration_z'])
            st.dataframe(df1)
            print(df1)

            # Plot der Daten
            st.line_chart(df1.set_index('timestamp').rename(columns={   'acceleration_x': 'Beschleunigung X',
                                                                        'acceleration_y': 'Beschleunigung Y',
                                                                        'acceleration_z': 'Beschleunigung Z'}))
            

    elif add_selectbox == "Feuchtigkeit":
        if submitted_button_humidity:
            data = get_data_humidity(start_datetime, end_datetime)

            # Erstelle panda dataframe
            df2 = pd.DataFrame(data, columns=['timestamp', 'humidity'])
            st.dataframe(df2)
            print(df2)

            # Plot der Daten
            st.line_chart(df2.set_index('timestamp').rename(columns={'humidity': 'Feuchtigkeit'}))





if __name__ == "__main__":
    main()