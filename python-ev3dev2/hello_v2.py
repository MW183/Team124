#!/usr/bin/env python3
from ev3dev2.display import Display
import time

## Sets disp as the Display
disp = Display()

## Remember to use inputs you must use the SSH shell (type "PythonSampleFiles/HelloWorld.py")
## Writes message 0 pixels from the left of the screen and 64 pixels from the top of the screen
disp.text_pixels(input("Type your message here: "),x=0,y=64)
disp.update()

## Tells script to stop for 10 seconds
time.sleep(10)