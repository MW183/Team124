#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedRPS, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor

# Instantiate the MoveTank object
tank = MoveTank(OUTPUT_B, OUTPUT_A) #left, right
# Initialize the tank's gyro sensor
tank.gyro = GyroSensor()
# Calibrate the gyro to eliminate drift, and to initialize the current angle as 0
tank.gyro.calibrate()

kp = 10.0 #determines aggressiveness in corrections, can cause oscillations
ki = 0.15  #attempts to eliminate drift over time
kd = 3.0 #dampens the system response to oscillations
RPS = 1

def distance_to_time(distance_inches):
    distance_mm = 25.4 * distance_inches #mm
    circumference = 175.924 #mm / rotation
    rotations = distance_mm / circumference 
    time = 1000 * rotations
    return time


def straight(time):
    tank.gyro.calibrate
    tank.follow_gyro_angle(kp, ki, kd, speed=SpeedRPS(RPS), target_angle=0, follow_for=follow_for_ms, ms= time)

def turn_left():
    tank.turn_left(SpeedRPS(RPS), 90)
def turn_right():
    tank.turn_right(SpeedRPS(RPS), 90)
    
    
def main():
    distance_inches = int(input("Enter the distance in inches >> "))
    time = distance_to_time(distance_inches)
    straight(time)
main()