#!/usr/bin/env python3

## Imports all Objects and Methods from the motor module
from ev3dev2.motor import *

## Sets mt Equal to the MoveTank of two motors allowing
## them to run concurrently
mt = MoveTank(OUTPUT_A,OUTPUT_B)

# Run Motor 1 at 50% max speed and Run Motor 2 at 50% Max Speed for 5 seconds
mt.on_for_seconds(SpeedPercent(50),SpeedPercent(50),5)