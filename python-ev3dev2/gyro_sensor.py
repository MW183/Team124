#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor, GyroSensor
from ev3dev2.sound import Sound
from time import sleep

# Connect gyro and touch sensors to any sensor ports
gy = GyroSensor() 
ts = TouchSensor()
sound = Sound()

# Stop program by long-pressing touch sensor button
while not ts.is_pressed:
    angle = gy.angle
    print(str(angle) + ' degrees')  #this will print out the degrees of rotaion of the gyro sensor on the ev3 brick display screen
    sound.play_tone(1000+angle*10, 1) #it will also play a tone 
    sleep(0.5)
