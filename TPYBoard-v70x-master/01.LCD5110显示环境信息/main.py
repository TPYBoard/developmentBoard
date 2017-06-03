# main.py -- put your code here!
#main.py
import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
from ubinascii import hexlify
from ubinascii import *
from SHT20 import SHT20


ds=SHT20(1)
leds = [pyb.LED(i) for i in range(1,5)]
P,L,SHUCHU=0,0,0
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST    = pyb.Pin('X20')
CE     = pyb.Pin('X19')
DC     = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
count_=0
N2 = Pin('Y3', Pin.OUT_PP)
N1 = Pin('Y6', Pin.OUT_PP)
N1.low()
pyb.delay(2000)
N1.high()
while True:
    ads = pyb.ADC(Pin('Y12'))
    a=ads.read()
    a=a/100
    a=33-a
    print("a=",a)
    H=ds.TEMP()
    S=ds.TEMP1()
    H=125*H/256-6
    S=175.72*S/256-46.85
    if(a<10):
        N2.high()
    lcd_5110.lcd_write_string('WENDU:',0,0)
    lcd_5110.lcd_write_string(str(S),0,1)
    lcd_5110.lcd_write_string('SHIDU:',0,2)
    lcd_5110.lcd_write_string(str(H),0,3)
    lcd_5110.lcd_write_string('LIANGDU:',0,4)
    lcd_5110.lcd_write_string(str(a),0,5)
    N2.low()
