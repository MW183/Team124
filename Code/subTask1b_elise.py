#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveDifferential, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor import INPUT_1
from time import sleep
import math


"""Initialized Constants"""
wheel_diameter_cm = 6.5 
circumference_cm = wheel_diameter_cm * math.pi
degrees_per_cm  = 360 / circumference_cm
base_power = 20
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3EducationSetTire, 5.98*25.4) #6*25 is slightly less that 6 inches into mm (less so drift decreases)
mdiff.gyro = GyroSensor(INPUT_1)

""" I have no idea if the below block needs to be calling so many functions, 
but the gyro sensor is finicky, so don't touch it"""


distance_cm = float(input("Enter travel distance (cm)  >> "))
num_laps = int(input("Enter number of laps >> "))

mdiff.gyro.reset()
mdiff.gyro.calibrate()



# for loop for the laps
#

for i in range(num_laps):
    if i == 4:
        error_margin = 2
    ###forward
    mdiff.on_for_distance(SpeedRPM(40), distance_cm*10)
    mdiff.turn_degrees(SpeedRPM(20), 182, error_margin=1, use_gyro=True)
    ###backward
    mdiff.on_for_distance(SpeedRPM(40), distance_cm*10)
    mdiff.turn_degrees(SpeedRPM(20), -182, error_margin=1, use_gyro=True)

# ls (that is an L)
# cd ./folder
# cd ./next folder
#brickrun -r ./taskfile