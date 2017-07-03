import machine
import time
import network
import usocket
import usocket as socket
    

def WorkMode_STA(essid,pwd):
    sta_mode=network.WLAN(network.STA_IF)#设定工作模式为STA模式
    sta_mode.active(True)#激活接口
    sta_mode.connect(essid,pwd)#essid:WIFI名称  pwd:WIFI密码
    #检测是否连接路由器成功
    while not sta_mode.isconnected():
        pass
    print('IP:', sta_mode.ifconfig()[0])#打印IP地址
    #ifconfig() (ip, subnet, gateway, dns)
    return sta_mode.ifconfig()[0]
def WorkMode_AP(essid,pwd):
    ap_mode=network.WLAN(network.AP_IF)#设定工作模式为AP模式
    ap_mode.active(True)#激活接口
    ap_mode.config(essid,pwd)#设置WIFI热点,essid:WIFI名称  pwd:WIFI密码
    print('IP:', ap_mode.ifconfig()[0])#打印IP地址
    return ap_mode.ifconfig()[0]
def StartServer(ip_):
    s = socket.socket()#创建TCPSocket服务
    ai = socket.getaddrinfo(ip_,8989)#获取IP地址和端口
    addr = ai[0][-1]
    print('Server:',addr)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)#绑定地址
    s.listen(5)#监听最大客户端数5个
    while True:
        res = s.accept()#接收请求
        client_s = res[0]
        client_addr = res[1]
        print('addr:',client_addr)#打印客户端地址
        req =client_s.recv(1024)#读取数据
        req=req.decode('utf-8')#字节数组转字符串
        print('reviceData:',req)
        try:
            val_=int(req)
            servo.duty(val_)#舵机角度的设定
            client_s.send('ok')
            client_s.close()
        except:
            client_s.send('no')
            client_s.close()
if __name__ =="__main__":
    #设置PWM 引脚G5,频率50Hz
    servo = machine.PWM(machine.Pin(5), freq=50)
    myip=WorkMode_STA('essid','pwd')
    #myip=WorkMode_AP('TPYBoard v202','12345678')
    StartServer(myip)