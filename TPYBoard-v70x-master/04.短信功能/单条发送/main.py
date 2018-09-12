import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
 
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST    = pyb.Pin('X20')
CE     = pyb.Pin('X19')
DC     = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
N1 = Pin('Y6', Pin.OUT_PP)
N1.low()
lcd_5110.lcd_write_string('Getting Ready',0,1)
pyb.delay(2000)
N1.high()
pyb.delay(10000)
u2 = UART(4, 115200,timeout = 100)
Message = 'Hello,I am TPYBoard v702'#输入你想要发送的短信的内容；
number = '1800000000'#输入想要发送的手机号
 
lcd_5110.lcd_write_string('Send Message',0,1)
lcd_5110.lcd_write_string(str(Message),0,2)
u2.write('AT+CMGF=1\r\n')#设置以文本方式发送短信
while True:
    if u2.any() > 0:
        _dataRead = u2.read()
        print('dataRead:',_dataRead)
        if _dataRead.find(b'AT+CMGF=1\r\n\r\nOK\r\n') > -1:
            u2.write('AT+CSCS="GB2312"\r\n')#设置文本编码
            lcd_5110.lcd_write_string('..',0,4)
        elif _dataRead.find(b'AT+CSCS="GB2312"\r\n\r\nOK\r\n') > -1:
            u2.write('AT+CNMI=2,2\r\n')#收到短信直接给出提示
            lcd_5110.lcd_write_string('...',0,4)
        elif _dataRead.find(b'AT+CNMI=2,2\r\n\r\nOK\r\n') > -1:
            u2.write('AT+CMGS="'+number+'"\r\n')#输入对方手机号
            lcd_5110.lcd_write_string('....',0,4)
        elif _dataRead.find(b'AT+CMGS="'+number+'"\r\n\r\n> ') > -1:
            u2.write(Message+'\r\n')#输入短信内容
            lcd_5110.lcd_write_string('.....',0,4)
        elif _dataRead.find(b'\r\n+CMGS') > -1 and _dataRead.find(b'OK') > -1:
            print('Send success')
            lcd_5110.lcd_write_string('Send success!',0,4)
        elif _dataRead.find(b''+Message+'') > -1:
            lcd_5110.lcd_write_string('......',0,4)
        else:
            print('error')