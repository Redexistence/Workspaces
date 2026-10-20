def define_rectangle(x, y, width, height, px, py):
    min_x = x
    max_x = x + width
    min_y = y
    max_y = y + height
    
    print(f"The rectangle has vertices A({min_x}, {min_y}), B({min_x}, {max_y}), C({max_x}, {max_y}) and D({max_x}, {min_y})")
    
    if (min_x <= px <= max_x) and (min_y <= py <= max_y):
        print(f"({px}, {py}) is on or within the rectangle.")
    else:
        print(f"({px}, {py}) is outside the rectangle.")

# example values from the assignment sheet
rect_x = 3
rect_y = 5
rect_width = 17
rect_height = 21

user_point = input("Please enter the point in the form (x, y): ")

# Clean up
cleaned_point = user_point.replace("(", "").replace(")", "")
parts = cleaned_point.split(",")

# Convert to integer
px_input = int(parts[0].strip())
py_input = int(parts[1].strip())

define_rectangle(rect_x, rect_y, rect_width, rect_height, px_input, py_input)
