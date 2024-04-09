#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_D, MoveTank, SpeedRPS, MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound
import time
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedRPS, follow_for_ms

from PID_movement import straight, distance_to_time


def med(sec):
    sound = Sound()
    sound.beep()

    medMotor = MediumMotor(OUTPUT_D)
    medMotor.reset()

    tank = MoveTank(OUTPUT_B, OUTPUT_A)  # left, right
    tank.gyro = GyroSensor()
    tank.gyro.calibrate()

    #medMotor.on_to_position(SpeedPercent(100), 0)
    #time.sleep(5)

    #straight(distance_to_time(25.4))

    medMotor.on_to_position(SpeedPercent(40), -40)
    time.sleep(2)
    tank.on_for_seconds(SpeedPercent(20), SpeedPercent(20), .5)
    medMotor.on_to_position(SpeedPercent(40), 200)
    time.sleep(sec)
duration = input('How long should it hold up the box')

med(duration)
