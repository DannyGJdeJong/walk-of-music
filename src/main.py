import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

i = 0

while True:
    if GPIO.input(26):
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("../audio/test.mpeg")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

GPIO.cleanup() 