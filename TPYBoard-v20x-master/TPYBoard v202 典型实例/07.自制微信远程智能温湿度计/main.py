import urequests
import dht
import machine
from machine import Pin
import time  
 
class AlarmSystem:
    def __init__(self):
        self.d = dht.DHT11(machine.Pin(5))
 
    def dht11(self):
        try:
            self.d.measure()
            return 'Temp:'+str(self.d.temperature())+'°C---Hum:'+str(self.d.humidity())+'%'
            
        except:
            return '0'
 
    def push(self, result):
        title = "TPYBoardv202提示您:注意天气变化保持健康心情"
        content = 'text='+title+'&'+'desp='+result
        url="https://sc.ftqq.com/你的密钥.send?%s" % content
        r = urequests.get(url)
        r.close()

p2=Pin(2,Pin.OUT)
a = AlarmSystem()

def SendData():
    p2.value(not p2.value())
    data_= a.dht11()
    if(data_!='0'):
        print(data_)
        a.push(data_)
    else:
        print('GET Data Fail')

if __name__ == '__main__':
    
    while True:
        SendData()
        time.sleep(300)
