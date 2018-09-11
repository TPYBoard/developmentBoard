#main.py
import pyb
import upcd8544
from machine import SPI,Pin
from dht11 import DHT11
def main(lcd_5110,dht,uart6):
    data_=dht.read_data()
    lcd_5110.lcd_write_string(' ',0,1)#添加一个分隔行
    lcd_5110.lcd_write_string('Temp:'+str(data_[0]),2,2)
    lcd_5110.lcd_write_string(' ',0,3)
    lcd_5110.lcd_write_string(' Hum:'+str(data_[1]),2,4)
    uart6.write(str(data_[0])+','+str(data_[1]))#通过串口将数据发送给v202
if __name__ == '__main__':
    #init UART
    u6=pyb.UART(6,115200)
    #init DHT11 
    dht=DHT11('X12')
    #init LCD5110
    SPI    = pyb.SPI(1) 
    RST    = pyb.Pin('Y11')
    CE     = pyb.Pin('Y10')
    DC     = pyb.Pin('Y9')
    LIGHT  = pyb.Pin('X4')
    #DIN=>X8-MOSI/CLK=>X6-SCK
    #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
    #CLK =>SPI(1).SCK  'X6' SPI clock
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    lcd_5110.lcd_write_string('TPYBoard v102',1,0)
    while True:
        main(lcd_5110,dht,u6)
        pyb.delay(2000)