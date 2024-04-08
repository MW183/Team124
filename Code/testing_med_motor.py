#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_D, MoveTank, SpeedRPS, MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound
import time

sound = Sound()
sound.beep()

medMotor = MediumMotor(OUTPUT_D)
medMotor.reset()

medMotor.on_to_position(SpeedPercent(100), 0)
time.sleep(5)
medMotor.on_to_position(SpeedPercent(100), 180)
time.sleep(5)
medMotor.on_to_position(SpeedPercent(100), 0)

exit()