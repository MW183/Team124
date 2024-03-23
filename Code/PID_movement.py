#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor import INPUT_1
from time import sleep

def main():
    conversion_factor = 25.4
    kp = 10.0
    ki = 0
    kd = 3.0
    basespeed = 50
    target_angle = 0
    mdiff = MoveDifferential(OUTPUT_B, OUTPUT_A, EV3EducationSetTire, 6.1*25.4)
    mdiff.gyro = GyroSensor(INPUT_1)
    distance = float(input("Enter the distance in inches >> "))
    distance = distance * conversion_factor
    for _ in distance:
        mdiff.follow_gyro_angle(kp, ki, kd, basespeed, target_angle, sleep_time = 0.01 ) #sleep_time is in seconds
main()