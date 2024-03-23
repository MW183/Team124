# Constants
conversion_factor = 1
box_x = 4 * conversion_factor
box_x_gap = 2 * conversion_factor
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
        x_start_box = x_start_shelf + ((box_number - 7) * (box_x + box_x_gap)) + (1 * conversion_factor)
    else:
        x_start_box = x_start_shelf + ((box_number - 1) * (box_x + box_x_gap)) + (1 * conversion_factor)
    
    # The accessible edge y coordinate (bottom or top edge of the box)
    y_edge_box = y_start_shelf + shelf_y if is_on_top(box_number) else y_start_shelf
    print(f"{round(x_start_box, 2)}, {round(y_edge_box, 2)}")
    return x_start_box, y_edge_box


def main():
    rawinput = input("Enter shelf number, box number, barcode, and destination seperated by an underscore (I.E. A1_1, 1, C) >> ")
    split_by_comma = rawinput.split(",")
    split_input_str = [element.strip() for element in split_by_comma]
    
    shelf_and_box = split_by_comma[0]
    barcode = split_by_comma[1]
    destination = split_by_comma[2]
    
    shelf_and_box_lst = shelf_and_box.split("_")
    
    shelf_number = (shelf_and_box_lst[0])
    box_number = int(shelf_and_box_lst[1])
    
    print(f"{shelf_number}, {box_number}, {barcode}, {destination}")
    x_box_start, y_edge = get_box_coordinates(shelf_number, box_number)
    x_box_start = x_box_start - (6*conversion_factor)
    y_edge = y_edge + (6*conversion_factor)
main()