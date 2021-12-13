# DFRobot_STS3X
* [中文版](./README_CN.md)

High-Accuracy Digital Temperature Sensor IC
Fully calibrated and linearized digital output
Wide supply voltage range, from 2.15 V to 5.5 V 
I2C Interface with communication speeds up to 1 
MHz and two user selectable addresses
Accuracy of up to 0.1 °C
Very fast start-up and measurement time 
Tiny 8-pin DFN package
NIST traceability

![产品实物图](./resources/images/STS35.png)


## Product Link (链接到英文商城)
    SKU：SEN0434


## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)


## Summary

* Get the real-time temperature <br>
* Set measurement mode <br>
* Get the sensor status <br>


## Installation

Download the library file before use, paste it into the \Arduino\libraries directory, then open the sample folder and run the demo in the folder.


## Methods

```C++

  /**
   * @fn begin
   * @brief Init chip 
   * @return True means I2C communication succeeds, false means it fails.
   */
  bool begin(void);

  /**
   * @fn setRepeat
   * @brief Set repeat measurement rate (mode) of the sensor
   * @n Repeat setting will affect measurement duration and thereby impact the overall power consumption.
   * @param code: Select eHigh, eMedium and eLow mode in the enumeration variable eCode_t
   * @return None
   */
  void setRepeat(eCode_t code);

  /**
   * @fn setStretch
   * @brief Set clock stretching. After enabling clock stretching, the sensor won’t send NAK when the measurement is done; it won’t send data to complete the unfinished measurement command until the measurement is done.
   * @param clockStretch: Whether to turn on clock stretching, true for on, false for off
   * @return None
   */
  void setStretch(bool clockStretch);

  /**
   * @fn setFreq
   * @brief Set measurement frequency, enable period measurement mode of the sensor (set measurement frequency is equivalently to send the command of enabling period measurement mode)
   * @param freq: Select e2S, e1Hz, e2Hz, e4Hz and e10Hz mode in the enumeration variable eFreq_t
   * @return None
   */
  void setFreq(eFreq_t freq);

  /**
   * @fn setHeaterOn
   * @brief Set the heater on
   * @return None
   */
  void setHeaterOn(void);

  /**
   * @fn setHeaterOff
   * @brief Set the heater off
   * @return None
   */
  void setHeaterOff(void);

  /**
   * @fn breakSensor
   * @brief Break the ongoing work of the sensor, force it to enter into idle mode
   * @return None
   */
  void breakSensor(void);

  /**
   * @fn resetSensor
   * @brief Reset the sensor
   * @return None
   */
  void resetSensor(void);

  /**
   * @fn getStatus
   * @brief Get and save the current status of sensor
   * @n Every once in a while, you need to call the interface before using other api to get the current status of the sensor
   * @return None
   */
  void getStatus(void);

  /**
   * @fn checkSumStatus
   * @brief Get checksum status
   * @return true: checksum of last write transfer was correct
   * @n      false: checksum of last write transfer failed
   */
  bool checkSumStatus(void);

  /**
   * @fn commandStatus
   * @brief Get command status
   * @return true: last command executed successfully
   * @n      false: last command not processed.
   */
  bool commandStatus(void);

  /**
   * @fn systemResetDetected
   * @brief Detect whether the system is reset
   * @return true: no reset detected since last 'clear status register' command
   * @n      false: reset detected (hard reset, soft reset command or supply fail)
   */
  bool systemResetDetected(void);

  /**
   * @fn heaterStatus
   * @brief Temp tracking alert
   * @return true: no alert
   * @n      false: alert
   */
  bool temTrackingAlert(void);

  /**
   * @fn heaterStatus
   * @brief Get heater status
   * @return true: Heater OFF
   * @n      false: Heater ON
   */
  bool heaterStatus(void);

  /**
   * @fn alertPendingStatus
   * @brief Get alert pending status
   * @return true: no pending alerts
   * @n      false: at least one pending alert
   */
  bool alertPendingStatus(void);

  /**
   * @fn getTemperatureSingleC
   * @brief Under single measurement mode, get the current temp, note: ensure the sensor is in idle mode by calling related api: breakSensor()
   * @return The measured temp data under single measurement mode, unit: ℃
   */
  float  getTemperatureSingleC(void);

  /**
   * @fn getTemperaturePeriodC
   * @brief Under period measurement mode, get the current temp, note: set the sampling frequency in advance by calling related api: setFreq(eFreq_t freq)
   * @return The measured temp data under period measurement mode, unit: ℃
   */
  float getTemperaturePeriodC(void);

```


## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | :----:
Arduino Uno        |      √       |              |             |
Arduino MEGA2560   |      √       |              |             |
Arduino Leonardo   |      √       |              |             |
FireBeetle-ESP32   |      √       |              |             |
Micro:bit          |      √       |              |             |


## History

- 2021/09/01 - Version 1.0.0 released.


## Credits

Written by(yufeng.luo@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))





