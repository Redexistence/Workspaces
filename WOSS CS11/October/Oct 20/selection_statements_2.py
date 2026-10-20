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

# examples from the sheet
rect_x = 3
rect_y = 5
rect_width = 17
rect_height = 21

define_rectangle(rect_x, rect_y, rect_width, rect_height)
