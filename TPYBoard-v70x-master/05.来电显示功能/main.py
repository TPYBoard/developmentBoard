import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
 
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST    = pyb.Pin('X20')
CE     = pyb.Pin('X19')
DC     = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
N2 = Pin('Y3', Pin.OUT_PP)
N1 = Pin('Y6', Pin.OUT_PP)
N1.low()
pyb.delay(2000)
N1.high()
pyb.delay(10000)
u2 = UART(4, 115200,timeout=100)
 
while True:
    N2.low()
    if u2.any()>0:
        _dataRead=u2.read()
        if _dataRead!=None:
            print('原始数据=',_dataRead)
            print('原始数据长度:',len(_dataRead))
            print('123',_dataRead[2:6])
            RING=_dataRead[2:6]
            print('111',_dataRead[18:29])
            HM=_dataRead[18:29]
            if(RING==b'RING'):
                N2.high()
                lcd_5110.lcd_write_string('Phone Number:',0,0)
                lcd_5110.lcd_write_string(HM.decode("utf8"),2,1)
        pyb.delay(1000)