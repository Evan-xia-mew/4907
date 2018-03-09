# -*- coding: utf-8 -*
import RPi.GPIO as gpio
import time

class ESC(object):
    def __init__(self):
        gpio.setmode(gpio.BOARD)
        motor_pin=13
        gpio.setup(motor_pin,gpio.OUT)
        self.pwm=gpio.PWM(motor_pin,50)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(10)
        print('high set')
        self.pwm.ChangeDutyCycle(5)
        print('low set')

    def on(self):
        global i
        #float(i)
        i=5
        print(i)

    def add(self):
        #global i
        while 1:
            self.pwm.ChangeDutyCycle(6)
            time.sleep(0.05)
        #i+=0.1
        #if i<10:
        #    self.ChangeDutyCycle(i) 
	#    time.sleep(0.3)
        #    print(i)
        #else:
        #    i-=0.1
        #    self.ChangeDutyCycle(i) 
	#    time.sleep(0.3)
        #    print(i)

    def dec(self):
        while 1:
            self.pwm.ChangeDutyCycle(6)
            time.sleep(0.05)
        #global i
        #i-=0.1
        #if i>5:
        #    self.ChangeDutyCycle(i) 
	#    time.sleep(0.3)
        #    print(i)
        #else:
        #    i+=0.1
        #    self.ChangeDutyCycle(i) 
	#    time.sleep(0.3)
        #    print(i)

    def off(self):
        self.pwm.stop()
        gpio.cleanup()
      
     
