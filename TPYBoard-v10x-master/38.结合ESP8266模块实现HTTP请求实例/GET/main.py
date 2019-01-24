from pyb import UART
from pyb import LED

#等待ESP-01模块初始化，忽略启动时的内部信息
pyb.delay(1000)

ESP_UART = UART(4,115200,timeout=100)

def sendToUart(msg):
    ESP_UART.write(msg+'\r\n')

CWMODE_CUR = 'AT+CWMODE_CUR=1'
CWJAP_CUR = 'AT+CWJAP_CUR="TurnipSmart","turnip2016"'
CIPSTART = 'AT+CIPSTART="TCP","183.230.40.33",80'
CIPSEND = 'AT+CIPSEND=%s'

get = """GET /devices/5835707 HTTP/1.1
api-key: xUrvOCDB=iRuS5noq9FsKrvoW=s=
Host:api.heclouds.com\r\n\r\n
"""
if __name__  == '__main__':
    #退出透传
    ESP_UART.write('+++')
    pyb.delay(500)
    sendToUart('AT')
    isConn = 0
    while True:
        if ESP_UART.any()  > 0:
            buf = ESP_UART.read().decode().replace('\r','').replace('\n','').replace(' ','')
            print(buf)
            pyb.delay(200)
            if buf.find('busyp') > -1 or buf.find('ERROR') > -1:
                # AT指令执行失败
                # 结束程序排查原因
                break
            elif buf.find('ATOK') > -1:
                # 说明AT指令执行成功
                #if 'ATOK' in buf:
                # 成功进入AT指令模式
                # 设置WIFI模式
                sendToUart(CWMODE_CUR)
            elif buf.find(CWMODE_CUR) > -1:
                # 设置sta模式成功，连接AP
                sendToUart(CWJAP_CUR)
                LED(1).on()
            elif buf.find(CWJAP_CUR) > -1:
                isConn = 1
            elif buf.find('OK') > -1 and isConn:
                # 连接AP成功
                # 连接TCP Server
                sendToUart(CIPSTART)
                LED(2).on()
                isConn = 0
            elif buf.find('WIFIGOTIP') > -1:
                # 连接AP成功
                # 连接TCP Server
                sendToUart(CIPSTART)
                LED(2).on()
            elif buf.find('CONNECTOK') > -1:
                # 连接TCP Server成功，发送数据
                LED(3).on()
                sendToUart('AT+CIPMODE=1')#透传
            elif buf.find('AT+CIPMODE=1') > -1:
                sendToUart('AT+CIPSEND')#启动传输
            elif buf.find('>') > -1:
                # 发送数据
                sendToUart(get)
                LED(4).on()
            elif buf.find('HTTP') > -1:
                #退出透传
                ESP_UART.write('+++')
                pyb.delay(500)
                break