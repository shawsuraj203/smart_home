import time
import logging
#import random

import Adafruit_ADS1x15

from  logger import setup_logger, log_message, get_logger

adc = None
log = None

# Gain setting for the ADC (adjust based on your voltage range)
GAIN = 1
# ACS712 constants
ACS712_SENSITIVITY = 0.100  # Sensitivity in V/A (e.g., 100mV/A for 20A module)
VREF = 5  # Reference voltage for ADS1115
ADC_RESOLUTION = 32768  # 16-bit ADC resolution
ADC_CALIBRATION = 4042  # Calibration offset for the ADC (if needed)

def adc_init():
  """
  Initialize the ADC.
  """
  global adc
  global log 
  log = get_logger()
  # Create an ADS1115 ADC instance
  adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
  log_message(log, "ADC initialized successfully.", level=logging.INFO)

def read_current(device_id):
  data = []
  try:
    # Read raw ADC value
    for i  in range(10):
      data.append(adc.read_adc(device_id, gain=GAIN))
      time.sleep(1.5)
    raw_value = max(data) - ADC_CALIBRATION # Get the maximum value from the readings
    if raw_value < ADC_RESOLUTION/2:
      raw_value = ADC_RESOLUTION/2 # Set a minimum threshold to avoid negative values
    # Calculate the average ADC value
    log_message(log, "Raw ADC Value: {0}".format(raw_value), level=logging.DEBUG)
    # Convert raw ADC value to voltage
    voltage = (raw_value / ADC_RESOLUTION) * VREF
    log_message(log, "Voltage: {0:.2f} V".format(voltage), level=logging.DEBUG)
    # Calculate current in Amperes
    current = (voltage - (VREF / 2)) / ACS712_SENSITIVITY
    log_message(log, "Current: {0:.2f} A".format(current), level=logging.INFO)
  except Exception as e:
    log_message(log, "Exception occurred: {}".format(e), level=logging.DEBUG)
    current = None
  return current


