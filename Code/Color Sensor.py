#Color Sensor
#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
import time 
import math
from ev3dev2.display import Display


disp = Display()
color_sensor = ColorSensor(INPUT_1)
color_sensor.calibrate_white()
'''will write each box as a certain code combo: ex. A1 = 1666'''
#COLOR_BLACK = 1
#COLOR_WHITE = 6

barcode_dict = {1:'1666', 2:'1616', 3:'1166', 4:'1661'}
def barcode_reading(barcode_type, near = False):
    color = '0000'
    if near == True:
        for i in range(len(barcode_dict[barcode_type])):
            for k in (1, i):
                if color_sensor == color_sensor.COLOR_BLACK:
                    color = color + str(color_sensor.COLOR_BLACK)
                elif color_sensor == color_sensor.COLOR_WHITE:
                    color = color + str(color_sensor.COLOR_WHITE)
    if color == barcode_dict[barcode_type]:
        return color
    if near == True:
        if barcode_type != color:
            disp.text_pixels(input("This is not the box"),x=0,y=64)
            disp.update()
            time.sleep(5)
        elif barcode_type == color:
            disp.text_pixels("This is the box",x=0,y=64)
            disp.update()
            time.sleep(5)

'''boxtype1=0
boxtype2=0
boxtype3=0
boxtype4=0

if color_sensor.COLOR_BLACK:
    if color_sensor.COLOR_WHITE:
        if color_sensor.COLOR_BLACK:
            if color_sensor.COLOR_BLACK:
                boxtype2=1
        elif color_sensor.COLOR_WHITE:
            if color_sensor.COLOR_WHITE:
                boxtype1=1
            elif color_sensor.COLOR_BLACK:
                boxtype4=1
    elif color_sensor.COLOR_BLACK:
        if color_sensor.COLOR_WHITE:
            if color_sensor.COLOR_WHITE:
                boxtype3=1
'''