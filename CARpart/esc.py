import RPi.GPIO as gpio
#import threading
#import time
#import os

global i	
class ESC(object):
    def __init__(self):
         gpio.setwarnings(False)
         gpio.setmode(gpio.BOARD)
         gpio.setup(13, gpio.OUT)
            
    def on(self):
        self = gpio.PWM(13, 100)
        self.start(0)
        self.ChangeDutyCycle(1.5)
        i=+1
               
    def count(i):
        i=0
        print('i is ' ,i)
        return i

    def off(self):
        self.stop()
        gpio.cleanup()
        
		 
      





