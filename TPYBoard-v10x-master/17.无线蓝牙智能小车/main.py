import pyb
from pyb import UART
from pyb import Pin

M2 = Pin('X3', Pin.IN)
M3 = Pin('X4', Pin.IN)
N1 = Pin('Y1', Pin.OUT_PP)
N2 = Pin('Y2', Pin.OUT_PP)
N3 = Pin('Y3', Pin.OUT_PP)
N4 = Pin('Y4', Pin.OUT_PP)

u2 = UART(2, 9600,timeout = 100)

while True:
    pyb.LED(2).on()
    pyb.LED(3).on()
    pyb.LED(4).on()
    _dataRead=u2.read()
    if _dataRead!=None:
        #停止
        if(_dataRead.find(b'\xa5Z\x04\xb1\xb5\xaa')>-1):
            print('stop')
            N1.low()
            N2.low()
            N3.low()
            N4.low()
        #向左
        elif(_dataRead.find( b'\xa5Z\x04\xb4\xb8\xaa')>-1):
            print('left')
            N1.low()
            N2.high()
            N3.high()
            N4.low()
        #向右
        elif(_dataRead.find( b'\xa5Z\x04\xb6\xba\xaa')>-1):
            print('right')
            N1.high()
            N2.low()
            N3.low()
            N4.high()
        #后退
        elif(_dataRead.find(b'\xa5Z\x04\xb5\xb9\xaa')>-1):
            print('back')
            N2.high()
            N1.low()
            N4.high()
            N3.low()
        #向前    
        elif(_dataRead.find( b'\xa5Z\x04\xb2\xb6\xaa')>-1):
            print('go')
            N1.high()
            N2.low()
            N3.high()
            N4.low()
