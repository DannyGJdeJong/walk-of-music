import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

i = 0

import pygame
pygame.mixer.init()
pygame.mixer.music.load("../audio/test.mp3")
pygame.mixer.music.set_volume(100)

while True:
    if GPIO.input(26):
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

GPIO.cleanup() 