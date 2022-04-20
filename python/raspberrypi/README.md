# DFRobot_STS3X
* [中文版](./README_CN.md)

This High-Accuracy Digital Temperature Sensor has fully-calibrated and linearized digital output and wide supply voltage range from 2.15V to 5.5V. It offers a temperature accuracy of ± 0.1 C°. Its functionality includes enhanced signal processing, two distinctive and user-selectable I2C addresses, communication speeds of up to 1MHz, very fast start-up and measurement time, small 8pin DFN package and NIST traceability.

![正反面svg效果图](../../resources/images/STS35.png)


## Product Link (https://www.dfrobot.com/product-2548.html)
    SKU: SEN0434


## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)


## Summary

* Get the real-time temp
* Set measurement mode
* Get the sensor status


## Installation

Download the library file before use, paste it into the specified directory, then open the Examples folder and run the demo in the folder.


## Methods

```python

    '''
       @brief Init the sensor
    '''
    def begin(self)

    '''
       @brief Set repeat mode
       @n The repeat setting will affect the measurement duration and thereby impact the overall energy consumption of the sensor.
       @param repeat, Repeat measurement config mode, there are three modes: REPEAT_HIGH, REPEAT_MEDIUM, REPEAT_LOW
    '''
    def set_repeat(self, repeat=REPEAT_LOW)

    '''
       @brief Set measurement frequency
       @param Data measurement frequency, default to be 1Hz, freq: FREQ_2S, FREQ_1HZ, FREQ_2HZ, FREQ_4HZ, FREQ_10HZ
    '''
    def set_freq(self,  freq=FREQ_1HZ)

    '''
       @brief Turn the heater on
    '''
    def set_heater_on(self)

    '''
       @brief Turn the heater off
    '''
    def set_heater_off(self)

    '''
       @brief Break off the ongoing work of the sensor to wait the next command
    '''
    def sensor_break(self)

    '''
       @brief Reset the sensor
    '''
    def sensor_reset(self)

    '''
       @brief Get and save all the current status of sensor
       @n Every once in a while, you need to call the interface before using other API to get the current status of the sensor
    '''
    def get_sensor_status(self)

    '''
       @brief Get checksum status
       @return true: checksum of last write transfer is correct 
       @n      false: checksum of last write transfer failed 
    '''
    def check_sum_status(self)

    '''
       @brief Get command status
       @return true: The last command is executed successfully.
       @n      false: The last command is not processed.
    '''
    def command_status(self)

    '''
       @brief Detect whether the system is reset
       @return true: no reset detected since last 'clear status register' command.
       @n      false: reset detected (hard and soft reset command or supply failed)
    '''
    def system_reset_detected(self)

    '''
       @brief Temp tracking alert
       @return true: No alert
       @n      false: There is an alert
    '''
    def temp_tracking_alert(self)

    '''
       @brief Get heater status
       @return true: The heater is off
       @n      false: The heater is on
    '''
    def heater_status(self)

    '''
       @brief Get alert pending status
       @return true: No pending alert
       @n      false: There is at least a pending alert
    '''
    def alert_pending_status(self)

    '''
       @brief Get the current temp under single measurement mode
       @return unit: ℃
    '''
    def get_temperature_single(self)

    '''
       @brief Get the current temp under period measurement mode
       @return unit: ℃
    '''
    def get_temperature_period(self)

```


## Compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |           |            |    √     |         |
| RaspberryPi4 |     √     |            |          |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |


## History

- 2021/09/01 - Version 1.0.0 released.
- 2021/12/30 - Version 1.0.1 released.
- 2022/04/20 - Version 1.0.2 released.


## Credits

Written by qsjhyy(yihuan.huang@dfrobot.com), 2022. (Welcome to our [website](https://www.dfrobot.com/))
