#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from time import sleep

cl = ColorSensor() 
ts = TouchSensor()

# Stop program by long-pressing touch sensor button
#his program will make the color sensor display RGB colors together

while not ts.is_pressed:
    # rgb is a tuple containing three integers
    # each 0-255 representing the amount of
    # red, green and blue in the reflected light
    print(cl.rgb)
    red = cl.rgb[0]
    green=cl.rgb[1]
    blue=cl.rgb[2]
    print("Red: "+str(red)+", Green: "+str(green)+", Blue: "+str(blue)+'\n')
    # '\n' is the newline character so an extra (blank) line is printed
    sleep(1)