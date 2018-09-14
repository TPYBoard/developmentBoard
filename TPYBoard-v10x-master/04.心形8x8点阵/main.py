# main.py -- put your code here!
import  pyb
from pyb import Pin
x_row = [Pin(i, Pin.OUT_PP) for i in ['X1','X2','X3','X4','X5','X6','X7','X8']]
y_col = [Pin(i, Pin.OUT_PP) for i in ['Y1','Y2','Y3','Y4','Y5','Y6','Y7','Y8']]
tuxing = [
#大心
['11111111','10011001','00000000','00000000','10000001','11000011','11100111','11111111'],
#小心
['11111111','11111111','10011001','10000001','11000011','11100111','11111111','11111111']
]
def displayLED(num):
    for i,j in enumerate(x_row):
        x_row[i-1].value(0)
        data = tuxing[num][i]
        for k,v in enumerate(data):
            y_col[k].value(int(v))
        j.value(1)
        pyb.delay(1)

while True:
    for i in range(2):
        for k in range(100):
            displayLED(i)