import sqlite3
import time

def save_temperature_to_database(temperature):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO temperature_data (timestamp, temperature) VALUES (?, ?)", (timestamp, temperature))
        conn.commit()
        print("Temperature data successfully saved to database.")
    except Exception as e:
        print(f"Error saving temperature data to database: {e}")
    finally:
        conn.close()

def save_acceleration_to_database(acceleration_data):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO acceleration_data (timestamp, acceleration_x, acceleration_y, acceleration_z) VALUES (?, ?, ?, ?)",
                    (timestamp, acceleration_data[0], acceleration_data[1], acceleration_data[2]))
        conn.commit()
        print("Acceleration data successfully saved to database.")
    except Exception as e:
        print(f"Error saving acceleration data to database: {e}")
    finally:
        conn.close()

def save_humidity_to_database(humidity):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO humidity_data (timestamp, humidity) VALUES (?, ?)", (timestamp, humidity))
        conn.commit()
        print("Humidity data successfully saved to database.")
    except Exception as e:
        print(f"Error saving humidity data to database: {e}")
    finally:
        conn.close()

def save_camera_to_database(camera_data):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO camera_data (timestamp, camera_byte_data) VALUES (?, ?)", (timestamp, camera_data))
        conn.commit()
        print("Camera picture data successfully saved to database.")
    except Exception as e:
        print(f"Error saving camera data to database: {e}")
    finally:
        conn.close()

def save_weight_to_database(weight):
    try:
        conn = sqlite3.connect('Data_3D_printer.db')
        cur = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO weight_data (timestamp, weight) VALUES (?, ?)", (timestamp, weight))
        conn.commit()
        print("Weight data successfully saved to database.")
    except Exception as e:
        print(f"Error saving weight data to database: {e}")
    finally:
        conn.close()
