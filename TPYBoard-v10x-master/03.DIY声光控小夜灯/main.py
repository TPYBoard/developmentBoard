# main.py -- put your code here!
import pyb
from pyb import Pin

voice = Pin('Y1',Pin.IN)
light = Pin('Y2',Pin.IN)
led = pyb.Pin("X1",pyb.Pin.OUT_PP)
print('start')
print('guang',light.value())
while 1:
    if light.value()==1:
        if voice.value()==1:
            led.value(0)
            pyb.LED(2).off()
            pyb.LED(3).off()
            pyb.LED(4).on()     
        else:
            pyb.LED(3).off()
            pyb.LED(4).off()
            led.value(1)
            pyb.LED(2).on()
            pyb.delay(5000)
    else:
        pyb.LED(3).on()
        pyb.LED(2).off()
        pyb.LED(4).off()
        led.value(0)
            