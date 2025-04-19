# `sen_web.py` - Sensor Data Web Posting

This module provides functionality to post sensor data to a remote server using HTTP requests.

---

## Constants

- **`URL`**: The URL of the remote server to which the sensor data will be posted (e.g., `http://192.168.0.129:8000/data/`).
- **`post_curser`**: A global variable to track the index of the last posted row in the database.

---

## Functions

### `post_sensor_data()`
Posts sensor data from the local SQLite database to a remote server.

#### Workflow:
1. Retrieves the total number of rows in the `SensorData` table using `sens_db.get_table_row_count()`.
2. Iterates through the rows starting from the `post_curser` index.
3. Reads each row using `sens_db.read_row_by_index(post_curser)`.
4. Converts the row data into a dictionary using the `create_data_entry` function from `main.py`.
5. Sends the data to the remote server using an HTTP POST request.
6. Handles server responses:
   - If the response status code is `200`, the data is considered successfully sent.
   - If an error occurs, it logs the error and continues to the next row.
7. Waits for new data if all rows have been processed, with a delay of 60 seconds.

#### Parameters:
- None

#### Returns:
- None

#### Example Usage:
```python
post_sensor_data()