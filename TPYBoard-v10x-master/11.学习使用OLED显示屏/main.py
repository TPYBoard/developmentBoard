import pyb
from ssd1306_lib import SSD1306

# SPI
display = SSD1306(pinout={'dc': 'Y9',
                          'res': 'Y10'},
                  height=64,
                  external_vcc=False)

# I2C connected to Y9, Y10 (I2C bus 2)
# display = SSD1306(pinout={'sda': 'Y10',
#                           'scl': 'Y9'},
#                   height=64,
#                   external_vcc=False)

led_red = pyb.LED(1)
led_red.off()

try:
  display.poweron()
  display.init_display()

  display.draw_text(1,1,'Welcome T TurnipSmart',size=1,space=1)
  display.draw_text(1,10,'Hello MicroPython!',size=1,space=1)
  
  # Write display buffer
  display.display()
  pyb.delay(10000)

  x = 0
  y = 0
  direction_x = True
  direction_y = True


except Exception as ex:
  led_red.on()
  print('Unexpected error: {0}'.format(ex))
  display.poweroff()