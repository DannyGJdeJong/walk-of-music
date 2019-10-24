import RPi.GPIO as GPIO
import time
import os

STEP_PINS = [6, 13, 19, 26]
GENRES = ["Rock"]
GENRE_PINS = []

GPIO.setmode(GPIO.BCM)

for pin in STEP_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

import pygame
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 1024)

s1 = pygame.mixer.Sound("../audio/test.ogg")
s1.set_volume(100)
s1 = pygame.mixer.Sound("../audio/test.ogg")
s1.set_volume(100)

audiopath = "../audio"

songs = []
for i in range(4):
    s = pygame.mixer.Sound(os.path.join(audiopath, str(i) + ".mp3"))
    s.set_volume(100)
    songs.append(s)
c = pygame.mixer.Channel(0)

while True:
    # if GPIO.input(26):
    #     c.play(s)
    #     while c.get_busy() == True:
    #         continue
    for i in range(len(STEP_PINS)):
        if GPIO.input(STEP_PINS[i]):
            c.play(songs[i])
            while c.get_busy() == True:
                continue

# pygame.mixer.pre_init(44100, -16, 1, 512)
# pygame.mixer.music.load("../audio/test.ogg")
# pygame.mixer.music.set_volume(100)

# while True:
#     if GPIO.input(26):
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy() == True:
#             continue

GPIO.cleanup() 