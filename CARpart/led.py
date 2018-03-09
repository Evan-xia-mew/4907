import RPi.GPIO as gpio
import time

class LED(object):
    def __init__(self):
        gpio.setmode(gpio.BOARD)
        gpio.setup(12, gpio.OUT)
        
    def work(self):
        pwm = gpio.PWM(12, 50)
        pwm.start(0)
        for i in xrange(0, 101, 2):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.03)
