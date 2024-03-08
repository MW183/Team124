conversion_factor = 1
def get_box_coordinates(shelf_label, box_number):
    # Constants
    box_x = 6 * conversion_factor
    box_y = 6 * conversion_factor
    shelf_x = 36 * conversion_factor
    shelf_y = 12 * conversion_factor
    shelf_spacing = 12 * conversion_factor
    
    # Determine the quadrant, column, and row from the shelf_label
    quadrant = ord(shelf_label[0]) - ord('A')  # Convert 'A'-'D' to 0-3
    column = quadrant % 2
    
    #store each row
    row_dict = {'A1': 0, 'B1': 0, 'A2': 1, 'B2': 1, 'C1': 2, 'D1': 2, 'C2': 3, 'D2': 3}
    row = row_dict.get(shelf_label, 0)
        
    # Calculate starting x coordinate of the shelf
    x_start_shelf = shelf_spacing + (column * shelf_x + shelf_spacing)
    
    
    # Calculate starting y coordinate of the shelf
    y_start_shelf = shelf_spacing + row * (shelf_y + shelf_spacing)
    
    # Calculate x_start, x_end based on box number
    x_start_box = x_start_shelf + (box_x * (box_number - 1))
    x_end_box = x_start_box + box_x
    
    # The accessible edge y coordinate (bottom or top edge of the box)
    y_edge_box = y_start_shelf if box_number < 7 else y_start_shelf + shelf_y
    print(f"{x_start_box}, {y_edge_box}")
    return x_start_box, x_end_box, y_edge_box

def move_robot_to_box(target_x, target_y, box_number):
    # Initial robot position (bottom left corner of the storage area)
    robot_x = 0
    robot_y = 0
    orientation_degrees = 90
    
    
    distance_error_rate = -0.01 
    turn_error_degrees = -1 

    def calculate_drift(distance):
        return distance * distance_error_rate

    def apply_turn_error(target_orientation):
        return target_orientation + turn_error_degrees
    
    def move_horizontal(target_x):
        nonlocal robot_x
        distance = target_x - robot_x
        drift = calculate_drift(abs(distance))
        adj_target_x = target_x - drift if distance > 0 else target_x + drift
        robot_x = adj_target_x
        
    def move_vertical(target_y):
        nonlocal robot_y
        if box_number > 7:
            target_y += shelf_y
        distance = target_y - robot_y
        drift = calculate_drift(abs(distance))
        adj_target_y = target_y - drift if distance > 0 else target_y + drift
        robot_y = adj_target_y
    
    move_horizontal(target_x)
    orientation_degrees = apply_turn_error(orientation_degrees)
    move_vertical(target_y))
    print(f"{robot_x}, {robot_y}")
userinput = input("Enter a shelf and box number seperated by an underscore (I.E. A1_1) >> ")
splituserinput = userinput.split("_")
shelf_number = (splituserinput[0])
box_number = int(splituserinput[1])
x_start, x_end, y_edge = get_box_coordinates(shelf_number, box_number)
target_x = x_start - 3
target_y = y_edge - 3
move_robot_to_box(target_x, target_y, box_number)

