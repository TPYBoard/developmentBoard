from pyb import *

accel = Accel()
servo = Servo(1)
while True:
    x = accel.x()
    servo.angle(-x*3,300)
    delay(200)