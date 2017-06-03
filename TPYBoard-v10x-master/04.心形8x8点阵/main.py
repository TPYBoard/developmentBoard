# main.py -- put your code here!
import  pyb
from pyb import Pin
#x17 = pyb.Pin("X17",pyb.Pin.IN)
x_PIN = [Pin(i, Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7','X8']]
y_PIN = [Pin(i, Pin.OUT_PP) for i in ['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8']]
hanzi=['11111111','11011101','10001000','10000000','10000000','11000001','11100011','11110111']
def displayLED():
    flag=0
    for x_ in range(0,8):
        for b in range(0,8):
            print(b)
            if b!=flag:
                x_PIN[b].value(0)
        li_l = hanzi[x_]
        y_PIN[0].value(int(li_l[:1]))
        y_PIN[1].value(int(li_l[1:2]))
        y_PIN[2].value(int(li_l[2:3]))
        y_PIN[3].value(int(li_l[3:4]))
        y_PIN[4].value(int(li_l[4:5]))
        y_PIN[5].value(int(li_l[5:6]))
        y_PIN[6].value(int(li_l[6:7]))
        y_PIN[7].value(int(li_l[7:8]))
        x_PIN[flag].value(1)
        flag=flag+1
        pyb.delay(2)
        def displayOFF():
    flag=0
for x_ in range(0,8):
    for b in range(0,8):
        print(b)
        if b!=flag:
            x_PIN[b].value(0)
    li_l = hello[x_]
    y_PIN[0].value(int(li_l[:1]))
    y_PIN[1].value(int(li_l[1:2]))
    y_PIN[2].value(int(li_l[2:3]))
    y_PIN[3].value(int(li_l[3:4]))
    y_PIN[4].value(int(li_l[4:5]))
    y_PIN[5].value(int(li_l[5:6]))
    y_PIN[6].value(int(li_l[6:7]))
    y_PIN[7].value(int(li_l[7:8]))
    x_PIN[flag].value(1)
    flag=flag+1
    pyb.delay(2)
while 1:
    displayLED()

