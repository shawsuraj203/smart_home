# `sen_hal.py` - Sensor Hardware Abstraction Layer

This module provides functionality to interface with an ADC (Analog-to-Digital Converter) and read current values using an ACS712 current sensor.

## Constants

- **`GAIN`**: Gain setting for the ADC. Adjust this based on your voltage range.
- **`ACS712_SENSITIVITY`**: Sensitivity of the ACS712 current sensor in V/A (e.g., 185mV/A for a 5A module).
- **`VREF`**: Reference voltage for the ADS1115 ADC.
- **`ADC_RESOLUTION`**: Resolution of the ADC (16-bit, 32768).

## Global Variables

- **`adc`**: A global variable to hold the ADC instance.

## Functions

### `adc_init()`
Initializes the ADC by creating an instance of the ADS1115 ADC and setting up the I2C bus.

#### Example Usage:
```python
adc_init()
```

### `read_current(device_id)`
Reads the current value for a given device ID.

1. Reads the raw ADC value using the `read_adc` method.
2. Converts the raw ADC value to voltage using the formula:
   ```
   voltage = (raw_value / ADC_RESOLUTION) * VREF
   ```
3. Calculates the current in amperes using the formula:
   ```
   current = (voltage - (VREF / 2)) / ACS712_SENSITIVITY
   ```
4. Returns the calculated current.

#### Parameters:
- **`device_id`**: The ID of the device to read the current for.

#### Returns:
- **`current`**: The calculated current in amperes.

#### Example Usage:
```python
current = read_current(0)
print(f"Current: {current} A")
```

## Notes
- The commented-out `read_current` function at the bottom simulates current readings for testing purposes by returning random values between 0 and 5 amperes.

#### Simulated Function:
```python
def read_current(device_id):
    return random.uniform(0, 5)  # Simulate current reading for testing
```

## Dependencies
- `time`: Standard Python library for time-related functions.
- `board`: Library for accessing board-specific I2C pins.
- `busio`: Library for creating I2C bus instances.
- `Adafruit_ADS1x15`: Library for interfacing with the ADS1115 ADC.
- `random`: Standard Python library for generating random numbers (used in the simulated function).

## Example Workflow
1. Initialize the ADC:
   ```python
   adc_init()
   ```
2. Read the current for a specific device:
   ```python
   current = read_current(0)
   print(f"Current: {current} A")
   ```