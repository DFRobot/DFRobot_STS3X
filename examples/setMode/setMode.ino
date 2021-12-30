/*!
 * @file setMode.ino
 * @brief Set parameters like sampling repeat rate (over sampling, improve the data accuracy and filter the error data), clock stretching and the heater. Get the temp data under single measurement mode.
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
    /*Wait for the chip to be initialized completely, and then exit*/
    while(sts.begin() != true){
        Serial.println("Failed to init chip, please check if the chip connection is fine. ");
        delay(1000);
    }
    Serial.println("Begin ok!");

    /**
     * Set repeat mode
     * code: Select eHigh, eMedium and eLow mode in the enumeration variable eCode_t
     */
    sts.setRepeat(sts.eHigh);

    /**
     * Set clock stretching. After enabling clock stretching, it won’t send NAK when the measurement is not done; it will send data to complete the unfinished measurement command until the measurement is done.
     * clockStretch: Whether to turn on clock stretching, true for on, false for off
     */
    sts.setStretch(true);

    /**
     * Turn on or off the heater, increase the sensor temp for easy internal test
     */
    sts.setHeaterOn();
    //sts.setHeaterOff();

    /**
     * Break the ongoing work of the sensor, force it to enter into idle mode
     */
    sts.breakSensor();

    /**
     * Reset the sensor
     */
    //sts.resetSensor();
}

void loop() {
    Serial.print(sts.getTemperatureSingleC());
    Serial.println(" ℃");
    delay(1000);
}
