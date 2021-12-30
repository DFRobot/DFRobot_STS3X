/*!
 * @file getTemperature.ino
 * @brief Enable period measurement mode of the sensor (set measurement frequency is equivalent to send the command of enabling period measurement mode)
 * @n Get the measured temp data of the sensor under period measurement mode
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
 * ADDR pin or pull-up: STS3X_I2C_ADDRESS_B   0x4B
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
     * Set measurement frequency
     * freq: Select e2S, e1Hz, e2Hz, e4Hz and e10Hz mode in the enumeration variable eFreq_t
     */
    sts.setFreq(sts.e10Hz);

}

void loop() {
    Serial.print(sts.getTemperaturePeriodC());
    Serial.println(" ℃");
    delay(1000);
}
