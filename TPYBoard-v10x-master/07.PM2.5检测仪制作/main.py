#main.py
import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
from ubinascii import hexlify
from ubinascii import *


leds = [pyb.LED(i) for i in range(1,5)] 
P,L,SHUCHU=0,0,0
#A比例系数，在北方一般使用800-1000.南方空气好一些，一般使用600-800.这个还和你使用的传感器灵敏度有关的，需要自己测试再定下来
A=800
#G为固定系数，是为了把串口收到的数据转换成PM标准值
G=1024/5
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST    = pyb.Pin('Y10')
CE     = pyb.Pin('Y11')
DC     = pyb.Pin('Y9')
LIGHT  = pyb.Pin('Y12')
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
u2 = UART(2, 2400)
count_=0
def ChangeLEDState(num_):
    global leds
    len_=len(leds)
    for i in range(0,len_):
        if i!=num_:
            leds[i].off()
        else:
            leds[i].on()
while True:
    u2.init(2400, bits=8, parity=None, stop=1)
    pyb.delay(80)
    Quality='DATA NULL'
    if(u2.any()>0):
        u2.deinit()
        _dataRead=u2.read()
        #R代表截取数据的起始位
        R=_dataRead.find(b'\xaa')
        #R>-1代表存在起始位，长度大于起始位位置+2
        if R>-1 and len(_dataRead)>(R+2):
            P=_dataRead[R+1]
            L=_dataRead[R+2]
            #把串口收到的十六进制数据转换成十进制
            SHI=P*256+L  
            SHUCHU=SHI/G*A
        if(SHUCHU<35):
            Quality = 'Excellente'
            print('环境质量:优','PM2.5=',SHUCHU)
            count_=1
        elif(35<SHUCHU<75):
            Quality = 'Good'
            print('环境质量：良好','PM2.5=',SHUCHU)
            count_=1
        elif(75<SHUCHU<115):
            Quality = 'Slightly-polluted'
            print('环境质量：轻度污染 ','PM2.5=',SHUCHU)
            count_=3
        elif(115<SHUCHU<150):
            Quality = 'Medium pollution'
            print('环境质量：中度污染 ','PM2.5=',SHUCHU)
            count_=2
        elif(150<SHUCHU<250):
            Quality = 'Heavy pollution'
            print('环境质量：重度污染 ','PM2.5=',SHUCHU)
            count_=0
        elif(250<SHUCHU):
            Quality = 'Serious pollution'
            print('环境质量：严重污染 ','PM2.5=',SHUCHU)
            count_=0
    ChangeLEDState(count_)
    lcd_5110.lcd_write_string('AQI Level',0,0)
    lcd_5110.lcd_write_string(str(Quality),0,1)
    lcd_5110.lcd_write_string('PM2.5:',0,2)
    lcd_5110.lcd_write_string(str(SHUCHU),0,3)