/*!
 * @file  getStatus.ino
 * @brief  Get all the current status of the sensor, and parse and print them one by one.
 * @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license  The MIT License (MIT)
 * @author  [LuoYufeng](yufeng.luo@dfrobot.com)
 * @maintainer  [qsjhyy](yihuan.huang@dfrobot.com)
 * @version  V1.0
 * @date  2021-11-18
 * @url  https://github.com/DFRobot/DFRobot_STS3X
 */
#include "DFRobot_STS3X.h"

/**
 * Determine I2C address according to the ADDR pin pull-up or pull-down
 * ADDR pin pull-down: STS3X_I2C_ADDRESS_A   0x4A
 * ADDR pin pull-up: STS3X_I2C_ADDRESS_B   0x4B
 */
DFRobot_STS3X sts(&Wire, STS3X_I2C_ADDRESS_B);


void setup(void)
{
    Serial.begin(9600);
    /* Wait for the chip to be initialized completely, and then exit */
    while(sts.begin() != true){
        Serial.println("Failed to init chip, please check if the chip connection is fine. ");
        delay(1000);
    }
    Serial.println("Begin ok!");

    /**
     * Get and save all the current status of sensor
     * Every once in a while, you need to call the interface before using other api to get the current status of the sensor
     */
    sts.getStatus();

    /**
     * Get checksum status
     *  true: checksum of last write transfer was correct
     *  false: checksum of last write transfer failed
     */
    if(sts.checkSumStatus() == true)
        Serial.println("checksum of last write transfer was correct");
    else
        Serial.println("checksum of last write transfer failed");

    /**
     * Get command status
     *  true: last command executed successfully
     *  false: last command not processed.
     */
    if(sts.commandStatus() == true)
        Serial.println("last command executed successfully");
    else
        Serial.println("last command not processed");

    /**
     * Detect whether the system is reset
     *  true: no reset detected since last 'clear status register' command
     *  false: reset detected (hard reset, soft reset command or supply fail)
     */
    if(sts.systemResetDetected() == true)
        Serial.println("no reset detected since last 'clear status register' command");
    else
        Serial.println("reset detected");

    /**
     * Temp tracking alert
     *  true: no alert
     *  false: alert
     */
    if(sts.temTrackingAlert() == true)
        Serial.println("temperature have not been alerted");
    else
        Serial.println("temperature have been alerted");

    /**
     * Get heater status
     *  true: Heater OFF
     *  false: Heater ON
     */
    if(sts.heaterStatus() == true)
        Serial.println("Heater has been closed");
    else
        Serial.println("Heater has been opened");

    /**
     * Get alert pending status
     *  true: no pending alerts
     *  false: at least one pending alert
     */
    if(sts.alertPendingStatus() == true)
        Serial.println("There is no pending alert");
    else
        Serial.println("There is at least pending alert");
}

void loop() {
    
}
