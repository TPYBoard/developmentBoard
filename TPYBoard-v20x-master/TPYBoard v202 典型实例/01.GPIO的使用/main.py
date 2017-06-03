from machine import Pin
import time

p2 = Pin(2, Pin.OUT)    # create output pin on GPIO2
p2.value(1)             # set pin to high

while True:
    p2.low()                # set pin to low
    p2.value()
    time.sleep(3)           # sleep for 3 second
    p2.high()               # set pin to high
    p2.value()
    time.sleep(3)# sleep for 3 second