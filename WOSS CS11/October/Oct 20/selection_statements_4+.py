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
