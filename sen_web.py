import time
import requests
import logging
import sens_db
from  logger import setup_logger, log_message, get_logger
 
URL = "http://192.168.0.129:8000/data/"
MAX_DEVICE = 1
VOLTAGE = 230
post_curser = 0

log = None
def post_sensor_data():
    global post_curser
    global log
    temp_data = []
    log = get_logger()
    while True:
        table_row_count = sens_db.get_table_row_count()
        log_message(log, "Number of new data available: {0}".format(table_row_count - post_curser), level=logging.INFO)
        temp_data = []
        for device in range(MAX_DEVICE):
            temp_data.append([])
        while post_curser < table_row_count:
            sens_data = sens_db.read_row_by_index(post_curser)
            if int(sens_data[1]) < MAX_DEVICE:
                temp_data[int(sens_data[1])].append(float(sens_data[4]))
            post_curser += 1
        for device in range(MAX_DEVICE):
            try:
                if len(temp_data[device]) == 0:
                    log_message(log,"No data available for device {0}".format(device), level=logging.INFO)
                    continue
                current = max(temp_data[device])
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                post_data = create_data_entry(device, round((current * VOLTAGE),3), round(current,3), timestamp)
                log_message(log,"Data to be sent: {0}".format( post_data), level=logging.DEBUG)
                response = requests.post(URL, json=post_data)
                if response.status_code == 200:
                    log_message(log,"Data sent successfully!", level=logging.DEBUG)
                else:
                    log_message(log,"Server returned an error: {0}".format(response.status_code), level=logging.WARNING)
                    log_message(log,"Retrying...", level=logging.INFO)
                    try:
                        response = requests.post(URL, json=post_data)
                        log_message(log,"Server Response for retry: {0}".format(response.status_code), level=logging.WARNING)
                    except:
                        log_message(log,"Retry failed", level=logging.ERROR)
            except requests.exceptions.RequestException as e:
                log_message(log,"Request failed: {0}".format(e), level=logging.ERROR)
        log_message(log,"Waiting for new data...", level=logging.INFO)
        time.sleep(60)  # Sleep for 15 minutes before checking for new data
    return  # End of the function

# Function to create a key-value pair (dictionary) for each data entry
def create_data_entry(deviceid, power, current, timestamp):
    return {
        "deviceid": deviceid,
        "power": power,
        "current": current,
        "timestamp": timestamp,
    }

    