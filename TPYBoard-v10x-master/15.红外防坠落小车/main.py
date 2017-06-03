import pyb
from pyb import UART
from pyb import Pin

M0 = Pin('X1', Pin.IN)
M1 = Pin('X2', Pin.IN)
M2 = Pin('X3', Pin.IN)
M3 = Pin('X4', Pin.IN)
N1 = Pin('Y1', Pin.OUT_PP)
N2 = Pin('Y2', Pin.OUT_PP)
N3 = Pin('Y3', Pin.OUT_PP)
N4 = Pin('Y4', Pin.OUT_PP)

print('while')
while True:
    print('while')
    if(M2.value()|M1.value()|M3.value()|M0.value()==0):
        N1.low()
        N2.high()
        N4.high()
        N3.low()
        pyb.LED(2).on()
        pyb.LED(3).off()
    elif(M2.value()|M1.value()|M3.value()|M0.value()==1):
        N1.high()
        N2.low()
        N4.low()
        N3.high()
        pyb.delay(300)
        N1.low()
        N2.high()
        N3.high()
        N4.low()
        pyb.delay(200)
        pyb.LED(3).on()
        pyb.LED(2).off()