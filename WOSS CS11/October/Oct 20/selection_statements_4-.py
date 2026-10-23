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
