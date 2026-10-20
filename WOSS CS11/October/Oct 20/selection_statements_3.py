def define_rectangle(x, y, width, height, px, py):
    min_x = x
    max_x = x + width
    min_y = y
    max_y = y + height
    
    print(f"The rectangle has vertices A({min_x}, {min_y}), B({min_x}, {max_y}), C({max_x}, {max_y}) and D({max_x}, {min_y})")
    
    # Selection Statement to determine if P is on or within bounds
    if (min_x <= px <= max_x) and (min_y <= py <= max_y):
        print(f"({px}, {py}) is on or within the rectangle.")
    else:
        print(f"({px}, {py}) is outside the rectangle.")

# Again, the example values from the assignment sheet
rect_x = 3
rect_y = 5
rect_width = 17
rect_height = 21

px_input = int(input("Please enter the x coordinate of P: "))
py_input = int(input("Please enter the y coordinate of P: "))

define_rectangle(rect_x, rect_y, rect_width, rect_height, px_input, py_input)
