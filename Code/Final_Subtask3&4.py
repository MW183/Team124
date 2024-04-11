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

hold_position = True 

def motor_control():
    global hold_position
    med = MediumMotor(OUTPUT_D)
    med.on_for_degrees(SpeedPercent(100), -60)
    med.wait_while('running')
    
    while hold_position:
            med.on(SpeedPerecent(100))
    
    med.stop()

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
    box_number = 9
    isRight = True
    while True:
        barcode = int(input("Enter the corresponding number for the barcode type >> "))
        if barcode in range(1, 5):
            break
        else:
            print("Wrong input, try again!")
    current_x = (0 * conversion_factor) 
    target_x = (19) * conversion_factor
    
    
    straight(distance= target_x - current_x)
    isSuccess = barcode_reading(barcode, isRight)
    tries = 1
    
    while not (isSuccess) and (tries <= 3):
        straight(distance = 2 * conversion_factor)
        tries += 1
        isSuccess = barcode_reading(barcode, isRight)
        sleep(2)
    if isSuccess:
        turn_right()
        #starting motor control in a seperate thread
        motor_thread = threading.Thread(target = motor_control)
        motor_thread.start()        
        turn_left()
    
    #move to drop-off
    straight(distance = (21 * conversion_factor))
    #execute once box no longer needs to be held
    global hold_position
    hold_position = False
    motor_thread.join()
    
    
    
main()
    