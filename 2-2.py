import RPi.GPIO as GPIO
import time
import random
dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [1, 1, 1, 1, 1, 1, 1, 1] 
for a in range(8):
    number [a] = random.randint (0, 1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
for a in range(8):
    GPIO.output(dac[a], number[a])
time.sleep(10)
GPIO.output(dac, 0)
GPIO.cleanup()