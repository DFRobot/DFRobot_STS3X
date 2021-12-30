/*!
 * @file  DFRobot_STS3X.h
 * @brief  Realize the specific function of class DFRobot_STS3X
 * @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license  The MIT License (MIT)
 * @author  [yufeng](yufeng.luo@dfrobot.com)
 * @maintainer  [qsjhyy](yihuan.huang@dfrobot.com)
 * @version  V1.0
 * @date  2021-11-18
 * @url  https://github.com/DFRobot/DFRobot_STS3X
 */
#ifndef _DFRobot_STS3X_H
#define _DFRobot_STS3X_H

#include "Arduino.h"
#include <Wire.h>


/* I2C ADDRESS */
#define STS3X_I2C_ADDRESS_A                0x4A   ///< The I2C communication address when addr pin is connected to GND
#define STS3X_I2C_ADDRESS_B                0x4B   ///< The I2C communication address when addr pin is connected to VCC

// The repeatability setting influences the measurement duration and thus the overall energy consumption of the sensor
// Oversampling (repeatability) setting of single measurement mode
#define STS3X_CMD_CLK_STR_EN_NULL          0x2C
#define STS3X_CMD_CLK_STR_EN_HIGH          0x06
#define STS3X_CMD_CLK_STR_EN_MED           0x0D
#define STS3X_CMD_CLK_STR_EN_LOW           0x10

#define STS3X_CMD_CLK_STR_DIS_NULL         0x24
#define STS3X_CMD_CLK_STR_DIS_HIGH         0x00
#define STS3X_CMD_CLK_STR_DIS_MED          0x0B
#define STS3X_CMD_CLK_STR_DIS_LOW          0x16

// Frequency setting of period measurement mode
#define STS3X_CMD_MEA_PER_2S_NULL          0x20
#define STS3X_CMD_MEA_PER_2S_HIGH          0x16
#define STS3X_CMD_MEA_PER_2S_MED           0x24
#define STS3X_CMD_MEA_PER_2S_LOW           0x2F

#define STS3X_CMD_MEA_PER_1HZ_NULL         0x21
#define STS3X_CMD_MEA_PER_1HZ_HIGH         0x30
#define STS3X_CMD_MEA_PER_1HZ_MED          0x26
#define STS3X_CMD_MEA_PER_1HZ_LOW          0x2D

#define STS3X_CMD_MEA_PER_2HZ_NULL         0x22
#define STS3X_CMD_MEA_PER_2HZ_HIGH         0x36
#define STS3X_CMD_MEA_PER_2HZ_MED          0x20
#define STS3X_CMD_MEA_PER_2HZ_LOW          0x2B

#define STS3X_CMD_MEA_PER_4HZ_NULL         0x23
#define STS3X_CMD_MEA_PER_4HZ_HIGH         0x34
#define STS3X_CMD_MEA_PER_4HZ_MED          0x22
#define STS3X_CMD_MEA_PER_4HZ_LOW          0x29

#define STS3X_CMD_MEA_PER_10HZ_NULL        0x27
#define STS3X_CMD_MEA_PER_10HZ_HIGH        0x37
#define STS3X_CMD_MEA_PER_10HZ_MED         0x21
#define STS3X_CMD_MEA_PER_10HZ_LOW         0x2A

// MSB bits of the command to read data in periodic measurement mode
#define STS3X_CMD_READ_FETCH_DATA          0xE0

// The command to stop sensor working and force it enter into idle status
#define STS3X_CMD_BREAK_MSB                0x30
#define STS3X_CMD_BREAK_LSB                0x93

// Soft reset command
#define STS3X_CMD_SOFT_RESET_MSB           0x30
#define STS3X_CMD_SOFT_RESET_LSB           0xA2

// Command to enable/disable the heater
#define STS3X_CMD_HEATER_NULL              0x30
#define STS3X_CMD_HEATER_ENABLE            0x6D
#define STS3X_CMD_HEATER_DISABLE           0x66

// General reset command
#define STS3X_CMD_GENERAL_RESET            0x0006

// Command to read the sensor status
#define STS3X_CMD_READ_STATUS_MSB          0xF3
#define STS3X_CMD_READ_STATUS_LSB          0x2D

// Command to clear the sensor status
#define STS3X_CMD_CLEAR_STATUS_MSB         0x30
#define STS3X_CMD_CLEAR_STATUS_LSB         0x41

// #define ENABLE_DBG   //!< open this macro and you can see the details of the program
#ifdef ENABLE_DBG
  #define DBG(...) {Serial.print("[");Serial.print(__FUNCTION__); Serial.print("(): "); Serial.print(__LINE__); Serial.print(" ] "); Serial.println(__VA_ARGS__);}
#else
  #define DBG(...)
#endif


class DFRobot_STS3X
{
public:
    /**
     * @enum  eCode_t
     * @brief  The sensor repeat measurement rate
     */
    typedef enum
    {
        eHigh,
        eMedium,
        eLow
    }eCode_t;

    /**
     * @enum  eFreq_t
     * @brief  Period measurement frequency
     */
    typedef enum
    {
        e2S,
        e1Hz,
        e2Hz,
        e4Hz,
        e10Hz
    }eFreq_t;

    /**
     * @fn DFRobot_STS3X
     * @brief Constructor
     * @param pWire Wire object is defined in Wire.h, so just use &Wire, and the methods in Wire can be pointed to and used
     * @param i2cAddr Wire address
     * @return None
     */
    DFRobot_STS3X(TwoWire *pWire = &Wire, uint8_t i2cAddr = STS3X_I2C_ADDRESS_B);

    /**
     * @fn begin
     * @brief Init chip 
     * @return True means I2C communication succeeds, false means it fails.
     */
    bool begin(void);

    /**
     * @fn setRepeat
     * @brief Set repeat measurement rate (mode) of the sensor
     * @n The repeatability setting influences the measurement duration and thus the overall energy consumption of the sensor
     * @param code: Select eHigh, eMedium and eLow mode in the enumeration variable eCode_t
     * @return None
     */
    void setRepeat(eCode_t code);

    /**
     * @fn setStretch
     * @brief Set clock stretching. After enabling clock stretching, it won’t send NAK when the measurement is not done; it will send data to complete the unfinished measurement command until the measurement is done.
     * @param clockStretch: Whether to turn on clock stretching, true for on, false for off
     * @return None
     */
    void setStretch(bool clockStretch);

    /**
     * @fn setFreq
     * @brief Set measurement frequency, enable period measurement mode of the sensor (set measurement frequency is equivalent to send the command of enabling period measurement mode)
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
     * @brief Get and save all the current status of sensor
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
     * @fn tempTrackingAlert
     * @brief Temp tracking alert
     * @return true: no alert
     * @n      false: alert
     */
    bool tempTrackingAlert(void);

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


protected:
    /**
     * @fn clearStatus
     * @brief Clear all the current status of the sensor status register
     * @return None
     */
    void clearStatus(void);

    /**
     * @fn writeCommand
     * @brief Communicate with the sensor through I2C
     * @param pBuf Storage and buffer for data to be written
     * @param size Length of data to be written
     * @return None
     */
    virtual void writeCommand(const void *pBuf, size_t size);

    /**
     * @fn readData
     * @brief Communicate with the sensor through I2C
     * @param pBuf Storage and buffer for data to be read
     * @param size Length of the data to be read
     * @return Always return 1
     */
    virtual uint8_t readData(const void* pBuf, size_t size);


private:
    /**
     * @fn checkCRC8
     * @brief Check whether the returned CRC is the same as the CRC8 checked by the two data at the data bit
     * @param cmd for calculating the data pointer to the check code
     * @param Num for calculating the data length of the check code
     * @return Returning 0 means the crc is right, returning other values for the crc error
     */
    bool checkCRC8(uint8_t *cmd, uint8_t Num);

    /**
     * @fn calculateCrc
     * @brief Calculate the CRC corresponding to the data
     * @param data Data at data bits
     * @return The CRC calculation result
     */
    uint8_t calculateCrc(uint8_t data[]);

    TwoWire *_pWire;
    uint8_t _deviceAddr;
    uint8_t _repeat;
    uint8_t _stretch;
    eFreq_t _freq;
    uint16_t _status;
};

#endif
