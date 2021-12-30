# DFRobot_STS3X
* [English Version](./README.md)

高精度数字温度传感器集成电路
完全校准和线性化数字输出
电源电压范围宽，从2.15 V到5.5 V
I2C接口，通讯速度可达1
MHz和两个用户可选地址
精度可达0.1°C
启动和测量时间非常快
Tiny 8-pin DFN包
NIST可追溯性。

![产品实物图](./resources/images/STS35.png)


## 产品链接 (链接到英文商城)
    SKU: SEN0434


## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性)
* [历史](#历史)
* [创作者](#创作者)


## 概述

* 获取实时温度<br>
* 设置测量模式<br>
* 获取传感器状态<br>


## 库安装

要使用这个库，首先下载库文件，将其粘贴到\Arduino\libraries目录中，然后打开示例文件夹并在文件夹中运行演示。


## 方法

```C++

  /**
   * @fn begin
   * @brief Init chip 
   * @return True means I2C communication succeeds, false means it fails.
   */
  bool begin(void);

  /**
   * @fn setRepeat
   * @brief 设置传感器重复测量速率（模式）
   * @n 重复性设置影响测量持续时间，从而影响传感器的总能耗。
   * @param code: 在枚举变量eCode_t中选择eHigh，eMedium，eLow模式
   * @return None
   */
  void setRepeat(eCode_t code);

  /**
   * @fn setStretch
   * @brief 设置时钟延展，开启时钟延展后，当传感器未测量完成时不会发送NAK，直到测量完成时才发送数据完成之前未完成的测量命令
   * @param clockStretch: 是否打开时钟延展，true表示打开，false表示关闭
   * @return None
   */
  void setStretch(bool clockStretch);

  /**
   * @fn setFreq
   * @brief 设置测量频率，开启传感器周期测量模式（设置周期测量频率，相当于发送开启周期测量模式的指令）
   * @param freq: 在枚举变量eFreq_t中选择e2S，e1Hz，e2Hz，e4Hz，e10Hz模式
   * @return None
   */
  void setFreq(eFreq_t freq);

  /**
   * @fn setHeaterOn
   * @brief 打开加热器
   * @return None
   */
  void setHeaterOn(void);

  /**
   * @fn setHeaterOff
   * @brief 关闭加热器
   * @return None
   */
  void setHeaterOff(void);

  /**
   * @fn breakSensor
   * @brief 中断传感器正在进行的工作，强制使其进入空闲模式
   * @return None
   */
  void breakSensor(void);

  /**
   * @fn resetSensor
   * @brief 将参数设置回默认值
   * @return None
   */
  void resetSensor(void);

  /**
   * @fn getStatus
   * @brief 获取并保存传感器当前所有状态
   * @n 每隔一段时间之后需要先调用这个接口，才能用其他api获得传感器当前的状态
   * @return None
   */
  void getStatus(void);

  /**
   * @fn checkSumStatus
   * @brief 获取校验和状态
   * @return true: checksum of last write transfer was correct
   * @n      false: checksum of last write transfer failed
   */
  bool checkSumStatus(void);

  /**
   * @fn commandStatus
   * @brief 获取指令状态
   * @return true: last command executed successfully
   * @n      false: last command not processed.
   */
  bool commandStatus(void);

  /**
   * @fn systemResetDetected
   * @brief 检测系统是否重置
   * @return true: no reset detected since last 'clear status register' command
   * @n      false: reset detected (hard reset, soft reset command or supply fail)
   */
  bool systemResetDetected(void);

  /**
   * @fn tempTrackingAlert
   * @brief 温度跟踪提醒
   * @return true: no alert
   * @n      false: alert
   */
  bool tempTrackingAlert(void);

  /**
   * @fn heaterStatus
   * @brief 获取加热器状态
   * @return true: Heater OFF
   * @n      false: Heater ON
   */
  bool heaterStatus(void);

  /**
   * @fn alertPendingStatus
   * @brief 获取警报待处理状态
   * @return true: no pending alerts
   * @n      false: at least one pending alert
   */
  bool alertPendingStatus(void);

  /**
   * @fn getTemperatureSingleC
   * @brief 单次测量模式下，获取当前温度，注：需保证传感器处于空闲状态，可以调用相关api：breakSensor()
   * @return 单次测量模式下的温度测量数据，单位：℃
   */
  float  getTemperatureSingleC(void);

  /**
   * @fn getTemperaturePeriodC
   * @brief 周期测量模式下，获取当前温度，注：需提前设置采样频率，可以调用相关api：setFreq(eFreq_t freq)
   * @return 周期测量模式下的温度测量数据，单位：℃
   */
  float getTemperaturePeriodC(void);

```


## 兼容性

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | :----:
Arduino Uno        |      √       |              |             |
Arduino MEGA2560   |      √       |              |             |
Arduino Leonardo   |      √       |              |             |
FireBeetle-ESP32   |      √       |              |             |
Micro:bit          |      √       |              |             |


## 历史

- 2021/09/01 - 1.0.0 版本
- 2021/12/30 - 1.0.1 版本


## 创作者

Written by(yufeng.luo@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))
