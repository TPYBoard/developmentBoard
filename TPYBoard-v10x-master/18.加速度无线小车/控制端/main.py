import pyb
xlights = (pyb.LED(2), pyb.LED(3))
ylights = (pyb.LED(1), pyb.LED(4))
from pyb import UART
from pyb import Pin
#from ubinascii import hexlify
from ubinascii import *
accel = pyb.Accel()
u2 = UART(2,9600,timeout=100)
i=0
K=1

#*******************************主程序**********************************
print('while')
while (K>0):
    _dataRead=u2.readall()
    if(1>0):
        x = accel.x()
        print("x=")
        print(x)
        if x > 10:
            xlights[0].on()
            xlights[1].off()
            u2.write('\x00\x05\x18YOU')
            print('\x00\x01\x18YOU')
        elif x < -10:
            xlights[1].on()
            xlights[0].off()
            u2.write('\x00\x05\x18ZUO')
            print('\x00\x01\x18ZUO')

        else:
            xlights[0].off()
            xlights[1].off()

        y = accel.y()
        print("y=")
        print(y)
        if y > 15:
            ylights[0].on()
            ylights[1].off()
        elif y < -15:
            ylights[1].on()
            ylights[0].off()
            u2.write('\x00\x05\x18QIAN')
            print('\x00\x01\x18QIAN')
        else:
            ylights[0].off()
            ylights[1].off()

        pyb.delay(10)