# Constants
conversion_factor = 1
box_x = 6 * conversion_factor
box_y = 6 * conversion_factor
shelf_x = 36 * conversion_factor
shelf_y = 12 * conversion_factor
shelf_spacing = 12 * conversion_factor
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
        x_start_box = x_start_shelf + ((box_number - 7) * box_x)
    else:
        x_start_box = x_start_shelf + ((box_number - 1) * box_x)
    
    # The accessible edge y coordinate (bottom or top edge of the box)
    y_edge_box = y_start_shelf + shelf_y if is_on_top(box_number) else y_start_shelf
    print(f"{round(x_start_box, 2)}, {round(y_edge_box, 2)}")
    return x_start_box, y_edge_box

def move_robot_to_box(target_x, target_y, box_number):
    #assuming robot is a 6x6 cube starting at (0, 0)
    robot_x = 3
    robot_y = 3
    current_orient = 0 #0 means north
    
    
    error_rate_x = -0.04 * conversion_factor
    error_rate_y = -0.48 * conversion_factor
    turn_error_degrees = -1.15 #negative numbers are to the left in this program

    def calculate_x_drift(distance):
        return distance * error_rate_x
    
    def calculate_y_drift(distance):
        return distance * error_rate_y
    
    def move_horizontal(target_x):
        nonlocal robot_x
        distance = target_x - robot_x
        drift = calculate_x_drift(distance)
        adj_target_x = target_x + drift
        robot_x = adj_target_x
        
    def move_vertical(target_y):
        nonlocal robot_y
        distance = target_y - robot_y
        drift = calculate_y_drift(distance)
        adj_target_y = target_y + drift
        robot_y = adj_target_y
    
    def turn(target_orient):
        nonlocal current_orient
        current_orient = target_orient + turn_error_degrees

    move_vertical(target_y)
    turn(90)
    move_horizontal(target_x)
    turn(0)        
    print(f"{round(robot_x, 2)}, {round(robot_y, 2)}")

def main():

    userinput = input("Enter a shelf and box number seperated by an underscore (I.E. A1_1) >> ")
    splituserinput = userinput.split("_")
    shelf_number = (splituserinput[0])
    box_number = int(splituserinput[1])
    x_box_start, y_edge = get_box_coordinates(shelf_number, box_number)
    target_x = x_box_start
    target_y = y_edge 
    move_robot_to_box(target_x, target_y, box_number)
main()