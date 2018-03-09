import RPi.GPIO as gpio
import time

class ESC(object):
    def __init__(self):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD)
        gpio.setup(13,gpio.OUT)
        self.pwm = gpio.PWM(13,50)
        global i
        
    def on(self):
        gpio.setmode(gpio.BOARD)
        gpio.setup(13,gpio.OUT)
        self.pwm = gpio.PWM(13,50)
        global i
        i=6
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(i)
        #time.sleep(0.05)
        print(i)

    def add(self):
        global i
        i+=0.5
        self.pwm.ChangeDutyCycle(i)
        time.sleep(0.05)
        print(i)

    def dec(self):
        global i
        i-=1
        self.pwm.ChangeDutyCycle(i)
        time.sleep(0.05)
        print(i)

        
    def off(self):
        global i
        i=0
        self.pwm.ChangeDutyCycle(i)
        self.pwm.stop()
        gpio.cleanup()
        print(i)
