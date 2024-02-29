#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor   #we're importing the motor function
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM #we're importing other functions related to speed
from time import sleep

lm = LargeMotor()    #defining a large motor

'''
This will run the large motor at 50% of its
rated maximum speed of 1050 deg/s.
50% x 1050 = 525 deg/s
'''
lm.on_for_seconds(speed = 50, seconds=5)    #speed represents the percentage of the rated maximum speed of the motor. 
sleep(1)

'''
This will run at 500 degrees per second (DPS).
You should be able to hear that the motor runs a
little slower than before.
'''
lm.on_for_seconds(speed=SpeedDPS(500), seconds=3)
sleep(1)

# 36000 degrees per minute (DPM) (rarely useful!)
lm.on_for_seconds(speed=SpeedDPM(36000), seconds=3)
sleep(1)

# 2 rotations per second (RPS)
lm.on_for_seconds(speed=SpeedRPS(2), seconds=3)
sleep(1)

# 100 rotations per minute(RPM)
lm.on_for_seconds(speed=SpeedRPM(100), seconds=3)
