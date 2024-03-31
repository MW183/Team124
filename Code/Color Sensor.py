#Color Sensor
#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
from time import sleep
import math

color_sensor = ColorSensor(INPUT_1)
color_sensor.calibrate_white()


def barcode_reading(barcode_type, near = false)
    barcode_dict = (1:'1666', 2:'1616',3:'1166',4:'1661') 
    color = '0000'
    if near == true:
        for i in range(len(color)):
            color[i] = color[i] + color_sensor
            i = i + 1
    if color != '0000' && color == barcode_dict[barcode_type]
        return color
    

#loop??/bool
boxtype1=0
boxtype2=0
boxtype3=0
boxtype4=0

if color_sensor.COLOR_BLACK:
    #move .5 inches
    if color_sensor.COLOR_WHITE:
        # move .5 inches
        if color_sensor.COLOR_BLACK:
            boxtype2=1
        elif color_sensor.COLOR_WHITE:
            #move .5 in
            if color_sensor.COLOR_WHITE:
                boxtype1=1
            elif color_sensor.COLOR_BLACK:
                boxtype4=1
    elif color_sensor.COLOR_BLACK:
        boxtype3=1
else:
    #move like normal?

#i have it so it keeps pausing i think
    
#black = 1, white = 6
def barcode_reading(barcode_type, near = false):
    barcode_dict = {1 : "1666", 2:"1616", 3:"1166", 4:"1661"}
    color = "0000"
    if near == true:
        for i in range(len(color):
            color[i] += color_sensor
            #move forward 0.5in
            i++ 
    if color != "0000" && color == barcode_dict[barcode_type]
        return color