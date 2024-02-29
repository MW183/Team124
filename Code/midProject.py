#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor import INPUT_1
from time import sleep

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3EducationSetTire, 5.98*25.4) #6*25 is slightly less that 6 inches into mm (less so drift decreases)
mdiff.gyro = GyroSensor(INPUT_1)


mdiff.gyro.reset()
mdiff.gyro.calibrate()

distance_cm = float(input("Distance (cm) >>"))
distance_mm = distance_cm * 10 
speed = int(input("Speed [-100, 100] >> "))
num_turn = int(input("Turn by 90 >> "))

degrees_to_turn = 90 * num_turn


for i in range(1):
    # MOVEDIFFERENTIAL.on_for_distance(SPEED, DISTANCE_MM, BRAKE)
    # MOVEDIFFERENTIAL.turn_degrees(speed, degrees, brake, error, gyro)
    mdiff.on_for_distance(speed, distance_mm)
   # mdiff.turn_degrees(speed * 0.7, num_turn, error_margin=1, use_gyro=True)
