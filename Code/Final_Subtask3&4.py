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
med = MediumMotor(OUTPUT_D)

def motor_control(degrees):
    med.on_for_degrees(SpeedPercent(50), degrees)
    med.wait_while('running')




def straight(distance):
    RPS_factor = 1
    if distance < 0:
        RPS_factor = -1
    circumference = 6.92614   # Wheel circumference in mm
    rotations = abs(distance) / circumference
    time = 1000 * rotations
    
    # PID constants
    kp = 10.0  # determines aggressiveness in corrections, can cause oscillations
    ki = 0.15  # attempts to eliminate drift over time
    kd = 3.0  # dampens the system response to oscillations

    tank.gyro.reset()
    tank.follow_gyro_angle(kp, ki, kd, SpeedRPS(RPS * RPS_factor), target_angle=0, follow_for=follow_for_ms, ms=time)
    
def turn_left():
    tank.turn_left(SpeedRPS(RPS), 90)

def turn_right():
    tank.turn_right(SpeedRPS(RPS), 90)

def turn_around():
    tank.turn_right(SpeedRPS(RPS), 180)

def barcode_reading(barcode_type):
    barcode_dict = {1:'1666', 2:'1616', 3:'1166', 4:'1661'}
    color = ''
    for i in range(1,5):
        straight(distance = -0.75)
        sleep(0.5)
        if (color_sensor.reflected_light_intensity <= 15):
            color += str(1)
        elif (color_sensor.reflected_light_intensity >15):
            color += str(6)
        sleep(0.5)
    print(color)
    
    if barcode_dict[barcode_type] == color:
        print("This is the box")
        disp.text_pixels("This is the box", x=0, y=64)
        disp.update()
        sleep(5)
        return True
    else:
        print("This is not the box")
        disp.text_pixels("This is not the box", x=0, y=64)
        disp.update()
        sleep(3)
        return False

def main():
    barcode = int(input("Enter the corresponding number for the barcode type >> "))
    distance = (17.5 )
    straight(distance)
    barcode_reading(barcode)
    turn_right()
    straight(-1)
    motor_control(-60)
    straight(3)
    sleep(1)
    motor_control(250)
    straight(-2)
    turn_left()
    straight(21 )
    motor_control(-250)    
    straight(-2)
    motor_control(60)
main()
    