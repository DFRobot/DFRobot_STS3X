# -*- coding: utf-8 -*
'''!
  @file  DFRobot_STS3X.py
  @brief  Define the infrastructure of DFRobot_STS3X class.
  @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license  The MIT License (MIT)
  @author  [yihuan.huang](qsjhyy@dfrobot.com)
  @maintainer  [qsjhyy](yihuan.huang@dfrobot.com)
  @version  V1.0
  @date  2021-11-18
  @url  https://github.com/DFRobot/DFRobot_STS3X
'''
import sys
import time
import smbus
import logging
from ctypes import *


logger = logging.getLogger()
#logger.setLevel(logging.INFO)  #Display all print information
logger.setLevel(logging.FATAL)  #If you don’t want to display too many prints, only print errors, please use this option
ph = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - [%(filename)s %(funcName)s]:%(lineno)d - %(levelname)s: %(message)s")
ph.setFormatter(formatter)
logger.addHandler(ph)


# I2C ADDRESS
## ADDR pin is connected to GND
STS3X_I2C_ADDRESS_A = 0x4A
## ADDR pin is connected to VCC
STS3X_I2C_ADDRESS_B = 0x4B

# Sensor communication command
## "Repeatability measurement" config command high bit
STS3X_CMD_REPEATABILITY_MSB        = 0x24
## "Repeatability measurement" config command low bit, high repeatability
STS3X_CMD_REPEATABILITY_LSB_HIGH   = 0x00
## "Repeatability measurement" config command low bit, medium repeatability
STS3X_CMD_REPEATABILITY_LSB_MEDIUM = 0x0B
## "Repeatability measurement" config command low bit, low repeatability
STS3X_CMD_REPEATABILITY_LSB_LOW    = 0x16

## "0.5Hz measurement frequency" config command high bit
STS3X_CMD_MEA_PER_2S_MSB        = 0x20
## "0.5Hz measurement frequency" config command low bit, high repeatability
STS3X_CMD_MEA_PER_2S_LSB_HIGH   = 0x16
## "0.5Hz measurement frequency" config command low bit, medium repeatability
STS3X_CMD_MEA_PER_2S_LSB_MEDIUM = 0x24
## "0.5Hz measurement frequency" config command low bit, low repeatability
STS3X_CMD_MEA_PER_2S_LSB_LOW    = 0x2F

## "1Hz measurement frequency" config command high bit
STS3X_CMD_MEA_PER_1HZ_MSB        = 0x21
## "1Hz measurement frequency" config command low bit, high repeatability
STS3X_CMD_MEA_PER_1HZ_LSB_HIGH   = 0x30
## "1Hz measurement frequency" config command low bit, medium repeatability
STS3X_CMD_MEA_PER_1HZ_LSB_MEDIUM = 0x26
## "1Hz measurement frequency" config command low bit, low repeatability
STS3X_CMD_MEA_PER_1HZ_LSB_LOW    = 0x2D

## "2Hz measurement frequency" config command high bit
STS3X_CMD_MEA_PER_2HZ_MSB        = 0x22
## "2Hz measurement frequency" config command low bit, high repeatability
STS3X_CMD_MEA_PER_2HZ_LSB_HIGH   = 0x36
## "2Hz measurement frequency" config command low bit, medium repeatability
STS3X_CMD_MEA_PER_2HZ_LSB_MEDIUM = 0x20
## "2Hz measurement frequency" config command low bit, low repeatability
STS3X_CMD_MEA_PER_2HZ_LSB_LOW    = 0x2B

## "4Hz measurement frequency" config command high bit
STS3X_CMD_MEA_PER_4HZ_MSB        = 0x23
## "4Hz measurement frequency" config command low bit, high repeatability
STS3X_CMD_MEA_PER_4HZ_LSB_HIGH   = 0x34
## "4Hz measurement frequency" config command low bit, medium repeatability
STS3X_CMD_MEA_PER_4HZ_LSB_MEDIUM = 0x22
## "4Hz measurement frequency" config command low bit, low repeatability
STS3X_CMD_MEA_PER_4HZ_LSB_LOW    = 0x29

## "10Hz measurement frequency" config command high bit
STS3X_CMD_MEA_PER_10HZ_MSB        = 0x27
## "10Hz measurement frequency" config command low bit, high repeatability
STS3X_CMD_MEA_PER_10HZ_LSB_HIGH   = 0x37
## "10Hz measurement frequency" config command low bit, medium repeatability
STS3X_CMD_MEA_PER_10HZ_LSB_MEDIUM = 0x21
## "10Hz measurement frequency" config command low bit, low repeatability
STS3X_CMD_MEA_PER_10HZ_LSB_LOW    = 0x2A

## Fetch Data command MSB for Periodic Mode
STS3X_CMD_MEA_PER_FETCH_DATA_MSB = 0xE0
## Fetch Data command LSB for Periodic Mode
STS3X_CMD_MEA_PER_FETCH_DATA_LSB = 0x00

## Break command MSB / Stop Periodic Data Acquisition Mode
STS3X_CMD_MEA_PER_BREAK_MSB = 0x30
## Break command LSB / Stop Periodic Data Acquisition Mode
STS3X_CMD_MEA_PER_BREAK_LSB = 0x93

## Soft reset command MSB
STS3X_CMD_SOFT_RESET_MSB = 0x30
## Soft reset command LSB
STS3X_CMD_SOFT_RESET_LSB = 0xA2

## Heater command MSB
STS3X_CMD_HEATER_MSB         = 0x30
## Heater Enable command LSB
STS3X_CMD_HEATER_LSB_ENABLE  = 0x6D
## Heater Disabled command LSB
STS3X_CMD_HEATER_LSB_DISABLE = 0x66

## Reset command using the general call address
STS3X_CMD_GENERAL_RESET = 0x0006

## Read Out of status command MSB
STS3X_CMD_READ_STATUS_MSB = 0xF3
## Read Out of status command LSB
STS3X_CMD_READ_STATUS_LSB = 0x2D

## Clear status command MSB
STS3X_CMD_CLEAR_STATUS_MSB = 0x30
## Clear status command LSB
STS3X_CMD_CLEAR_STATUS_LSB = 0x41


class DFRobot_STS3X(object):
    '''!
      @brief Define DFRobot_STS3X basic class
      @details Drive the temp sensor
    '''

    REPEAT_HIGH   = 0
    REPEAT_MEDIUM = 1
    REPEAT_LOW    = 2

    FREQ_2S   = 0
    FREQ_1HZ  = 1
    FREQ_2HZ  = 2
    FREQ_4HZ  = 3
    FREQ_10HZ = 4

    def __init__(self, i2c_addr=STS3X_I2C_ADDRESS_A, bus=1):
        '''!
          @brief Module init
          @param i2c_addr I2C communication address
          @param bus I2C bus
        '''
        self._i2c_addr = i2c_addr
        self._i2c = smbus.SMBus(bus)
        self._repeat = self.REPEAT_LOW
        self._freq = self.FREQ_1HZ

    def begin(self):
        '''!
           @brief Initialize sensor
        '''
        self.sensor_reset()
        time.sleep(0.1)
        self._clear_sensor_status()
        time.sleep(0.1)
     ## self._status = self.get_sensor_status()
     ## time.sleep(0.1)
     ## self.set_freq(self._freq)
     ## time.sleep(0.1)

    def set_repeat(self, repeat=REPEAT_LOW):
        '''!
           @brief Set repeat mode
           @n The repeatability setting influences the measurement duration and thus the overall energy consumption of the sensor.
           @param repeat Repeat measurement config mode, there are three modes: REPEAT_HIGH, REPEAT_MEDIUM, REPEAT_LOW
        '''
        self._repeat = repeat

    def set_freq(self, freq=FREQ_1HZ):
        '''!
           @brief Set measurement frequency
           @param freq Data measurement frequency, default to be 1Hz, freq: FREQ_2S, FREQ_1HZ, FREQ_2HZ, FREQ_4HZ, FREQ_10HZ
        '''
        self._freq = freq
        if self._freq == self.FREQ_2S:
            CMD_MSB = STS3X_CMD_MEA_PER_2S_MSB
            if self._repeat == self.REPEAT_HIGH:
                CMD_LSB = STS3X_CMD_MEA_PER_2S_LSB_HIGH
            elif self._repeat == self.REPEAT_MEDIUM:
                CMD_LSB = STS3X_CMD_MEA_PER_2S_LSB_MEDIUM
            elif self._repeat == self.REPEAT_LOW:
                CMD_LSB = STS3X_CMD_MEA_PER_2S_LSB_LOW
            else:
                CMD_LSB = STS3X_CMD_MEA_PER_2S_LSB_MEDIUM
        elif self._freq == self.FREQ_1HZ:
            CMD_MSB = STS3X_CMD_MEA_PER_1HZ_MSB
            if self._repeat == self.REPEAT_HIGH:
                CMD_LSB = STS3X_CMD_MEA_PER_1HZ_LSB_HIGH
            elif self._repeat == self.REPEAT_MEDIUM:
                CMD_LSB = STS3X_CMD_MEA_PER_1HZ_LSB_MEDIUM
            elif self._repeat == self.REPEAT_LOW:
                CMD_LSB = STS3X_CMD_MEA_PER_1HZ_LSB_LOW
            else:
                CMD_LSB = STS3X_CMD_MEA_PER_1HZ_LSB_MEDIUM
        elif self._freq == self.FREQ_2HZ:
            CMD_MSB = STS3X_CMD_MEA_PER_2HZ_MSB
            if self._repeat == self.REPEAT_HIGH:
                CMD_LSB = STS3X_CMD_MEA_PER_2HZ_LSB_HIGH
            elif self._repeat == self.REPEAT_MEDIUM:
                CMD_LSB = STS3X_CMD_MEA_PER_2HZ_LSB_MEDIUM
            elif self._repeat == self.REPEAT_LOW:
                CMD_LSB = STS3X_CMD_MEA_PER_2HZ_LSB_LOW
            else:
                CMD_LSB = STS3X_CMD_MEA_PER_2HZ_LSB_MEDIUM
        elif self._freq == self.FREQ_4HZ:
            CMD_MSB = STS3X_CMD_MEA_PER_4HZ_MSB
            if self._repeat == self.REPEAT_HIGH:
                CMD_LSB = STS3X_CMD_MEA_PER_4HZ_LSB_HIGH
            elif self._repeat == self.REPEAT_MEDIUM:
                CMD_LSB = STS3X_CMD_MEA_PER_4HZ_LSB_MEDIUM
            elif self._repeat == self.REPEAT_LOW:
                CMD_LSB = STS3X_CMD_MEA_PER_4HZ_LSB_LOW
            else:
                CMD_LSB = STS3X_CMD_MEA_PER_4HZ_LSB_MEDIUM
        elif self._freq == self.FREQ_10HZ:
            CMD_MSB = STS3X_CMD_MEA_PER_10HZ_MSB
            if self._repeat == self.REPEAT_HIGH:
                CMD_LSB = STS3X_CMD_MEA_PER_10HZ_LSB_HIGH
            elif self._repeat == self.REPEAT_MEDIUM:
                CMD_LSB = STS3X_CMD_MEA_PER_10HZ_LSB_MEDIUM
            elif self._repeat == self.REPEAT_LOW:
                CMD_LSB = STS3X_CMD_MEA_PER_10HZ_LSB_LOW
            else:
                CMD_LSB = STS3X_CMD_MEA_PER_10HZ_LSB_MEDIUM
        else:
            CMD_MSB = STS3X_CMD_MEA_PER_1HZ_MSB
            if self._repeat == self.REPEAT_HIGH:
                CMD_LSB = STS3X_CMD_MEA_PER_1HZ_LSB_HIGH
            elif self._repeat == self.REPEAT_MEDIUM:
                CMD_LSB = STS3X_CMD_MEA_PER_1HZ_LSB_MEDIUM
            elif self._repeat == self.REPEAT_LOW:
                CMD_LSB = STS3X_CMD_MEA_PER_1HZ_LSB_LOW
            else:
                CMD_LSB = STS3X_CMD_MEA_PER_1HZ_LSB_MEDIUM
        self._write_command(CMD_MSB, [CMD_LSB])

    def set_heater_on(self):
        '''!
           @brief Set the heater on
        '''
        self._write_command(STS3X_CMD_HEATER_MSB, [STS3X_CMD_HEATER_LSB_ENABLE])

    def set_heater_off(self):
        '''!
           @brief Set the heater off
        '''
        self._write_command(STS3X_CMD_HEATER_MSB, [STS3X_CMD_HEATER_LSB_DISABLE])

    def sensor_break(self):
        '''!
           @brief Break the ongoing work of the sensor to wait the next command.
        '''
        self._write_command(STS3X_CMD_MEA_PER_BREAK_MSB, [STS3X_CMD_MEA_PER_BREAK_LSB])

    def sensor_reset(self):
        '''!
           @brief Reset the sensor
        '''
        self.sensor_break()
        self._write_command(STS3X_CMD_SOFT_RESET_MSB, [STS3X_CMD_SOFT_RESET_LSB])

    def get_sensor_status(self):
        '''!
           @brief Get and save all the current status of sensor
           @n Every once in a while, you need to call the interface before using other api to get the current status of the sensor.
        '''
        self._write_command(STS3X_CMD_READ_STATUS_MSB, [STS3X_CMD_READ_STATUS_LSB])
        rslt = self._read_data(3)
        if self._crc8_131(rslt) == rslt[2]:
            self._status = rslt[0]<<8 | rslt[1]

    def _clear_sensor_status(self):
        '''!
           @brief Clear the sensor status bit
        '''
        self._write_command(STS3X_CMD_CLEAR_STATUS_MSB, [STS3X_CMD_CLEAR_STATUS_LSB])
        self._status = 0x0000

    def check_sum_status(self):
        '''!
           @brief Get checksum status
           @return true: checksum of last write transfer was correct
           @n      false: checksum of last write transfer failed
        '''
        ret = False
        if (self._status & 0x0001) == 0:
            ret = True
        return ret

    def command_status(self):
        '''!
           @brief Get command status
           @return true: last command executed successfully
           @n      false: last command not processed.
        '''
        ret = False
        if (self._status & 0x0002) == 0:
            ret = True
        return ret

    def system_reset_detected(self):
        '''!
           @brief Detect whether the system is reset
           @return true: no reset detected since last 'clear status register' command
           @n      false: reset detected (hard reset, soft reset command or supply fail)
        '''
        ret = False
        if (self._status & 0x0010) == 0:
            ret = True
        return ret

    def temp_tracking_alert(self):
        '''!
           @brief Temp tracking alert
           @return true: no alert
           @n      false: alert
        '''
        ret = False
        if (self._status & 0x0400) == 0:
            ret = True
        return ret

    def heater_status(self):
        '''!
           @brief Get heater status
           @return true: Heater OFF
           @n      false: Heater ON
        '''
        ret = False
        if (self._status & 0x2000) == 0:
            ret = True
        return ret

    def alert_pending_status(self):
        '''!
           @brief Get alert pending status
           @return true: no pending alerts
           @n      false: at least one pending alert
        '''
        ret = False
        if (self._status & 0x8000) == 0:
            ret = True
        return ret

    def get_temperature_single(self):
        '''!
           @brief Get the current temp under single measurement mode
           @return unit: ℃
        '''
        CMD_MSB = STS3X_CMD_REPEATABILITY_MSB
        if self._repeat == self.REPEAT_HIGH:
            CMD_LSB = STS3X_CMD_REPEATABILITY_LSB_HIGH
        elif self._repeat == self.REPEAT_MEDIUM:
            CMD_LSB = STS3X_CMD_REPEATABILITY_LSB_MEDIUM
        elif self._repeat == self.REPEAT_LOW:
            CMD_LSB = STS3X_CMD_REPEATABILITY_LSB_LOW
        else:
            CMD_LSB = STS3X_CMD_REPEATABILITY_LSB_MEDIUM

        self._write_command(CMD_MSB, [CMD_LSB])
        rslt = self._read_data(3)
        rawData = rslt[0]<<8 | rslt[1]
        result = 0.0
        if self._crc8_131(rslt) == rslt[2]:
            result = 175.0 * float(rawData) / 65535.0 - 45.0
        return result

    def get_temperature_period(self):
        '''!
           @brief Get the current temp under period measurement mode
           @return unit: ℃
        '''
        self._write_command(STS3X_CMD_MEA_PER_FETCH_DATA_MSB, [STS3X_CMD_MEA_PER_FETCH_DATA_LSB])
        rslt = self._read_data(3)
        rawData = rslt[0]<<8 | rslt[1]
        result = 0.0
        if self._crc8_131(rslt) == rslt[2]:
            result = 175.0 * float(rawData) / 65535.0 - 45.0
        return result

    def _crc8_131(self, data):
        '''!
          @brief Calculate crc8 (the polynomial corresponds to 0x131) check code (PEC)
          @param data For calculating the data of check code
          @return CRC calculation results
        '''
        crc = 0xFF
        for i in [0, 1]:
            #logger.info(hex(data[i]))
            crc = (crc & 0xFF) ^ data[i]
            for j in range(8):
                if (crc & 0x80):
                    crc = (crc << 1) ^ 0x31
                else:
                    crc = (crc << 1)
        #logger.info(hex(crc & 0xFF))
        return crc & 0xFF

    def _write_command(self, cmd_msb, cmd_lsb):
        '''!
           @brief writes CMD to a sensor
           @param cmd_msb Command high 8-bit, variable
           @param cmd_lsb Command low 8-bit, array
        '''
        self._i2c.write_i2c_block_data(self._i2c_addr, cmd_msb, cmd_lsb)
        time.sleep(0.01)

    def _read_data(self, length):
        '''!
          @brief read the data from the sensor
          @param length read data length
          @return read data list
        '''
        rslt = self._i2c.read_i2c_block_data (self._i2c_addr, 0x00, length)
        time.sleep(0.01)
        return rslt
