# SQLite Database for Sensor Data

This document provides an overview of the Python code used to manage a SQLite database for storing sensor data. The database is designed to store information such as device ID, timestamp, power, and current readings.

## Database Configuration

The database file is named `sensor_data.db`. The table `SensorData` is created with the following schema:

- `id`: An auto-incrementing primary key.
- `deviceid`: A string representing the device ID.
- `timestamp`: A string representing the timestamp of the data.
- `power`: A real number representing the power reading.
- `current`: A real number representing the current reading.

### Code Overview

#### 1. Setting Up the Database

The `setup_database` function initializes the database connection and ensures the `SensorData` table exists. It creates the table if it does not already exist.

#### 2. Storing Data

The `store_data` function inserts sensor data into the `SensorData` table. It handles database errors and ensures data integrity.

#### 3. Counting Rows

The `get_table_row_count` function retrieves the total number of rows in the `SensorData` table. It is useful for determining the size of the dataset.

#### 4. Reading a Row by Index

The `read_row_by_index` function retrieves a specific row from the `SensorData` table based on its index. It validates the index to ensure it is within range.

### Usage

1. Call `setup_database()` to initialize the database.
2. Use `store_data()` to insert sensor readings.
3. Use `get_table_row_count()` to get the total number of rows.
4. Use `read_row_by_index()` to fetch a specific row by its index.

This code provides a simple yet effective way to manage sensor data using SQLite.
