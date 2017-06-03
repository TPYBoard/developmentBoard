import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
from ubinascii import hexlify
from ubinascii import *


leds = [pyb.LED(i) for i in range(1,5)]
P,L,SHUCHU=0,0,0
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST    = pyb.Pin('X20')
CE     = pyb.Pin('X19')
DC     = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
count_=0
N2 = Pin('Y3', Pin.OUT_PP)
N1 = Pin('Y6', Pin.OUT_PP)
N1.low()
pyb.delay(2000)
N1.high()
pyb.delay(10000)
u2 = UART(4, 115200)
i='0'
w=0
d=0
q=0
G=0
j=0
def DataConver(str_,flag):
    wei_=float(str_)/100
    wei_arr=str(wei_).split('.')
    val_=100000
    if flag==0:#纬度
        val_=10000
    wei_arr[1]=str(float(wei_arr[1])/60*val_).replace('.','')
    weidu=wei_arr[0]+'.'+wei_arr[1]
    return weidu
while True:
    pyb.LED(2).on()
    G=G+1
    u2.write('AT+GPSLOC=1\r\n')
    pyb.delay(3000)
    _dataRead=u2.readall()
    print('搜星=',_dataRead)
    pyb.delay(1000)
    u2.write('AT+GPSLOC=0\r\n')
    pyb.delay(200)
    print('BEIDOU')
    _dataRead=u2.readall()
    if _dataRead!=None:
        print('原始数据=',_dataRead)
        print('原始数据长度:',len(_dataRead))
        if 60<len(_dataRead)<70:
            _dataRead = _dataRead.decode('utf-8')
            _dataRead1=_dataRead.split(',')
            print('数据=',_dataRead1)
            print(len(_dataRead1),'***')
            if len(_dataRead1)>4:
#*******************纬度计算********************
                weidu=_dataRead1[1]
                WD=DataConver(weidu,0)
#*******************经度计算********************
                jingdu=_dataRead1[2]
                JD=DataConver(jingdu,1)
#***********************时间************************
    lcd_5110.lcd_write_string('JINGDU:',0,0)
    lcd_5110.lcd_write_string(str(JD),0,1)
    lcd_5110.lcd_write_string('WEIDU:',0,2)
    lcd_5110.lcd_write_string(str(WD),0,3)
