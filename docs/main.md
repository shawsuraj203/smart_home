```markdown
# Smart Home Sensor Data Collection and Web Posting

This document describes the functionality of the `main.py` script, which is designed for collecting sensor data, storing it in a database, and posting it to a web interface.

## Overview

The script performs the following tasks:
1. Initializes the hardware abstraction layer (HAL) for sensor data collection.
2. Sets up a database connection for storing sensor data.
3. Spawns two threads:
  - One for collecting and storing sensor data.
  - Another for posting the data to a web interface.

## Key Components

### Constants
- `DEVICE_IDS`: A list of device IDs for which sensor data is collected.
- `VOLTAGE`: A constant voltage value used for power calculations.

### Functions
- **`read_sensor_data(device_id)`**: Simulates reading current values from a sensor and calculates power.
- **`create_data_entry(deviceid, power, current, timestamp)`**: Creates a dictionary entry for sensor data.
- **`data_Collection(cursor, conn)`**: Collects sensor data, creates data entries, and stores them in the database.
- **`main()`**: Initializes the system, starts data collection and web posting threads, and manages their lifecycle.

## Workflow

1. **Initialization**:
  - The ADC (Analog-to-Digital Converter) is initialized using `sen_hal.adc_init()`.
  - A database connection is established using `sens_db.setup_database()`.

2. **Data Collection**:
  - The `data_Collection` function continuously reads sensor data, calculates power, and stores the data in the database.

3. **Web Posting**:
  - The `sen_web.post_sensor_data` function posts the collected data to a web interface.

4. **Multithreading**:
  - Two threads are created:
    - One for data collection.
    - One for web posting.
  - Both threads run concurrently.

5. **Graceful Shutdown**:
  - The script handles interruptions (e.g., `KeyboardInterrupt`) and ensures proper cleanup of resources.

## Entry Point

The script starts execution from the `main()` function, which orchestrates the entire workflow.

## Dependencies

- `sens_db`: Module for database operations.
- `sen_web`: Module for web interface operations.
- `sen_hal`: Module for hardware abstraction layer operations.

## Notes

- The script assumes a constant voltage of 230V for power calculations.
- The `DEVICE_IDS` list can be updated to include multiple devices.

## Example Usage

Run the script using the following command:
```bash
python main.py
```