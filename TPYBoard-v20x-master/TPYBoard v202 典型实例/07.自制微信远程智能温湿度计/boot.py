import network
import utime

pdcn = network.WLAN(network.STA_IF)
pdcn.active(True)
pdcn.connect('wifi账号', 'wifi密码')
utime.sleep(5)
if pdcn.isconnected():
    print("WiFi is connected %s."%pdcn.ifconfig()[0])
else:
    pdcn.active(False)
    utime.sleep(5)
    print("WiFi cannot connect.")