# main.py -- put your code here!
from pyb import Servo
while 1:
    s=Servo(1)
    s.angle(30,500)
    pyb.delay(1500)
    s.angle(-30,500)
    pyb.delay(1500)
    s.angle(60,500)
    pyb.delay(1500)
    s.angle(-60,500)
    pyb.delay(1500)
    s.angle(90,500)
    pyb.delay(1500)
    s.angle(-30,500)
    pyb.delay(1500)
    s.angle(135,500)
    pyb.delay(1500)
