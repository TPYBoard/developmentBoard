import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
from ubinascii import hexlify
from ubinascii import *#以上内容为声明所使用的类库


leds = [pyb.LED(i) for i in range(1,5)]
P,L,SHUCHU=0,0,0
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST    = pyb.Pin('X20')
CE     = pyb.Pin('X19')
DC     = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)#以上内容为声明并初始化显示屏
count_=0
N2 = Pin('Y3', Pin.OUT_PP)#定义“Y3”为输出模式，这个引脚是控制蜂鸣器的，来电话了需要响铃的
N1 = Pin('Y6', Pin.OUT_PP)#定义“Y6”位输出模式，“Y6”引脚是板载通信系统的开关控制引脚
N1.low()
pyb.delay(2000)
N1.high()
pyb.delay(10000)#通过拉低拉高开光控制引脚，启动通信系统
u2 = UART(4, 115200)#设置串口4，并设置串口波特率为115200
i='0'
w=0
d=0
q=0
G=0
j=0
while 0<1:
    N2.low()#设置蜂鸣器控制引脚为低电平，不让蜂鸣器响
    if(u2.any()>0):#检测串口4是否有数据，如果有数据执行以下
        _dataRead=u2.readall()
        if _dataRead!=None:#判断串口4的数据是否为空，不为空执行以下代码
            print('原始数据=',_dataRead)
            print('原始数据长度:',len(_dataRead))
            print('123',_dataRead[2:6])
            RING=_dataRead[2:6]#截取包头，这个包头是为了判断数据是否正确的重要依据
            print('111',_dataRead[18:29])
            HM=_dataRead[18:29]#数据的18至29位是数据中携带的手机号码，我们把它们保存出来
            WD='No such person'#设置一个变量，这个变量我们可以称为是电话本类比变量
            if(RING==b'RING'):#判断包头正确，执行下面代码
                if(HM==b'18654868920'):#判断来电是否是一个已经存储的号码
                    WD='TPYBoard_GPS'#如果是，显示存储名称,如果没有存储显示'Nosuch person'
                N2.high()#拉高蜂鸣器控制引脚，使蜂鸣器响铃
                lcd_5110.lcd_write_string('Phone Number:',0,0)
                lcd_5110.lcd_write_string(HM.decode("utf8"),2,1)
                lcd_5110.lcd_write_string('The contact:',0,2)
                lcd_5110.lcd_write_string(str(WD),0,3)#显示相应的来电号码，来电人称谓
        pyb.delay(1000)