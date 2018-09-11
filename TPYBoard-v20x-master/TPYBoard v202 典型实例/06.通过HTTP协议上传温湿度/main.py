import dht
import machine
import network
from machine import Pin
import socket
import urllib
import time#声明用到的类库，尤其是dht的类库

d = dht.DHT11(machine.Pin(5))#声明用到类库中的函数，并设置参数
led = Pin(2, Pin.OUT)
count=0
def http_get(url):#定义数据上传的函数
    _, _, host, path = url.split('/', 3)#分割传进来的参数
    addr = socket.getaddrinfo(host, 80)[0][-1]#把传进来的参数处理成符合格式的地址
    s = socket.socket()
    s.connect(addr)#链接地址
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))#向链接的地址发送数据
    while True:#开始数据发送
        data = s.recv(50)
        if data:#数据未发送完成，继续发送
            recive=str(data, 'utf8').upper()
            #print(str(data, 'utf8'), end='')
            if(recive.find('YES')>-1):
                print('Send Data OK')
        else:#数据发送完成，退出while
            break
    s.close()#关闭数据连接
def do_connect():#定义开发板连接无线网络的函数
    wlan = network.WLAN(network.STA_IF)#设置开发板的网#络模式
    wlan.active(True)#打开网络连接
    if not wlan.isconnected():#判断是否有网络连接
        print('connecting to network...')
        wlan.connect('无线名称', '密码')#设置想要连接的无线名称和密码
        while not wlan.isconnected():#等待连接上无线网络
            pass
    print('network config:', wlan.ifconfig())

do_connect()#调用一次开发板连接无线网络的函数
while True:#开始整个代码的大循环
    d.measure()#调用DHT类库中测量数据的函数
    temp_=str(d.temperature())#读取measure()函数中的温度数据
    hum_=str(d.humidity())#读取measure()函数中的湿度数据
    count+=1#计数变量+1
    print('eg:',temp_,'-',hum_)
    http_get('http://www.tpyboard.com/esp8266/SensorTest.php?t='+temp_+'&h='+hum_+'')
    #调用数据上传函数，把最新测量得到的数据进行上传
    print('Count:',count)
    time.sleep(5)