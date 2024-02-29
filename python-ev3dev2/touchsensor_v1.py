#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from time import sleep

# Connect  touch sensor to port 1
ts = TouchSensor()
leds = Leds()

leds.all_off() # stop the LEDs flashing (as well as turn them off)

while True:  # The loop will run continously when you keep pressing the touch sensor, color changes from red to yellow and back to red and then yellow and so on
    leds.set_color('LEFT', ('RED',  'YELLOW')[ts.is_pressed])
    leds.set_color('RIGHT', ('RED', 'YELLOW')[ts.is_pressed])
    sleep (0.01) # Give the CPU a rest