#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.motor import LargeMotor   #we're importing the motor function
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM #we're importing other functions related to speed

lm = LargeMotor()    #defining a large motor

# Connect ultrasonic sensor to any port 1,2 or 3 or 4
us = UltrasonicSensor()
leds = Leds()

leds.all_off() # stop the LEDs flashing (as well as turn them off)

while True:  # runs forever
    if us.distance_centimeters < 40: # to detect objects closer than 40cm 
        lm.on_for_seconds(speed = 50, seconds=5)   #speed represents the percentage of the rated maximum speed of the motor. If you move your hand closer than 40cm to the US sensor the motor spins
    else: #if you move your hand away from the ultrasonic sensor the motor stops whirring.
        lm.off()
        #break    #(uncomment the break word if you dont want the program to run forever)
