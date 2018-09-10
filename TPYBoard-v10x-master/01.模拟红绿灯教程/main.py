import pyb
from pyb import Pin
  
r_LED=Pin('Y1',Pin.OUT_PP)#red
y_LED=Pin('Y2',Pin.OUT_PP)#yellow
g_LED=Pin('Y3',Pin.OUT_PP)#green
  
#数码管a~g对应的开发板引脚X1~X7
d_Pins=[Pin(i,Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7']]
  
number=[
[0,0,0,0,0,0,1],#0
[1,1,1,1,0,0,1],#1
[0,0,1,0,0,1,0],#2
[0,0,0,0,1,1,0],#3
[1,0,0,1,1,0,0],#4
[0,1,0,0,1,0,0],#5
[0,1,0,0,0,0,0],#6
[0,0,0,1,1,1,1],#7
[0,0,0,0,0,0,0],#8
[0,0,0,0,1,0,0],#9
]
  
def display(num):
    global number
    count=0
    for pin in d_Pins:#X1~X7分别设置电平值 动态显示num的值
        pin.value(number[num][count])
        count+=1
  
if __name__=='__main__':
    while True:
        #红灯亮10秒
        r_LED.value(1)
        for i in range(0,10):
            display(9-i)
            pyb.delay(1000)#1s
        r_LED.value(0)
        #黄灯亮3秒
        y_LED.value(1)
        for i in range(0,3):
            display(2-i)
            pyb.delay(1000)#1s
        y_LED.value(0)
        #绿灯亮10秒
        g_LED.value(1)
        for i in range(0,10):
            display(9-i)
            pyb.delay(1000)#1s
        g_LED.value(0)