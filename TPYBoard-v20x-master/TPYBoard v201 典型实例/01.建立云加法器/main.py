import pyb
from pyb import UART
from pyb import Pin
from ubinascii import hexlify
from ubinascii import *

ulan = UART(6, 9600)#定义连接网口的串口
K=1
jia=0
jie1=0
he=0
js=0#设置寄存变量
#*******************************主程序**********************************
print('while')
while (K>0):
    _dataRead=ulan.readall()#读取客户端数据
    if _dataRead!=None:#判断客户端是否传来数据
        print(_dataRead)
        js=js+1#计数判断执行命令标志
        if(js==1):
            jia=_dataRead.decode('utf-8')#数据转换
            jia=int(jia)#数据转换
            print(jia)
        if(js==2):
            jia1=_dataRead.decode('utf-8')
            jia1=int(jia1)
            print(jia1)
        if(js==2):
            he=jia+jia1
            js=0
            ulan.write(str(jia)+'+'+str(jia1)+'='+str(he)+'\r\n')#计算结果返回给客户端