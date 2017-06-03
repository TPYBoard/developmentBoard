import pyb
from pyb import UART
from pyb import Pin
from ubinascii import hexlify
from ubinascii import *
from dht11 import DHT11#定义温湿度传感器的库

ulan = UART(6, 115200)#定义串口，我的网口设置了115200的波特率
K=1
#*******************************主程序**********************************
print('while')
while (K>0):
    #init DHT11 
    dht=DHT11('X8')
    data_=dht.read_data()#读取温湿度的值
    temp=str(data_[0])#温度
    hum=str(data_[1])#湿度
    print('temp:'+temp)
    print('hum:'+hum)
    ulan.write('temperature is:'+temp+'\r\n')#上传温度
    pyb.delay(2000)#做延时是为了让给模拟服务器一个反应时间
    ulan.write('wet is:'+hum+'%'+'\r\n')#上传湿度
    pyb.delay(12000)