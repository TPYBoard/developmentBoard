import pyb
from pyb import Pin
from pyb import Timer
import upcd8544
from machine import SPI,Pin

Trig = Pin('X2',Pin.OUT_PP)
Echo = Pin('X1',Pin.IN)
num=0
flag=0
run=1
def start(t):
    global flag
    global num
    if(flag==0):
        num=0
    else:
        num=num+1
def stop(t):
    global run
    if(run==0):
        run=1
start1=Timer(1,freq=10000,callback=start)
stop1=Timer(4,freq=2,callback=stop)
while True:
    if(run==1):
        SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
        #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
        #CLK =>SPI(1).SCK  'X6' SPI clock
        RST    = pyb.Pin('Y10')
        CE     = pyb.Pin('Y11')
        DC     = pyb.Pin('Y9')
        LIGHT  = pyb.Pin('Y12')
        lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
        Trig.value(1)
        pyb.udelay(100)
        Trig.value(0)
        while(Echo.value()==0):
            Trig.value(1)
            pyb.udelay(100)
            Trig.value(0)
            flag=0
        if(Echo.value()==1):
            flag=1
            while(Echo.value()==1):           
                flag=1
        if(num!=0):
            #print('num:',num)
            distance=num/10000*34299/2
            print('Distance:')
            print(distance,'cm')
            lcd_5110.lcd_write_string('Distance',0,0)
            lcd_5110.lcd_write_string(str(distance),6,1)
            lcd_5110.lcd_write_string('cm',55,1)
        flag=0
        run=0