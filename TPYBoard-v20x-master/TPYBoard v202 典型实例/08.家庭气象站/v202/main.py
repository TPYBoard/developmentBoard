import machine
import network
import socket
from machine import Pin
from machine import UART
import time
u2=UART(0,115200)#串口初始化
led = Pin(2, Pin.OUT).value(1)#板载小蓝灯 默认关闭
def http_get(temp,hum):
    url='http://old.tpyboard.com/esp8266/SensorTest.php?t='+temp+'&h='+hum+''
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(50)
        if data:
            recive=str(data, 'utf8').upper()
            #print(str(data, 'utf8'), end='')
            if(recive.find('YES')>-1):
               print('Send Data OK')
        else:
            break
    s.close()
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('essid', 'password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()
led = Pin(2, Pin.OUT).value(0)#连接wifi成功 点亮LED
while 1:
    data_=u2.read()
    if data_!=None:
        data_=data_.decode('utf8')#数组转成字符串
        data_a=data_.split(',')#分割
        temp_=str(data_a[0])#温度
        hum_=str(data_a[1])#湿度
        http_get(temp_,hum_)#发送给服务器
    time.sleep(2)