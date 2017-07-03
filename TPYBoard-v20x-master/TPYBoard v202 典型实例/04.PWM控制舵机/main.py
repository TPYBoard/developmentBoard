import machine
import time

#设置PWM 引脚G5,频率50Hz
servo = machine.PWM(machine.Pin(5), freq=50)

servo.duty(40)#舵机角度的设定
time.sleep(2)#延时2秒
servo.duty(115)
time.sleep(2)
servo.duty(180)