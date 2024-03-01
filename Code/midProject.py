#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor import INPUT_1
from time import sleep
def main():
    
    mdiff = MoveDifferential(OUTPUT_B, OUTPUT_A, EV3EducationSetTire, 6.1*25.4)
    mdiff.gyro = GyroSensor(INPUT_1)
    distance_in2 = int(input("Enter the number of inches >> "))

    mdiff.gyro.reset()
    mdiff.gyro.calibrate()

    distance_in = 12
    distance_mm1 = distance_in * 25.4 
    
    distance_mm2 = distance_in2 * 25.4
    speed = 30
    degrees_to_turn = 90 * 0.88 #adjustment factor



    # MOVEDIFFERENTIAL.on_for_distance(SPEED, DISTANCE_MM, BRAKE)
    # MOVEDIFFERENTIAL.turn_degrees(speed, degrees, brake, error, gyro)
    mdiff.on_for_distance(speed, distance_mm1)
    mdiff.turn_left(speed * 0.7, degrees_to_turn)
    mdiff.on_for_distance(speed, distance_mm2)
    #drift is 5-10% -Y
    #drift is <1% -X
main()