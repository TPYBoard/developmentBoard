from machine import Timer
import dht
import machine
def f(t):
    d=dht.DHT11(machine.Pin(4))
    d.measure()
    a=d.temperature()
    b=d.humidity()
    print('温度:',a,'°C')
    print('湿度:',b,'%')

tim = Timer(-1)  #新建一个虚拟定时器
tim.init(period=2000, mode=Timer.PERIODIC, callback=f)