#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_D, MediumMotor, MoveTank, SpeedRPS, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.display import Display
from time import sleep

# Constants
box_x = 4 
box_x_gap = 2 
box_y = 6 
shelf_x = 36 
shelf_y = 12 
shelf_spacing = 12 
RPS = 1  # rotations per second

# Motor and sensor setup
tank = MoveTank(OUTPUT_B, OUTPUT_A)  # left, right
tank.gyro = GyroSensor()
tank.gyro.calibrate()
color_sensor = ColorSensor()
disp = Display()
med = MediumMotor(OUTPUT_D)
def is_on_top(box_number):
    if box_number >= 7:
        return True
    else: 
        return False

def get_box_coordinates(shelf_label, box_number):
    #store each row
    row_dict = {'A1': 0, 'B1': 0, 'A2': 1, 'B2': 1, 'C1': 2, 'D1': 2, 'C2': 3, 'D2': 3}
    # Determine the quadrant, column, and row from the shelf_label
    quadrant = ord(shelf_label[0]) - ord('A')  # Convert 'A'-'D' to 0-3
    column = quadrant % 2
    row = row_dict.get(shelf_label, 0)
        
    # Calculate starting x coordinate of the shelf
    x_start_shelf = shelf_spacing + (column * (shelf_x + shelf_spacing))
    
    # Calculate starting y coordinate of the shelf
    y_start_shelf = shelf_spacing + (row * (shelf_y + shelf_spacing))
    
    # Calculate x_start, x_end based on box number
    if is_on_top(box_number):
        x_start_box = x_start_shelf + ((box_number - 7) * (box_x + box_x_gap)) + (1 )
    else:
        x_start_box = x_start_shelf + ((box_number - 1) * (box_x + box_x_gap)) + (1 )
    
    # The accessible edge y coordinate (bottom or top edge of the box)
    y_edge_box = y_start_shelf + shelf_y if is_on_top(box_number) else y_start_shelf

    #print(f"{round(x_start_box, 2)}, {round(y_edge_box, 2)}")
    return x_start_box, y_edge_box

def adjust_coordinates(x, y, box_number):
    if is_on_top(box_number):
        return x, (y + (3 )), True
    else:
        return x, (y - (3 )), False
def lift():
    med.on_for_degrees(SpeedPercent(100), 250)
def drop():
    med.on_for_degrees(SpeedPercent(70), -150)
    
def straight(distance):
    RPS_factor = 1 if distance >= 0 else -1
    circumference = 6.92614 
    rotations = abs(distance) / circumference
    time = 1000 * rotations
    kp, ki, kd = 10.0, 0.15, 3.0
    tank.gyro.reset()
    tank.follow_gyro_angle(kp, ki, kd, SpeedRPS(RPS * RPS_factor), target_angle=0, follow_for=follow_for_ms, ms=time)
def turn_left():
    tank.turn_left(SpeedRPS(RPS), 90)

def turn_right():
    tank.turn_right(SpeedRPS(RPS), 90)

def turn_around():
    tank.turn_right(SpeedRPS(RPS), 180)

def barcode_reading(barcode_number):
    barcode_dict = {1: '1666', 2: '1616', 3: '1166', 4: '1661'}
    color = ''
    for _ in range(4):
        straight(-0.75 )
        color += '1' if color_sensor.reflected_light_intensity <= 15 else '6'
        sleep(0.5)
    print(color)
    if barcode_dict[barcode_number] == color:
        disp.text_pixels("This is the box", x=0, y=64)
        disp.update()
        sleep(5)
        return True
    else:
        disp.text_pixels("This is not the box", x=0, y=64)
        disp.update()
        sleep(3)
        return False
def get_destination_coordinates(destination):
    if destination.lower() == 'b':
        return 102, -6
    elif destination.lower() == 'c':
        return 6, 114
    elif destination.lower() == 'd':
        return 102, 114
def handle_box(box_number):
    if is_on_top(box_number):
        turn_right()
    else:
        turn_left()
        
    straight(1)
    sleep(1)
    lift()
    sleep(1)
    
    
    if is_on_top(box_number):
        turn_around()
        
def try_adjustments(barcode, adjustments):
    for adjust in adjustments:
        straight(adjust)
        if barcode_reading(barcode):
            return True
        straight(-adjust)
    return False

def get_user_input():
    rawinput = input("Enter shelf number, box number, barcode, and destination separated by an underscore (I.E. A1_1, 1, C) >> ")
    split_input = [element.strip() for element in rawinput.split(",")]
    shelf_label, box_number = split_input[0].split("_")
    barcode = split_input[1]
    destination = split_input[2]
    box_number = int(box_number)
    return shelf_label, box_number, barcode, destination

def main():
    shelf_label, box_number, barcode, destination = get_user_input()
    target_x, target_y = get_box_coordinates(shelf_label, box_number)
    target_x, target_y = adjust_coordinates(target_x, target_y, box_number)
    start_x = 4 
    start_y = -4 
    distance_x = target_x - start_x
    distance_y = target_y - start_y
    
    straight(distance_y)
    turn_right()
    straight(distance_x)
    
    isSuccess = barcode_reading(barcode)
    if not isSuccess:
        adjustments = [-1.5, 1.5, -1, 1, -0.5, 0.5]
        isSuccess = try_adjustments(barcode, adjustments)
        
    handle_box(box_number)    
    
    final_x, final_y =  get_destination_coordinates(destination)
        
    current_x = target_x
    current_y = target_y + 3 if is_on_top(box_number) else target_y - 3
        
    distance_x = final_x - current_x
    distance_y = final_y - current_y
    
    turn_left() if distance_y >= 0 else turn_right()
    straight(abs(distance_y))
    turn_left() if distance_x >= 0 else turn_right()
    straight(abs(distance_x))
    drop()
    
    start_x = 4
    start_y = -4
    
    current_x = final_x
    current_y = final_y

    #move to start
    
main()