#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor
import time

## Sets ts to a Touch Sensor located in port 2
ts = TouchSensor(INPUT_2)

while True:
    ## When ts is pressed within 1000ms print the message
    if ts.wait_for_pressed(timeout_ms=1000):
        print("Touch Sensor has been Pressed")
    ## If ts is not pressed within 1000ms print this other message
    else:
        print("Touch Sensor was not pressed in the last 1000ms")
    time.sleep(1)

