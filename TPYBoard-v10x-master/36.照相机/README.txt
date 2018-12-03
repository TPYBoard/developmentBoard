实例的大概简介
-----------------------
TPYBoard v102 通过串口与串口摄像头模块（PTC06）进行连接，通过按键控制模块进行拍照，并保存到TF卡中。


接线方式

TPYBoard v102   摄像头模块
---------------------------
    VIN            5V
    GND            GND
    X1(UART 4 TX)  RX
    X2(UART 4 RX)  TX

TPYBoard v102   LCD5110显示屏
---------------------------      
    Y12       RST
    Y11       CE
    Y10       DC
    Y9        LIGHT
    X8        DIN
    X6        CLK
    3.3V      VIN
    GND       GND

按键引出
------------------
将TPYBoard v102上面的两个板子按键RST、USR引出，好嵌入到相机纸盒的顶部。由于板子按键初始化默认为低电平。
所以接按键模块时，需要将正负极反过来接。

TPYBoard v102   RST按键（黑色） 
--------------------------------
    3.3V         GND             
    GND          VCC           
    RST          OUT


TPYBoard v102    USR按键（黄色）
---------------------------------
    GND          VCC 
    3.3V         GND   
    X17          OUT

