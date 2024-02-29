#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_1
from time import sleep
import math


"""Initialized Constants"""
wheel_diameter_cm = 6.5 
circumference_cm = wheel_diameter_cm * math.pi
degrees_per_cm  = 360 / circumference_cm
base_power = 50
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
gyro = GyroSensor(INPUT_1)

#both need to be here for the gyro sensor to function
gyro.reset()
gyro.calibrate()


def motors_straight(distance_cm, base_power, isReverse = False):
    if isReverse == True:
        base_power = base_power * -1 
    
    degrees_to_move = distance_cm * degrees_per_cm
    
    k = 0.5 #adjust according to tests
    
    desired_angle = 0
    actual_angle = gyro.angle
    error = desired_angle - actual_angle
    adjustment = error * k

    left_power = base_power + adjustment
    right_power = base_power - adjustment

    left_power = max(min(left_power, 100), -100)
    right_power = max(min(right_power, 100), -100)
    
    tank_drive.ramp_down_sp = 500 #controls the decceleration
    tank_drive.on_for_degrees(SpeedPercent(left_power), SpeedPercent(right_power), degrees_to_move)
    
    sleep(0.1)
    

def main():

    
    """User inputs"""
distance_cm = float(input("Enter travel distance (cm) >> "))
num_laps = int(input("Enter number of laps >> "))

for _ in range(num_laps):
    # Drive forward
    motors_straight(distance_cm, base_power)
    # Drive in reverse
    motors_straight(distance_cm, base_power, True)


if __name__ == "__main__":
    main()
