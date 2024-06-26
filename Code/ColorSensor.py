#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank
import time 
from ev3dev2.display import Display
from PID_movement import *
from ev3dev2.motor import OUTPUT_D, MoveTank, SpeedRPS, MediumMotor, SpeedPercent


disp = Display()
color_sensor = ColorSensor(INPUT_1)
color_sensor.calibrate_white()
'''will write each box as a certain code combo: ex. A1 = 1666'''

def barcode_reading(barcode_type, near = False):
    #COLOR_BLACK = 1
    #COLOR_WHITE = 6
    barcode_dict = {1:'1666', 2:'1616', 3:'1166', 4:'1661'}
    color = ''
    if near == True:
        for i in range(len(barcode_dict[barcode_type])):
            if (color_sensor.reflected_light_intensity <= 15):
                color += str(1)
            elif (color_sensor.reflected_light_intensity >15):
                color += str(6)
            straight(distance_to_time(.75*25.4)) #.75 needs to go back to .5 in but *conversion factor
            time.sleep(0.5)
            print(color)
    if color == barcode_dict[barcode_type]:
        return True
    if near == True:
        if barcode_type != color:
            disp.text_pixels(("This is not the box"),x=0,y=64)
            disp.update()
            time.sleep(5)
        elif barcode_type == color:
            disp.text_pixels("This is the box",x=0,y=64)
            disp.update()
            time.sleep(5)
    return False

if (barcode_reading(3, True)):
    print('barcode_match')
else:
    print('barcode_no_match')

