import time
import sqlite3


# Initialize the database connection
DB_NAME = 'sensor_data.db'
conn = None

# Function to set up SQLite database
def setup_database():
    global conn
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    cursor = conn.cursor()     
    cursor.execute('''CREATE TABLE IF NOT EXISTS SensorData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deviceid TEXT,
        timestamp TEXT,
        power REAL,
        current REAL
    )''')
    conn.commit()
    return conn, cursor


# Function to store data in the database
def store_data(cursor, conn, data):
    try:
        cursor.execute(
            'INSERT INTO SensorData (deviceid, timestamp, power, current) VALUES (?, ?, ?, ?)',
            (data["deviceid"], data["timestamp"], data["power"], data["current"])
        )
        conn.commit()
        print(f"Data saved: {data}")
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()
    except Exception as e:
        print(f"Unexpected error: {e}")

def get_table_row_count():
    global conn
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM SensorData")
    count = cursor.fetchone()[0]
    cursor.close()
    return count


def read_row_by_index(row_index):
    """
    Reads a specific row by index from an SQLite3 database table.
    
    Parameters:
        database_path (str): Path to the SQLite3 database file.
        table_name (str): Name of the table to query.
        row_index (int): Index of the row to retrieve (0-based).
    
    Returns:
        tuple or None: The row data as a tuple, or None if the index is invalid.
    """
    global conn
    cursor = conn.cursor()
    try:
        # Connect to the database
        row_count = get_table_row_count()
        # Validate the index
        if row_index < 0 or row_index >= row_count:
            print("Index out of range.")
            cursor.close()
            return None

        # Fetch the specific row using OFFSET
        cursor.execute(f"SELECT * FROM SensorData LIMIT 1 OFFSET {row_index}")
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        cursor.close()
        return None
    cursor.close()


