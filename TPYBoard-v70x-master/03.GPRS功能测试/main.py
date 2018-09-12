import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
 
#lcd5110初始化
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST    = pyb.Pin('X20')
CE     = pyb.Pin('X19')
DC     = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
lcd_5110.clear()
lcd_5110.lcd_write_string('Getting Ready',0,1)
#GU620模块初始化
N1 = Pin('Y6', Pin.OUT_PP)#定义通信系统启动引脚
N1.low()
pyb.delay(2000)
N1.high()
pyb.delay(10000)#拉高拉低引脚，启动通信系统
u2 = UART(4,115200,timeout = 100)#定义串口4，设置 波特率为115200
#报文详细格式说明参照萝卜电子服务平台示例报文格式。
#www.turnipsmart.com:8080
message = 'TPGPS,1234567890abcde,36.67191670,119.17200000,201701120825,25,50,END'
if __name__ == '__main__':
    #连接TCP服务器
    u2.write('AT+CIPSTART="TCP","139.196.110.155",30000\r\n')
    while True:
        if u2.any() > 0:
            _dataRead = u2.read()
            print('_dataRead:',_dataRead)
            if _dataRead.find(b'CONNECT OK') > -1:
                #说明已经和服务器成功建立连接
                lcd_5110.lcd_write_string('CONNECT OK',0,2)
                print('CONNECT OK')
                pyb.LED(2).on()
                #发送指令进入透传模式
                u2.write('ATO0\r\n')
            if _dataRead.find(b'ATO0\r\n\r\nOK\r\n') > -1:
                #成功进入透传模式,退出透传模式发送+++,注意前后1秒内不能输入任何字符
                #发送数据给服务器
                u2.write(message)
            if _dataRead.find(b'TPGPSOK') > -1:
                #该数据为服务器返回
                #在向服务器发送了数据后，服务器会对数据进行判断，并返相应的报文
                pyb.LED(3).on()
                lcd_5110.lcd_write_string('SEND OK',0,3)
                break