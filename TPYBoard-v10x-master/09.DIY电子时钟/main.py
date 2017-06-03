# main.py -- put your code here!
import pyb
import upcd8544
from machine import SPI,Pin
from DS3231 import DS3231

ds=DS3231(1)

while True:
    ds.TEMP()
    ds.DATE()
    SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
    #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
    #CLK =>SPI(1).SCK  'X6' SPI clock
    RST    = pyb.Pin('X1')
    CE     = pyb.Pin('X2')
    DC     = pyb.Pin('X3')
    LIGHT  = pyb.Pin('X4')
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    lcd_5110.lcd_write_string('Date',0,0)
    lcd_5110.lcd_write_string(str(ds.DATE()),0,1)
    lcd_5110.lcd_write_string('Time',0,2)
    lcd_5110.lcd_write_string(str(ds.TIME()),0,3)
    lcd_5110.lcd_write_string('Tem',0,4 )
    lcd_5110.lcd_write_string(str(ds.TEMP()),0,5)
    pyb.delay(1000)
    