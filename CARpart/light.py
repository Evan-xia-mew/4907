import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(12, RPi.GPIO.OUT)

pwm = RPi.GPIO.PWM(12, 50)
pwm.start(0)

try:
     while True:
          for i in range(0, 101, 2):
               pwm.ChangeDutyCycle(i)
               time.sleep(0.03)
               for i in range(100, -1, -2):
                    pwm.ChangeDutyCycle(i)
                    time.sleep(0.03)

except KeyboardInterrupt:
        print("User Cancelled")

pwm.stop()

RPi.GPIO.cleanup()
