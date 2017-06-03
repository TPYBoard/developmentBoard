import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
from ubinascii import hexlify
from ubinascii import *#以上为声明使用到的类库


leds = [pyb.LED(i) for i in range(1,5)]
P,L,SHUCHU=0,0,0
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST        = pyb.Pin('X20')
CE         = pyb.Pin('X19')
DC         = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
#以上为初始化显示屏的函数，虽然这次没有用到显示，但是备用
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
count_=0
N2 = Pin('Y3', Pin.OUT_PP)
N1 = Pin('Y6', Pin.OUT_PP)#定义通信系统启动引脚
N1.low()
pyb.delay(2000)
N1.high()
pyb.delay(10000)#拉高拉低引脚，启动通信系统
u2 = UART(4, 115200)#定义串口4，设置 波特率为115200
K=5#设置一个选择变量K
while (K==5):#这个循环是为了设置通信区域模式为透传模式。
    u2.write('AT+CIPMODE=1\r\n')
    pyb.delay(500)
    if(u2.any()>0):
        print('透传')
        _dataRead=u2.readall()
        print('透传',_dataRead.decode('utf-8'))
        if(_dataRead.find(b'OK')>-1):
            K=0
            pyb.delay(20)
#这个语句是为了搭建通信连接
u2.write('AT+CIPSTART="TCP","139.196.109.178",30000\r\n')
pyb.delay(10000)
print('123')
#这里是为了判断通信连接是否已经建立起来，如果没有建立起来通信的连接，则等待。
while (K==0):
    pyb.delay(3000)
    if(u2.any()>0):
        _dataRead=u2.readall()
        print('oo',_dataRead)
        #这个判断是为了判断是否已经和服务器建立起连接来
        if(_dataRead.find(b'CONNECT OK')>-1):
            #开发板已经和服务器建立起连接来，则改变选择变量的值，使其进入下一个循环
            K=1
            pyb.LED(1).on()
#这个循环是执行数据传输命令的执行所在，在这个循环中进行各种数据的裁剪拼接和发送。
while (K==1):
    print('DOU')
    #u2.write('+++')  此时整个系统进入透传通信模式，想要退出，则发送‘+++’，即可        #退出；
    #u2.write('ATO0') 想让系统从指令模式进入透传模式，则发送‘ATO0’,则进入透传；
    #pyb.delay(1500)
    pyb.LED(2).off()
    pyb.LED(3).off()
    pyb.LED(2).on()
    u2.write('TPGPS,1234567890abcde,36.67191670,119.17200000,201701120825,25,50,END')
    #这个报文详细格式参照服务平台示例报文格式。
    #把这格式里面的经纬度数据换成从定位系统获取到的经纬度，就可以实时定位了。
    pyb.delay(13000)#延时一下时间，官方提供的测试平台有上传频率限制
    if(u2.any()>0):
#这个返回仅适用于官方提供的服务平台
        _dataRead=u2.readall()
        print('1212',_dataRead)
    pyb.LED(3).on()
    pyb.delay(10000)