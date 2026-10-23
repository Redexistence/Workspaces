def define_rectangle(x, y, width, height):
    """
    Calculates the 4 vertices of the rectangle based on Point A, width, and height.
    According to assignment geometry: 
    AB is vertical (height), AD is horizontal (width).
    """
    ax = x
    ay = y
    
    bx = x
    by = y + height
    
    cx = x + width
    cy = y + height
    
    dx = x + width
    dy = y
    
    print(f"The rectangle has vertices A({ax}, {ay}), B({bx}, {by}), C({cx}, {cy}) and D({dx}, {dy})")

# Get rectangle dimensions and coordinates from the user
rect_x = float(input("Enter the x-coordinate of point A: "))
rect_y = float(input("Enter the y-coordinate of point A: "))
rect_width = float(input("Enter the rectangle width: "))
rect_height = float(input("Enter the rectangle height: "))

define_rectangle(rect_x, rect_y, rect_width, rect_height)
