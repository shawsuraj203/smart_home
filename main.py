import threading
import time

import sens_db
import sen_web
import sen_hal

DEVICE_IDS = [0]  # List of device IDs
VOLTAGE = 230  # Constant voltage for all devices (placeholder)

# Function to simulate reading sensor data based on device ID
def read_sensor_data(device_id):
    # Simulate random current values between 5 and 15 (as an example)
    current = sen_hal.read_current(device_id) 
    power = VOLTAGE * current
    return power, current

# Function to create a key-value pair (dictionary) for each data entry
def create_data_entry(deviceid, power, current, timestamp):
    return {
        "deviceid": deviceid,
        "power": power,
        "current": current,
        "timestamp": timestamp,
    }

def data_Collection(cursor, conn):
    while True:
        try:
          # Collect and store data (simulate for testing purposes)
            for device_id in DEVICE_IDS:  # Iterate through multiple devices
                power, current = read_sensor_data(device_id)  # Simulate sensor data for each device
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                data_entry = create_data_entry(device_id, power, current, timestamp)  # Create a key-value pair
                sens_db.store_data(cursor, conn, data_entry)  # Save data to database
        except KeyboardInterrupt:
            print("Stopping data collection...")
        time.sleep(1)  # Sleep for a second before collecting data again
    return 
# Main function to start data collection and allow querying
def main():
    sen_hal.adc_init()
    conn, cursor = sens_db.setup_database()
    thread1 = threading.Thread(target=data_Collection, args=(cursor, conn))
    thread2 = threading.Thread(target=sen_web.post_sensor_data) 
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    cursor.close()
    conn.close()
    return 
# Entry point of the script
if __name__ == "__main__":
    main()