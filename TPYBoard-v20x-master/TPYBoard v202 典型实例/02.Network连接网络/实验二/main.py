import network
from machine import Pin
import socket
import urllib
import time

def led_state():
    p2 = Pin(2, Pin.OUT)
    p2.value(0)
    time.sleep_ms(500)
    p2.value(1)
    time.sleep_ms(500)
    p2.value(0)
    time.sleep_ms(500)
    p2.value(1)

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    p2 = Pin(2, Pin.OUT)
    sta_if.active(False)
    if not sta_if.isconnected():
        p2.low()
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('TurnipSmart', 'turnip2016')
        while not sta_if.isconnected():
            pass
    if sta_if.isconnected():
        print('connect success')
        p2.high()
        print('network config:', sta_if.ifconfig())

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(50)
        if data:
            recive=str(data, 'utf8')
            #print('recive:',recive)
            print(str(data, 'utf8'), end='')
            if(recive.find('begin')>-1):
                led_state()
        else:
            break
    s.close()
do_connect()
http_get('http://www.tpyboard.com/esp8266/test.php?val=A')