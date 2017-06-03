# main.py -- put your code here!
import pyb
import upcd8544
from machine import SPI,Pin
from DS3231 import DS3231  

ds=DS3231(1) #定义DS3231

# 用于设定时间和日期
def setDateTime(year,month,day,time,minutes,seconds):
    ds.DATE([year,month,day])
    ds.TIME([time,minutes,seconds])
 
# 在LCD5110 显示时间或日期，separator 中间的分割符
# x，y 在LCD5110 显示的位置 
def showTimeOrDate(why,x,y,separator=':'):
    # [HH,MM,SS] >> HH:MM:SS
    why = why.replace('[','')
    why = why.replace(']','')
    why = why.replace(',',separator)
    print(why)
    lcd_5110.lcd_write_string(why,x,y)


def main():
    lcd_5110.lcd_write_chinese('萝',14,0)
    lcd_5110.lcd_write_chinese('卜',30,0)
    lcd_5110.lcd_write_chinese('智',46,0)
    lcd_5110.lcd_write_chinese('能',62,0)
    lcd_5110.lcd_write_string('TEM:',14,2)
    lcd_5110.lcd_write_string(str(ds.TEMP()),44,2)
    lcd_5110.lcd_write_chinese("当",14,3)
    lcd_5110.lcd_write_chinese("前",30,3)
    lcd_5110.lcd_write_chinese("时",46,3)
    lcd_5110.lcd_write_chinese("间",62,3)
    showTimeOrDate(str(ds.TIME()),14,5)
    print(str(ds.TIME()))
    pyb.delay(1000)

if __name__ == '__main__':
    #setDateTime(2016,12,27,13,17,00)#设置时间
    ds.DATE()
    SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
    #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
    #CLK =>SPI(1).SCK  'X6' SPI clock
    RST    = pyb.Pin('X1')
    CE     = pyb.Pin('X2')
    DC     = pyb.Pin('X3')
    LIGHT  = pyb.Pin('X4')
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    while(1):
     main()
