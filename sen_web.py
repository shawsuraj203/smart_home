import time
import requests
from main import create_data_entry
import sens_db
URL = "http://192.168.0.129:8000/data/"
post_curser = 0

def post_sensor_data():
    global post_curser
    table_row_count = sens_db.get_table_row_count()
    while True:
        while post_curser < table_row_count:
            try:
                sens_data = sens_db.read_row_by_index(post_curser)
                post_data = create_data_entry(sens_data[1], sens_data[3], sens_data[4], sens_data[2])
                print("Data to be sent:", post_data)
                response = requests.post(URL, json=post_data)
                post_curser += 1
                if response.status_code == 200:
                    print("Data sent successfully!")
                    print("Server response:", response.json())
                else:
                    print("Server returned an error:", response.status_code)
            except requests.exceptions.RequestException as e:
                print("Request failed:", e)
        print("Waiting for new data...")
        time.sleep(60)