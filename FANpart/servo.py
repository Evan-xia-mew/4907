import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
servoPin=13
gpio.setup(servoPin,gpio.OUT)
pwm=gpio.PWM(servoPin,50)
pwm.start(5)
while (1):
    for i in range(0,180):
        DC=1./18.*(i)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.05)
    for i in range(180,0,-1):
        DC=1/18.*i+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.05)


pwm.ChangeDutyCycle(5)
time.sleep(.03)

pwm.stop()
gpio.cleanup()
