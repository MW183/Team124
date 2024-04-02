#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedRPS, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor

# Initialization
tank = MoveTank(OUTPUT_B, OUTPUT_A)  # left, right
tank.gyro = GyroSensor()
tank.gyro.calibrate()

# PID constants
kp = 10.0  # determines aggressiveness in corrections, can cause oscillations
ki = 0.15  # attempts to eliminate drift over time
kd = 3.0  # dampens the system response to oscillations
RPS = 1  # rotations per second

# Constants for measurements
conversion_factor = 25.4  # mm in an inch


# Functions
def is_on_top(box_number):
    return box_number >= 7

def get_box_coordinates(shelf_label, box_number):
    box_x = 4 * conversion_factor
    box_x_gap = 2 * conversion_factor
    box_y = 6 * conversion_factor
    shelf_x = 36 * conversion_factor
    shelf_y = 12 * conversion_factor
    shelf_spacing = 12 * conversion_factor
    row_dict = {'A1': 0, 'B1': 0, 'A2': 1, 'B2': 1, 'C1': 2, 'D1': 2, 'C2': 3, 'D2': 3}
    quadrant = ord(shelf_label[0]) - ord('A')  # Convert 'A'-'D' to 0-3
    column = quadrant % 2
    row = row_dict.get(shelf_label, 0)
    x_start_shelf = shelf_spacing + (column * (shelf_x + shelf_spacing))
    y_start_shelf = shelf_spacing + (row * (shelf_y + shelf_spacing))
    if is_on_top(box_number):
        x_start_box = x_start_shelf + ((box_number - 7) * (box_x + box_x_gap)) + (1 * conversion_factor)
    else:
        x_start_box = x_start_shelf + ((box_number - 1) * (box_x + box_x_gap)) + (1 * conversion_factor)
    y_edge_box = y_start_shelf + shelf_y if is_on_top(box_number) else y_start_shelf
    return [x_start_box, y_edge_box]

def get_end_coordinates(destination):
    if destination == "B":
        return [102 * conversion_factor, -6 * conversion_factor]
    elif destination == "C":
        return [6 * conversion_factor, 114 * conversion_factor]
    elif destination == "D":
        return [102 * conversion_factor, 114 * conversion_factor]

def distance_to_time(distance):
    circumference = 6.92614 * conversion_factor  # Wheel circumference in mm
    rotations = distance / circumference
    time = 1000 * rotations  # Time in ms
    return time

def get_user_input():
    raw_input = input("Enter shelf number, box number, barcode, and destination separated by an underscore (I.E. A1_1, 1, C) >> ")
    split_input = [element.strip() for element in raw_input.split(",")]
    shelf_label, box_number = split_input[0].split("_")
    barcode = split_input[1]
    destination = split_input[2]
    box_number = int(box_number)
    return shelf_label, box_number, barcode, destination

def straight(time):
    tank.gyro.calibrate()
    tank.follow_gyro_angle(kp, ki, kd, speed=SpeedRPS(RPS), target_angle=0, follow_for=follow_for_ms, ms=time)

def turn_left():
    tank.turn_left(SpeedRPS(RPS), 90)

def turn_right():
    tank.turn_right(SpeedRPS(RPS), 90)

def move_robot_to_box(shelf_label, box_number):
    # Calculate target coordinates

    # Calculate distances to move
    start_x, start_y = 6 * conversion_factor, -6 * conversion_factor
    target_x, target_y = get_box_coordinates(shelf_label, box_number)
    current_x, current_y = start_x, start_y
    # Adjustments to account for the robot's dimensions or specific starting orientation could be added here

    # Move in +y direction
    distance_y = target_y - start_y
    if distance_y > 12:
        time_y = distance_to_time(distance_y)
        straight(time_y)
        current_y += distance_y 

    # Turn right to face +x direction
    turn_right()

    # Move in +x direction
    distance_x = target_x - start_x
    time_x = distance_to_time(distance_x)
    straight(time_x)
    current_x = start_x + distance_x

    # Final adjustment
    turn_right() if is_on_top(box_number) else turn_left()
    
    #Here we need to add in something to read the barcode, grab the box, and then turn in the opposite direction so we are oriented facing in the +y direction
    
    return current_x, current_y
def move_box_to_destination(current_x, current_y, destination):
    target_x, target_y = get_end_coordinates(destination)
    distance_x, distance_y = target_x - current_x, target_y - current_y
    time_x = distance_to_time(distance_x)
    time_y = distance_to_time(distance_y)
    if target_x == 6*conversion_factor:
        turn_left()
    elif target_x == 102*conversion_factor: 
        turn_right()
    straight(time_x)
    if target_y == -6*conversion_factor:
        turn_left()
    elif target_y == 102 * conversion_factor:
        turn_right()
    straight(time_y)    
    current_x += distance_x
    current_y += distance_y
    return current_x, current_y

def main():
    shelf_label, box_number, barcode, destination = get_user_input()
    current_x, current_y = move_robot_to_box(shelf_label, box_number)
    move_box_to_destination(current_x, current_y, destination)

main()
