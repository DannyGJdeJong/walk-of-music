import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

i = 0

while True:
    if GPIO.input(26):
        i = i + 1
        print(i)

GPIO.cleanup() 