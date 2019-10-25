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

for pin in GENRE_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Init pygame mixer for delay-less audio output
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 1024)

# Load songs
songs = []
for g in range(len(GENRES)):
    ss = []
    for i in range(len(STEP_PINS)):
        song_path = os.path.join(AUDIOPATH, GENRES[g] + str(i) + EXTENSION)
        if not os.path.exists(song_path):
            continue
        s = pygame.mixer.Sound(song_path)
        s.set_volume(100)
        ss.append(s)
    songs.append(ss)

c = pygame.mixer.Channel(0)

# Set variables to be used between loops
genre = 1
activated = 1

# Enter main loop
while True:
    for g in range(len(GENRE_PINS)):
        if GPIO.input(GENRE_PINS[g]):
            if genre != g:
                reset()
                genre = g

    # Only check activated sensors
    for i in range(activated):
        # Check if sensor is active
        if GPIO.input(STEP_PINS[i]):
            # Activate another sensor if the last one is active
            if i == activated - 1:
                activated = activated + 1
            
            # Reset when last sensor is active
            if i == len(STEP_PINS) - 1:
                reset()

            # Play song associated with the current sensor
            c.play(songs[genre][i])
            while c.get_busy() == True:
                continue

def reset():
    activated = 1

# Clean-up after running
GPIO.cleanup() 