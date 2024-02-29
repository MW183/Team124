#!/usr/bin/env python3

from ev3dev2.sound import Sound

## sets sound at the Sound manager for the brick
sound = Sound()

## sound manager tells the brick to play a beep
sound.beep()

## sound manager tells brick to play .wav file loaded onto brick
## importing .wav file will take time so upload .wav files in a seperate folder to your scripts
sound.play_file("UC_AlmaMater.wav")

