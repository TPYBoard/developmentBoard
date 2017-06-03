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
RST        = pyb.Pin('X20')
CE         = pyb.Pin('X19')
DC         = pyb.Pin('X18')
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
Message='TPYBoard_GPS00000000000001'#输入你想要发送的短信的内容；
number='目的号码'#输入想要发送的手机号
w=0
r=0
while r<1:
    u2.write('AT+CMGF=1\r\n')
    pyb.delay(50)
    if(u2.any()>0):
        _dataRead=u2.readall()
        print('1:',_dataRead)
        lcd_5110.lcd_write_string('Message:',0,0)
        lcd_5110.lcd_write_string(str(Message),0,2)
        if(_dataRead==b'AT+CMGF=1\r\n\r\nOK\r\n'):
            u2.write('AT+CSCS="GB2312"\r\n')
            pyb.delay(50)
            if(u2.any()>0):
                _dataRead=u2.readall()
                print('2:',_dataRead)
                if(_dataRead==b'AT+CSCS="GB2312"\r\n\r\nOK\r\n'):
                    u2.write('AT+CNMI=2,1\r\n')
                    pyb.delay(50)
                    if(u2.any()>0):
                        _dataRead=u2.readall()
                        print('3:',_dataRead)
                        if(_dataRead==b'AT+CNMI=2,1\r\n\r\nOK\r\n'):
                            u2.write('AT+CMGS="'+number+'"\r\n')
                            pyb.delay(50)
                            if(u2.any()>0):
                                _dataRead=u2.readall()
                                print('4:',_dataRead)#b'AT+CMGF=1\r\n\r\nOK\r\n'
                                if(_dataRead== b'AT+CMGS="'+number+'"\r\n\r\n> '):
                                    u2.write(Message+'\r\n')#短信内容
                                    pyb.delay(50)
                                    if(u2.any()>0):
                                        _dataRead=u2.readall()
                                        print('5:',_dataRead)
                                        print(len(_dataRead))
                                        w=len(_dataRead)
                                        _dataRead=str(_dataRead)[2:w]
                                        print('6:',_dataRead)
                                        if(_dataRead==Message):
                                            print('7:ok')
                                            lcd_5110.lcd_write_string('Has been sent',0,5)
                                            r=10