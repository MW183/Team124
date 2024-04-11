#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_D, MediumMotor, MoveTank, SpeedRPS, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.display import Display
import threading
from time import sleep

tank = MoveTank(OUTPUT_B, OUTPUT_A)  # left, right
tank.gyro = GyroSensor()
tank.gyro.calibrate()
color_sensor = ColorSensor()
disp = Display()
RPS = 1  # rotations per second
conversion_factor = 25.4 #mm to in


def motor_control(degrees):
    med = MediumMotor(OUTPUT_D)
    med.on_for_degrees(SpeedPercent(100), degrees)
    med.wait_while('running')


def straight(distance):
    circumference = 6.92614 *conversion_factor  # Wheel circumference in mm
    rotations = distance / circumference
    time = 1000 * rotations
    
    # PID constants
    kp = 10.0  # determines aggressiveness in corrections, can cause oscillations
    ki = 0.15  # attempts to eliminate drift over time
    kd = 3.0  # dampens the system response to oscillations

    tank.gyro.reset()
    tank.follow_gyro_angle(kp, ki, kd, SpeedRPS(RPS), target_angle=0, follow_for=follow_for_ms, ms=time)
    
def turn_left():
    tank.turn_left(SpeedRPS(RPS), 90)

def turn_right():
    tank.turn_right(SpeedRPS(RPS), 90)

def turn_around():
    tank.turn_right(SpeedRPS(RPS), 180)

def barcode_reading(barcode_type, isRight):
    #COLOR_BLACK = 1
    #COLOR_WHITE = 6
    distance_factor = 1    
    if (isRight): 
        distance_factor *= -1
    barcode_dict = {1:'1666', 2:'1616', 3:'1166', 4:'1661'}
    color = ''
    for i in range(len(barcode_dict[barcode_type])):
        straight(distance = ((0.5 * conversion_factor) * distance_factor))
        if (color_sensor.reflected_light_intensity <= 15):
            color += str(1)
        elif (color_sensor.reflected_light_intensity >15):
            color += str(6)
    print(color)
    
    if barcode_dict[barcode_type] == color:
        disp.text_pixels("This is the box", x=0, y=64)
        disp.update()
        sleep(5)
        return True
    else:
        disp.text_pixels("This is not the box", x=0, y=64)
        disp.update()
        sleep(5)
        return False

def main():
    barcode = int(input("Enter the corresponding number for the barcode type >> "))
    distance = 19*conversion_factor
    straight(distance)
    isSuccess = barcode_reading(barcode, isRight = True)
    isSuccess = True
    if isSuccess:
        turn_right()
        sleep(2)
        motor_control(150)
        sleep(2)
        turn_left()
        sleep(2)
    distance = 21 * conversion_factor
    straight(distance)
    motor_control(-150)    
main()
    