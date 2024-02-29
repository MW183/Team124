'''#!/usr/bin/env python3
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
#gyro = GyroSensor(INPUT_1)
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3EducationSetTire, 6*25.4) #6*25.4 is 6 inches to mm

""" I have no idea if the below block needs to be calling so many functions, 
but the gyro sensor is finicky, so don't touch it"""


distance_cm = float(input("Enter travel distance (cm)  >> "))
num_laps = int(input("Enter number of laps >> "))

#gyro.reset()
#gyro.calibrate()


# for loop for the laps
#
for i in range(num_laps):
    #forward
    mdiff.on_for_distance(SpeedRPM(40), distance_cm*10)
    #backward
    mdiff.on_for_distance(SpeedRPM(40), -distance_cm*10)

sleep(4)
''' 
#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor
from ev3dev2.motor import SpeedPercent, OUTPUT_C
from time import sleep

move_med = MediumMotor(OUTPUT_C)

speed_dps = SpeedPercent(30).percent * move_med.max_speed / 100

move_med.run_timed(time_sp=5000, speed_sp=speed_dps)


move_med.off()


# ls (that is an L)
# cd ./folder
# cd ./next folder
#brickrun -r ./taskfile

#python subTask1a_elise.py
#pip install python-ev3dev2
