import threading
import time
import logging

import sens_db
import sen_web
import sen_hal
from  logger import setup_logger, log_message

DEVICE_IDS = [0]  # List of device IDs
VOLTAGE = 230  # Constant voltage for all devices (placeholder)
log = None
# Function to simulate reading sensor data based on device ID
def read_sensor_data(device_id):
    # Simulate random current values between 5 and 15 (as an example)
    current = sen_hal.read_current(device_id) 
    if current is None:
        return None, None  # Handle case where current reading fails
    power = VOLTAGE * current
    log_message(log, "Device ID: {0}, Power: {1:.2f} W, Current: {2:.2f} A".format(device_id, power, current), level=logging.DEBUG)
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
                if power is None or current is None:
                    continue
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                data_entry = create_data_entry(device_id, power, current, timestamp)  # Create a key-value pair
                sens_db.store_data(cursor, conn, data_entry)  # Save data to database
        except KeyboardInterrupt:
            log_message(log, "Data collection interrupted by user.", level=logging.INFO)
            break
        time.sleep(1)  # Sleep for a second before collecting data again
    return 
# Main function to start data collection and allow querying
def main():
    global log
    log = setup_logger("smart_home", "./smart_home.log", level=logging.DEBUG)
    sen_hal.adc_init()
    conn, cursor = sens_db.setup_database()
    thread1 = threading.Thread(target=data_Collection, args=(cursor, conn))
    log_message(log, "Starting data collection thread.", level=logging.INFO)
    thread2 = threading.Thread(target=sen_web.post_sensor_data) 
    log_message(log, "Starting web posting thread.", level=logging.INFO)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    log_message(log, "Data collection and web posting threads have completed.", level=logging.INFO)
    cursor.close()
    conn.close()
    return 
# Entry point of the script
if __name__ == "__main__":
    main()