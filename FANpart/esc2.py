import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

motor_pin=13
gpio.setup(motor_pin,gpio.OUT)

motor=gpio.PWM(motor_pin,50)

motor.start(0)

motor.ChangeDutyCycle(10)
time.sleep(3)
print('high is finish')


motor.ChangeDutyCycle(5)
print('low is finish')
time.sleep(6)

while 1:
    motor.ChangeDutyCycle(6)
    time.sleep(0.05)
#for dc in range(20,40,1):
#    motor.ChangeDutyCycle(dc)
#    print('dc:'+str(dc))
#    time.sleep(0.5)


    

    
motor.stop()
