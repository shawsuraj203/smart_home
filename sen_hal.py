import time
import board
import busio
import Adafruit_ADS1x15
import random

adc = None

# Gain setting for the ADC (adjust based on your voltage range)
GAIN = 1
# ACS712 constants
ACS712_SENSITIVITY = 0.185  # Sensitivity in V/A (e.g., 185mV/A for 5A module)
VREF = 2.048  # Reference voltage for ADS1115
ADC_RESOLUTION = 32768  # 16-bit ADC resolution

def adc_init():
  """
  Initialize the ADC.
  """
  global adc
  # Create an ADS1115 ADC instance
  # Create the I2C bus
  bus = busio.I2C(board.SCL, board.SDA)
  adc = Adafruit_ADS1x15.ADS1115(i2c=bus)

def read_current(device_id):
  # Read raw ADC value
  raw_value = adc.read_adc(device_id, gain=GAIN)
  
  # Convert raw ADC value to voltage
  voltage = (raw_value / ADC_RESOLUTION) * VREF
  
  # Calculate current in Amperes
  current = (voltage - (VREF / 2)) / ACS712_SENSITIVITY
  return current

'''
def read_current(device_id):
  return random.uniform(0, 5)  # Simulate current reading for testing
'''