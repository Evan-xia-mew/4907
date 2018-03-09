# -*- coding: utf-8 -*
import RPi.GPIO as gpio
import time

class ESC(object):
    def __init__(self):
        gpio.setmode(gpio.BOARD)
        motor_pin=13
        gpio.setup(motor_pin,gpio.OUT)
        self=gpio.PWM(motor_pin,50)
        self.start(0)
        self.ChangeDutyCycle(10)
        print('high set')
        self.ChangeDutyCycle(5)
        print('low set')

    def on(self):
        global i
        float(i)
        i=5
        print(i)

    def add(self):
        global i
        i=6
        if i<10:
            print(i)
        else:
            print(i)

    def dec(self):
        global i
        i=7
        if i>5:
            print(i)
        else:
            print(i)

    def off(self):
        global i
        i=0
        print(i)
        self.stop()
        gpio.cleanup()
