#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.display import Display
import time

## Sets cs as a color sensor located in port 1
cs = ColorSensor(INPUT_1)

## Sets disp as the display
disp =Display()

while True:
    ## Writes a message containing the reflected light intensity value of cs
    disp.text_pixels(str(cs.reflected_light_intensity),x=0,y=64)

    ## updates the display to show the message
    disp.update()

    ## Tells the system to sleep so CPU does not run constantly
    time.sleep(0.1)