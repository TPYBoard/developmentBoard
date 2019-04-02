import pyb
from pyb import Pin
from dht11 import DHT11

dht = DHT11('X12')
def readTaHData():
    DATA = dht.read_data()#读取温湿度的值
    print(DATA[0],'℃')
    print(DATA[1],'%')
while True:
    readTaHData()
    
   
   