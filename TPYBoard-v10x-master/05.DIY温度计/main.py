import pyb
from pyb import Pin
from ds18x20 import DS18X20
from pyb import Timer

x_PIN = [Pin(i, Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7','X8']]
y_PIN = [Pin(i, Pin.OUT_PP) for i in ['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8']]
temp=['0000,0110,0110,0110,0110,0110,0110,0000','1101,1101,1101,1101,1101,1101,1101,1101',
'0000,1110,1110,0000,0111,0111,0111,0000','0000,1110,1110,0000,1110,1110,1110,0000',
'0101,0101,0101,0000,1101,1101,1101,1101','0000,0111,0111,0000,1110,1110,1110,0000',
'0000,0111,0111,0000,0110,0110,0110,0000','0000,1110,1110,1110,1110,1110,1110,1110',
'0000,0110,0110,0000,0110,0110,0110,0000','0000,0110,0110,0000,1110,1110,1110,0000']
tempValue=0
def show(l_num,r_num):
    flag=0
    for x_ in range(0,8):
        for x_ in range(0,8):
            if x_!=flag:
                x_PIN[x_].value(0)
        left_ = temp[l_num]
        left_item=left_.split(',')
        right_ = temp[r_num]
        right_item=right_.split(',')
        li_l=left_item[flag]
        li_r=right_item[flag]
        y_PIN[0].value(int(li_l[:1]))
        y_PIN[1].value(int(li_l[1:2]))
        y_PIN[2].value(int(li_l[2:3]))
        y_PIN[3].value(int(li_l[3:4]))
        y_PIN[4].value(int(li_r[:1]))
        y_PIN[5].value(int(li_r[1:2]))
        y_PIN[6].value(int(li_r[2:3]))
        y_PIN[7].value(int(li_r[3:4]))
        x_PIN[flag].value(1)
        flag=flag+1
        pyb.delay(2)
def display(time_,l_num,r_num):
    for x in range(0,time_):
        for y in range(0,110):
            show(l_num,r_num)
if __name__=='__main__':
    #time_t=Timer(4,freq=5,callback=randSensor)
    DQ=DS18X20(Pin('Y10'))#DQ
    while 1:
        tempValue =int(DQ.read_temp())
        print(tempValue)
        l_n=tempValue//10
        r_n=tempValue%10
        print(l_n,'-',r_n)
        display(1,l_n,r_n)
        for i in x_PIN:
            i.value(0)