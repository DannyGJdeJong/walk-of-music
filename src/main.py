import RPi.GPIO as GPIO
import pygame
import time
import os

"""
pad 4 only works if 1,2,3 are validated
pad 3 only works if 1,2 are valdated
etc.

when pad 4 is activated reset all pads

every valid pad is activatable mutliple times
"""

STEP_PINS = [6, 13, 19, 26]
GENRES = ["Jazz", "Rock", "Pop", "Disco", "Blues"]
GENRE_PINS = [2, 3, 4, 17, 27]
AUDIOPATH = "../audio"
EXTENSION = ".ogg"

GPIO.setmode(GPIO.BCM)

for pin in STEP_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Init pygame mixer for delay-less audio output
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 1024)

# Load songs
songs = [[]]
for g in range(len(GENRES)):
    ss = []
    for i in range(len(STEP_PINS)):
        s = pygame.mixer.Sound(os.path.join(AUDIOPATH, GENRES[g] + str(i) + EXTENSION))
        s.set_volume(100)
        ss.append(s)
    songs.append(ss)

c = pygame.mixer.Channel(0)

# Set variables to be used between loops
genre = 0

# Enter main loop
while True:
    for g in range(len(GENRE_PINS)):
        if GPIO.input(GENRE_PINS[g]):
            if genre != g:
                # Reset
                genre = g

    for i in range(len(STEP_PINS)):
        if GPIO.input(STEP_PINS[i]):
            c.play(songs[genre][i])
            while c.get_busy() == True:
                continue

# Clean-up after running
GPIO.cleanup() 