#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedRPS, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor

from time import sleep

tank = MoveTank(OUTPUT_B, OUTPUT_A)  # left, right
tank.gyro = GyroSensor()
tank.gyro.calibrate()

RPS = 1  # rotations per second

conversion_factor = 25.4 #mm to in


def straight(distance):
    circumference = 6.92614 *conversion_factor  # Wheel circumference in mm
    rotations = distance / circumference
    time = 1000 * rotations
    
    # PID constants
    kp = 10.0  # determines aggressiveness in corrections, can cause oscillations
    ki = 0.15  # attempts to eliminate drift over time
    kd = 3.0  # dampens the system response to oscillations

    tank.gyro.reset()
    tank.follow_gyro_angle(kp, ki, kd, SpeedRPS(RPS), target_angle=0, follow_for=follow_for_ms, ms=time)
    
def turn_left():
    tank.turn_left(SpeedRPS(RPS), 90)
    

def turn_right():
    tank.turn_right(SpeedRPS(RPS), 90)

def turn_around():
    tank.turn_right(SpeedRPS(RPS), 180)
    
def main():
    box_number = int(input("Enter the box number for Shelf A1 >> "))
    target_x = (16 + (6 * (box_number - 7))) * conversion_factor
    target_y = 24 * conversion_factor
    
    current_x = (4 * conversion_factor) 
    current_y = (-4 * conversion_factor)
    
    distance_x = target_x - current_x
    distance_y = target_y - current_y
    
    straight(distance_y)
    turn_right()
    straight(distance_x)
    sleep(5)
'''    
    current_x = target_x
    current_y = target_y
    
    target_x = 102 * conversion_factor
    target_y = -6 * conversion_factor
    
    distance_x = target_x - current_x
    distance_y = target_y - current_y
    
    straight(distance_x)
    turn_right()
    straight(distance_y)
'''
main()
    