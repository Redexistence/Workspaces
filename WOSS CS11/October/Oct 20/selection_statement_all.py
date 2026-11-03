# Level 2
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

# Level 3
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

# Get the rectangle's position and dimensions from the user
rect_x = int(input("Please enter the rectangle's x coordinate: "))
rect_y = int(input("Please enter the rectangle's y coordinate: "))
rect_width = int(input("Please enter the rectangle's width: "))
rect_height = int(input("Please enter the rectangle's height: "))

px_input = int(input("Please enter the x coordinate of P: "))
py_input = int(input("Please enter the y coordinate of P: "))

define_rectangle(rect_x, rect_y, rect_width, rect_height, px_input, py_input)

# Level 3+
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

# Get rectangle values from the user
rect_x = int(input("Enter the rectangle's x-coordinate: "))
rect_y = int(input("Enter the rectangle's y-coordinate: "))
rect_width = int(input("Enter the rectangle's width: "))
rect_height = int(input("Enter the rectangle's height: "))

user_point = input("Please enter the point in the form (x, y): ")

# Clean up
cleaned_point = user_point.replace("(", "").replace(")", "")
parts = cleaned_point.split(",")

# Convert to integer
px_input = int(parts[0].strip())
py_input = int(parts[1].strip())

define_rectangle(rect_x, rect_y, rect_width, rect_height, px_input, py_input)

# Level 4-
def calculate_midpoints(ax, ay, bx, by, cx, cy, dx, dy):
    """
    Calculates midpoints using standard formula: ((x1+x2)/2, (y1+y2)/2)
    F is midpoint of AB
    I is midpoint of AD
    H is midpoint of CD
    G is midpoint of BC
    M is midpoint of the rectangle center
    """
    fx = (ax + bx) / 2
    fy = (ay + by) / 2
    
    ix = (ax + dx) / 2
    iy = (ay + dy) / 2
    
    hx = (cx + dx) / 2
    hy = (cy + dy) / 2
    
    gx = (bx + cx) / 2
    gy = (by + cy) / 2
    
    mx = (ax + cx) / 2
    my = (ay + cy) / 2
    
    # 1 decimal place
    print(f"The midpoints are: F({fx:.1f}, {fy:.1f}), I({ix:.1f}, {iy:.1f}), H({hx:.1f}, {hy:.1f}), G({gx:.1f}, {gy:.1f}), M({mx:.1f}, {my:.1f})")

def process_rectangle(x, y, width, height, px, py):
    ax, ay = x, y
    bx, by = x, y + height
    cx, cy = x + width, y + height
    dx, dy = x + width, y
    
    print(f"The rectangle has vertices A({ax}, {ay}), B({bx}, {by}), C({cx}, {cy}) and D({dx}, {dy})")
    
    calculate_midpoints(ax, ay, bx, by, cx, cy, dx, dy)
    
    if (ax <= px <= cx) and (ay <= py <= cy):
        print(f"({px}, {py}) is on or within the rectangle.")
    else:
        print(f"({px}, {py}) is outside the rectangle.")

# Get the rectangle coordinates and dimensions from the user
rect_x = int(input("Enter the rectangle's bottom-left x-coordinate: "))
rect_y = int(input("Enter the rectangle's bottom-left y-coordinate: "))
rect_width = int(input("Enter the rectangle's width: "))
rect_height = int(input("Enter the rectangle's height: "))

user_point = input("Please enter the point in the form (x, y): ")
cleaned_point = user_point.replace("(", "").replace(")", "")
parts = cleaned_point.split(",")
px_input = int(parts[0].strip())
py_input = int(parts[1].strip())

process_rectangle(rect_x, rect_y, rect_width, rect_height, px_input, py_input)

# Level 4
def calculate_midpoints(ax, ay, bx, by, cx, cy, dx, dy, px, py):
    fx, fy = (ax + bx) / 2, (ay + by) / 2  # Left Edge Midpoint
    ix, iy = (ax + dx) / 2, (ay + dy) / 2  # Bottom Edge Midpoint
    hx, hy = (cx + dx) / 2, (cy + dy) / 2  # Right Edge Midpoint
    gx, gy = (bx + cx) / 2, (by + cy) / 2  # Top Edge Midpoint
    mx, my = (ax + cx) / 2, (ay + cy) / 2  # Center Point M
    
    print(f"The midpoints are: F({fx:.1f}, {fy:.1f}), I({ix:.1f}, {iy:.1f}), H({hx:.1f}, {hy:.1f}), G({gx:.1f}, {gy:.1f}), M({mx:.1f}, {my:.1f})")
    
    # Outer bound check
    if not (ax <= px <= cx and ay <= py <= cy):
        print(f"({px}, {py}) is outside the rectangle.")
        return

    print(f"({px}, {py}) is on or within the rectangle.")
    
    if px == ax and py == ay:
        print("Point P is at vertex A.")
    elif px == bx and py == by:
        print("Point P is at vertex B.")
    elif px == cx and py == cy:
        print("Point P is at vertex C.")
    elif px == dx and py == dy:
        print("Point P is at vertex D.")
        
    elif px == ax:
        print("Point P is on the left edge.")
    elif px == cx:
        print("Point P is on the right edge.")
    elif py == ay:
        print("Point P is on the bottom edge.")
    elif py == cy:
        print("Point P is on the top edge.")
        
    elif px == mx or py == my:
        print("Point P lies exactly on an internal dividing line.")
        
    else:
        # Standard Grid Quadrant layout mapped cleanly within a bounded rectangle:
        if px < mx and py > my:
            print(f"({px}, {py}) lies within Quadrant 1.")
        elif px > mx and py > my:
            print(f"({px}, {py}) lies within Quadrant 2.")
        elif px < mx and py < my:
            print(f"({px}, {py}) lies within Quadrant 3.")
        elif px > mx and py < my:
            print(f"({px}, {py}) lies within Quadrant 4.")

# Main
rect_x = 3
rect_y = 5
rect_width = 17
rect_height = 21

user_point = input("Please enter the point in the form (x, y): ").strip()
try:
    cleaned_point = user_point.strip("() ")
    parts = [coordinate.strip() for coordinate in cleaned_point.split(",")]
    if len(parts) != 2:
        raise ValueError
    px_input, py_input = map(int, parts)
except ValueError:
    print("Invalid point. Enter two integer coordinates, for example: (8, 12).")
    exit()

print(f"The rectangle has vertices A({rect_x}, {rect_y}), B({rect_x}, {rect_y+rect_height}), C({rect_x+rect_width}, {rect_y+rect_height}), D({rect_x+rect_width}, {rect_y})")
calculate_midpoints(rect_x, rect_y, rect_x, rect_y+rect_height, rect_x+rect_width, rect_y+rect_height, rect_x+rect_width, rect_y, px_input, py_input)

# Level 4+
def clean_and_parse_input(raw_input):
    """
    Cleans up input string and safely converts contents to a numerical point.
    Handles malformations seamlessly.
    """
    clean_str = raw_input.replace("(", "").replace(")", "")
    
    if "," not in clean_str:

        tokens = clean_str.split()
    else:
        tokens = clean_str.split(",")
        
    valid_tokens = []
    for t in tokens:
        stripped = t.strip()
        if stripped != "":
            valid_tokens.append(stripped)
            
    if len(valid_tokens) != 2:
        print("Error: Input does not contain exactly an X and Y coordinate. Ensure format is (x, y).")
        return None
        
    try:
        x_val = float(valid_tokens[0])
        y_val = float(valid_tokens[1])
        return x_val, y_val
    except ValueError:
        print("Error: One or both entered coordinate variables are non-numeric strings.")
        return None

def calculate_midpoints(ax, ay, bx, by, cx, cy, dx, dy, px, py):
    fx, fy = (ax + bx) / 2, (ay + by) / 2
    ix, iy = (ax + dx) / 2, (ay + dy) / 2
    hx, hy = (cx + dx) / 2, (cy + dy) / 2
    gx, gy = (bx + cx) / 2, (by + cy) / 2
    mx, my = (ax + cx) / 2, (ay + cy) / 2
    
    print(f"The midpoints are: F({fx:.1f}, {fy:.1f}), I({ix:.1f}, {iy:.1f}), H({hx:.1f}, {hy:.1f}), G({gx:.1f}, {gy:.1f}), M({mx:.1f}, {my:.1f})")
    
    if not (ax <= px <= cx and ay <= py <= cy):
        print(f"({px}, {py}) is outside the rectangle.")
        return

    print(f"({px}, {py}) is on or within the rectangle.")
    
    if px == ax and py == ay:
        print("Point P is at vertex A.")
    elif px == bx and py == by:
        print("Point P is at vertex B.")
    elif px == cx and py == cy:
        print("Point P is at vertex C.")
    elif px == dx and py == dy:
        print("Point P is at vertex D.")
    elif px == ax:
        print("Point P is on the left edge.")
    elif px == cx:
        print("Point P is on the right edge.")
    elif py == ay:
        print("Point P is on the bottom edge.")
    elif py == cy:
        print("Point P is on the top edge.")
    elif px == mx or py == my:
        print("Point P lies exactly on an internal dividing line.")
    else:
        if px < mx and py > my:
            print(f"({px}, {py}) lies within Quadrant 1.")
        elif px > mx and py > my:
            print(f"({px}, {py}) lies within Quadrant 2.")
        elif px < mx and py < my:
            print(f"({px}, {py}) lies within Quadrant 3.")
        elif px > mx and py < my:
            print(f"({px}, {py}) lies within Quadrant 4.")

# Main
rect_x, rect_y = clean_and_parse_input(
    input("Enter the rectangle's bottom-left corner as (x, y): ")
)

while True:
    try:
        rect_width = float(input("Enter the rectangle's width: "))
        rect_height = float(input("Enter the rectangle's height: "))
        if rect_width <= 0 or rect_height <= 0:
            print("Error: Width and height must be positive.")
            continue
        break
    except ValueError:
        print("Error: Width and height must be numeric.")

ax, ay = rect_x, rect_y
bx, by = rect_x, rect_y + rect_height
cx, cy = rect_x + rect_width, rect_y + rect_height
dx, dy = rect_x + rect_width, rect_y

parsed_point = None
while parsed_point is None:
    user_input = input("Please enter the point in the form (x, y): ")
    parsed_point = clean_and_parse_input(user_input)

px_input, py_input = parsed_point

print(f"The rectangle has vertices A({ax:.0f}, {ay:.0f}), B({bx:.0f}, {by:.0f}), C({cx:.0f}, {cy:.0f}) and D({dx:.0f}, {dy:.0f})")
calculate_midpoints(ax, ay, bx, by, cx, cy, dx, dy, px_input, py_input)
