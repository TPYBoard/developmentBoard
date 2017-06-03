#main.py
import pyb
from pyb import Pin
from ds18x20 import DS18X20

Pin("Y9",Pin.OUT_PP).high()#VCC
Pin("Y11",Pin.OUT_PP).low()#GND
x1 = Pin('X1', Pin.OUT_PP)
pyb.delay(100)
DQ=DS18X20(Pin('Y10'))#DQ
while 1:
    tem = DQ.read_temp()
    if tem > 18:
        x1.value(1)
    else:
        x1.value(0)