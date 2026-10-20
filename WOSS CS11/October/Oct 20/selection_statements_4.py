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

user_point = input("Please enter the point in the form (x, y): ")
cleaned_point = user_point.replace("(", "").replace(")", "")
parts = cleaned_point.split(",")
px_input = int(parts[0].strip())
py_input = int(parts[1].strip())

print(f"The rectangle has vertices A({rect_x}, {rect_y}), B({rect_x}, {rect_y+rect_height}), C({rect_x+rect_width}, {rect_y+rect_height}), D({rect_x+rect_width}, {rect_y})")
calculate_midpoints(rect_x, rect_y, rect_x, rect_y+rect_height, rect_x+rect_width, rect_y+rect_height, rect_x+rect_width, rect_y, px_input, py_input)
