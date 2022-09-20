import RPi.GPIO as GPIO
import time
leds = [21, 20, 16, 12, 7, 8, 25, 24]
number = [1, 1, 0, 0, 1, 0, 1, 0] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
for a in leds:
    GPIO.output(a, 1)
    time.sleep(0.2)
    GPIO.output(a, 0)
GPIO.output(leds, 0)
GPIO.cleanup()