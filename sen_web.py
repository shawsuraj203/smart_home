import time
import requests
import logging
import sens_db
from  logger import setup_logger, log_message, get_logger
 
URL = "http://192.168.0.129:8000/data/"
post_curser = 0
log = None
def post_sensor_data():
    global post_curser
    global log
    log = get_logger()
    while True:
        table_row_count = sens_db.get_table_row_count()
        log_message(log, "Number of new data available: {0}".format(table_row_count - post_curser), level=logging.INFO)
        while post_curser < table_row_count:
            try:
                sens_data = sens_db.read_row_by_index(post_curser)
                post_data = create_data_entry(sens_data[1], sens_data[3], sens_data[4], sens_data[2])
                log_message(log,"Data to be sent: {0}".format( post_data), level=logging.DEBUG)
                response = requests.post(URL, json=post_data)
                if response.status_code == 200:
                    log_message(log,"Data sent successfully!", level=logging.DEBUG)
                else:
                    log_message(log,"Server returned an error: {0}".format(response.status_code), level=logging.WARNING)
                post_curser += 1
            except requests.exceptions.RequestException as e:
                log_message(log,"Request failed: {0}".format(e), level=logging.ERROR)
                post_curser += 1
        log_message(log,"Waiting for new data...", level=logging.INFO)
        time.sleep(60)
    return  # End of the function

# Function to create a key-value pair (dictionary) for each data entry
def create_data_entry(deviceid, power, current, timestamp):
    return {
        "deviceid": deviceid,
        "power": power,
        "current": current,
        "timestamp": timestamp,
    }
