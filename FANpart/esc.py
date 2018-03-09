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

    def lel6(self):
        self.pwm.ChangeDutyCycle(6)
        time.sleep(0.05)
        print('level 6')
        #global i
        #i+=1
        #if i<10:
            #print(i)
            #print("User Cancelled")
                
        #else:
            #i-=1
            #print(i)
            #while 1:
                #self.pwm.ChangeDutyCycle(i)
                #time.sleep(0.05)
                
                
    def lel7(self):
        self.pwm.ChangeDutyCycle(7)
        time.sleep(0.05)
        print('level 7')
        #global i
        #i-=1
        #if i>5:
            #print(i)
            #while 1:
                #self.pwm.ChangeDutyCycle(i)
                #time.sleep(0.05)
                
        #else:
            #i+=1
            #print(i)
            #while 1:
                #self.pwm.ChangeDutyCycle(i)
                #time.sleep(0.05)

    def lel8(self):
        self.pwm.ChangeDutyCycle(8)
        time.sleep(0.05)
        print('level 8')

    def lel9(self):
        self.pwm.ChangeDutyCycle(9)
        time.sleep(0.05)
        print('level 9')
        
    def off(self):
        print('off')
        self.pwm.ChangeDutyCycle(5)
        self.pwm.stop()
        gpio.cleanup()
