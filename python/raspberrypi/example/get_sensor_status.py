# -*- coding: utf-8 -*
'''!
  # @file  get_sensor_status.py
  # @brief  Get all the current status of the sensor, and parse and print them one by one
  # @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  # @license  The MIT License (MIT)
  # @author  [qsjhyy](yihuan.huang@dfrobot.com)
  # @version  V1.0
  # @date  2021-11-18
  # @url  https://github.com/DFRobot/DFRobot_STS3X
'''
from __future__ import print_function
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from DFRobot_STS3X import *

# Determine I2C address according to the ADDR pin pull-up or pull-down
# ADDR pin pull-down: STS3X_I2C_ADDRESS_A   0x4A
# ADDR pin pull-up: STS3X_I2C_ADDRESS_B   0x4B
sensor = DFRobot_STS3X(i2c_addr = STS3X_I2C_ADDRESS_A,bus = 1)

def setup():
  sensor.begin()
  print("sensor begin successfully!!!")

  '''
    # Get and save all the current status of sensor
    # Every once in a while, you need to call the interface before using other api to get the current status of the sensor
  '''
  sensor.get_sensor_status()

  '''
    # Get checksum status
    #  true: checksum of last write transfer was correct
    #  false: checksum of last write transfer failed
  '''
  if sensor.check_sum_status():
      print("checksum of last write transfer was correct")
  else:
      print("checksum of last write transfer failed")

  '''
    # Get command status
    #  true: last command executed successfully
    #  false: last command not processed.
  '''
  if sensor.command_status():
      print("last command executed successfully")
  else:
      print("last command not processed")

  '''
    # Detect whether the system is reset
    #  true: no reset detected since last 'clear status register' command
    #  false: reset detected (hard reset, soft reset command or supply fail)
  '''
  if sensor.system_reset_detected():
      print("no reset detected since last 'clear status register' command")
  else:
      print("reset detected")

  '''
    # Temp tracking alert
    #  true: no alert
    #  false: alert
  '''
  if sensor.temp_tracking_alert():
      print("temperature have not been alerted")
  else:
      print("temperature have been alerted")

  '''
    # Get heater status
    #  true: Heater OFF
    #  false: Heater ON
  '''
  if sensor.heater_status():
      print("Heater has been closed")
  else:
      print("Heater has been opened")

  '''
    # Get alert pending status
    #  true: no pending alerts
    #  false: at least one pending alert
  '''
  if sensor.alert_pending_status():
      print("There is no pending alert")
  else:
      print("There is at least pending alert")

def loop():
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()
