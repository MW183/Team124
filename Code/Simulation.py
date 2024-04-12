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

def adjust_coordinates(x, y, box_number):
    if is_on_top(box_number):
        return x, (y + (3 * conversion_factor)), True
    else:
        return x, (y - (3 * conversion_factor)), False

def main():
    rawinput = input("Enter shelf number, box number, barcode, and destination separated by an underscore (I.E. A1_1, 1, C) >> ")
    # Splitting the input by commas and stripping spaces in one step
    split_input = [element.strip() for element in rawinput.split(",")]

    # Further splitting the first element by underscore for shelf and box
    shelf_number, box_number = split_input[0].split("_")

    # Directly accessing barcode and destination from the split_input list
    barcode = split_input[1]
    destination = split_input[2]

    # Converting box_number to int
    box_number = int(box_number)
    
    get_box_coordinates(shelf_number, box_number)
        
main()