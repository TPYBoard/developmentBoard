import pyb
from pyb import UART
from pyb import Pin
from ubinascii import hexlify
from ubinascii import *
M1 = Pin('X1', Pin.OUT_PP)
M3 = Pin('Y1', Pin.OUT_PP)
u2 = UART(2, 9600,timeout = 100)
i=0
K=1
#*******************************主程序**********************************
print('while')
while (K>0):
    M1.high()
    pyb.delay(3)
    M3.high()
    if(u2.any()>0):
        print('1234')
        M1.low()
        M3.low()
        pyb.delay(3)
        _dataRead=u2.readall()
        print('123',_dataRead)
        if(_dataRead.find(b'QIAN')>-1):
            M1.low()
            M3.low()
            print('QIAN')
            pyb.delay(250)
        elif(_dataRead.find(b'ZUO')>-1):
            M1.low()
            M3.high()
            print('ZUO')
            pyb.delay(250)
        elif(_dataRead.find(b'YOU')>-1):
            M1.high()
            M3.low()
            print('ZUO')
            pyb.delay(250)