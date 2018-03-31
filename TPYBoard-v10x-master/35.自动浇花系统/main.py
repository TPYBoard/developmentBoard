from pyb import Pin, ADC
from ds18x20 import DS18X20

gl = ADC(Pin('Y12'))		#300亮-1700暗
sd = ADC(Pin('Y11'))		#1800干-800湿
wd = DS18X20(Pin('Y10'))
ks = Pin('Y9', Pin.OUT_PP)
jr = Pin('Y8', Pin.OUT_PP)

while True:
	print('\t光照强度:',gl.read(),'\t土壤湿度:',sd.read(),'\t当前温度:',wd.read_temp())
	pyb.delay(200)
	if gl.read()<=250 :		#阳光充足
		if sd.read()>800 :	#多浇水
			ks.value(1)
		else :
			ks.value(0)
	elif  gl.read()>=1300 :	#阳光不足
		if sd.read()>1200 :	#少浇水
			ks.value(1)
		else :
			ks.value(0)
	else :					#阳光一般
		if sd.read()>1000 :	#正常浇水
			ks.value(1)
		else :
			ks.value(0)
	if wd.read_temp()<18 :	#温度过低
		jr.value(1)
	else :
		jr.value(0)