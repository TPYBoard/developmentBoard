# main.py -- put your code here!
import pyb
from pyb import UART
from pyb import Pin

N1 = Pin('X1', Pin.OUT_PP)
N2 = Pin('X2', Pin.OUT_PP)
N3 = Pin('X3', Pin.OUT_PP)
N4 = Pin('X4', Pin.OUT_PP)

M1 = Pin('Y1', Pin.IN)
M2 = Pin('Y2', Pin.IN)
M3 = Pin('Y3', Pin.IN)
M4 = Pin('Y4', Pin.IN)

blue=UART(3,9600)
mode='1'#1:表示蓝牙模式 2:循迹模式

def Stop():
    N1.low()
    N2.low()
    N3.low()
    N4.low()
def Back():
    N1.high()
    N2.low()
    N3.high()
    N4.low()
def Go():
    N1.low()
    N2.high()
    N3.low()
    N4.high()
def Left():
    N1.high()
    N2.low()
    N3.low()
    N4.high()
def Right():
    N1.low()
    N2.high()
    N3.high()
    N4.low()
while True:
    if blue.any()>0:
        data=blue.read().decode()
        print(data)
        if data.find('0')>-1:
            #stop
            Stop()
            mode="1"
            print('stop')
        if data.find('1')>-1:
            Go()
            print('go')
        if data.find('2')>-1:
            Back()
            pyb.delay(500)
            Stop()
        if data.find('3')>-1:
            Left()
            pyb.delay(250)
            Stop()
        if data.find('4')>-1:
            Right()
            pyb.delay(250)
            Stop()
        if data.find('5')>-1:
            mode="1"
            Stop()
        if data.find('6')>-1:
            mode="2"
    else:
        if mode=="2":
            print('循迹模式')
            if(M1.value() and M2.value() and M3.value()):
                Stop()
                mode="1"
            if(M2.value() or M3.value()):
                pyb.LED(2).on()
                pyb.LED(3).off()
                pyb.LED(4).off()
                Go()
            if M1.value():
                pyb.LED(3).on()
                pyb.LED(2).off()
                pyb.LED(4).off()
                Right()
                pyb.delay(10)
            if M4.value():
                pyb.LED(4).on()
                pyb.LED(2).off()
                pyb.LED(3).off()
                Left()
                pyb.delay(10)