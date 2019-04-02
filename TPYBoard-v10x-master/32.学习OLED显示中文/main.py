import pyb
from ssd1306_lib import SSD1306
import math
import font
from pyb import Timer

display = SSD1306(pinout={'dc': 'Y9',
                          'res': 'Y10'},
                  height=64,
                  external_vcc=False)

led_red = pyb.LED(2)
led_red.on()
display.poweron()
display.init_display()
display.draw_text(8,8,'TPYBoard OLED Text',)
display.draw_chinese('我爱你祖国',1,3)


display.display()
