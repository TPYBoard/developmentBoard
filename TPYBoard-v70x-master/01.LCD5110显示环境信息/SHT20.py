"""
SHT20 RTC drive
Author: shaoziyang
2016.May

>>> from SHT20 import SHT20

"""

import pyb
from pyb import I2C

SHT20_ADDR       = const(0x40)
SHT20_ADDR1       = const(0xE5)
SHT20_REG_TEMP   = const(0xE3)

class SHT20(object):
    def __init__(self, i2c_num):
        self.i2c = I2C(i2c_num, I2C.MASTER, baudrate = 200000)
    def TEMP(self):
        self.i2c.send(SHT20_ADDR1, SHT20_ADDR)
        t1 = self.i2c.recv(1, SHT20_ADDR)[0]
        return t1
    def TEMP1(self):
        self.i2c.send(SHT20_REG_TEMP, SHT20_ADDR)
        t1 = self.i2c.recv(1, SHT20_ADDR)[0]
        return t1
