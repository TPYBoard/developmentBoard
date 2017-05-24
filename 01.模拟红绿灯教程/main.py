# main.py -- put your code here!
from pyb import Pin

p_out1 = Pin('X1', Pin.OUT_PP)
p_out2 = Pin('X2', Pin.OUT_PP)
p_out3 = Pin('X3', Pin.OUT_PP)


leds = [pyb.LED(i) for i in range(1,5)]
for l in leds:
    l.off()

n = 0
try:
   while True:
      p_out1.high()
      p_out2.low()
      p_out3.low()
      pyb.delay(20000)
      p_out1.low()
      p_out2.low()
      p_out3.high()
      pyb.delay(3000)
      p_out1.low()
      p_out2.high()
      p_out3.low()
      pyb.delay(30000)
      p_out1.low()
      p_out2.low()
      p_out3.high()
      pyb.delay(3000)
    
      n = (n + 1) % 4
      leds[n].toggle()
      pyb.delay(50)

finally:
    for l in leds:
        l.off()
