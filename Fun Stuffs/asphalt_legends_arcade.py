import pygame
import math

# --- Configuration & Setup ---
pygame.init()

# Use a reasonably large resolution to match the original aspect ratio
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1200
FPS = 60

# Colors (matching the coloring book theme)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)  # slightly softer black

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Victorian Manor Sketch - Pure Pygame Drawing")
clock = pygame.time.Clock()

# Helper for precise coordinates based on a 1000x1200 grid
def c(val_x, val_y):
    return (int(val_x * SCREEN_WIDTH / 1000), int(val_y * SCREEN_HEIGHT / 1200))

# Helper for line thickness scaling
T_MAIN = 3
T_THIN = 2

# --- Drawing Data & Geometry Definitions ---

# 1. Main Roof & Structure Boundaries
main_roof_top = 230
main_roof_base = 380
house_base_y = 650
left_edge_x = 100
right_edge_x = 900
center_y_mid = 500  # for horizontal split
# Main wall box
house_walls_main = [
    c(left_edge_x, main_roof_base),
    c(right_edge_x, main_roof_base),
    c(right_edge_x, house_base_y),
    c(left_edge_x, house_base_y)
]
# Horizontal mid-level line
house_mid_line = [c(left_edge_x, center_y_mid), c(right_edge_x, center_y_mid)]

# 2. Main High Roof (Large Trapeze/Triangle shape)
large_roof_pts = [
    c(170, 230),  # Left peak apex
    c(220, main_roof_top),  # Connection to right peak apex (using approximate positions from original)
    # Re-analyzing the original: It's actually a large pentagonal shape with a main central span.
    # Let's define the large roof outline
    c(100, 380),  # Top left corner of walls
    c(170, 230),  # Left top peak apex
    c(170+35, 230-20),  # Point before the span (estimated)
    # The original is complex. I will draw it as two main steep triangles connecting a central ridge.
    # Left Triangle
    c(left_edge_x, main_roof_base),
    c(180, 200),
    c(180+90, main_roof_base),
    # Span
    c(right_edge_x-180-90, main_roof_base),
    c(right_edge_x-180, 200),
    c(right_edge_x, main_roof_base)
]
# Simplified large roof peak path for outline
main_roof_outline = [
    c(left_edge_x, main_roof_base), # Base L
    c(left_edge_x + 70, 200),     # Peak L apex
    c(left_edge_x + 220, 200),    # Ridge connect start (approx from original)
    c(right_edge_x - 220, 200),   # Ridge connect end
    c(right_edge_x - 70, 200),    # Peak R apex
    c(right_edge_x, main_roof_base) # Base R
]
# Adjusting to better match the sharp peaks in image_1.png
main_roof_outline = [
    c(100, 380),  # Top left of walls
    c(160, 200),  # Sharp left peak
    c(160+40, 200-20), # Span start point
    c(right_edge_x - (160+40), 200-20), # Span end point
    c(right_edge_x - 160, 200),  # Sharp right peak
    c(right_edge_x, 380) # Top right of walls
]

# 3. Octagonal Tower Gables (Left & Right)
# Steep isosceles triangles
t_tower_w = 110  # width
t_tower_h = 240  # height from base
tower_y_roof_base = main_roof_base - 10
# Left Tower Gable
left_tower_g_points = [
    c(170 - (t_tower_w//2), tower_y_roof_base), # Base Left
    c(170, tower_y_roof_base - t_tower_h),    # Apex
    c(170 + (t_tower_w//2), tower_y_roof_base)  # Base Right
]
# Right Tower Gable
right_tower_g_points = [
    c(right_edge_x - (170 + (t_tower_w//2)), tower_y_roof_base), # Base Left (flip)
    c(right_edge_x - 170, tower_y_roof_base - t_tower_h),        # Apex
    c(right_edge_x - (170 - (t_tower_w//2)), tower_y_roof_base)  # Base Right
]

# 4. Central Gables (Dormers)
# Upper Center (Large Gabled Dormer)
dormer_u_y = 280
dormer_u_h = 100
dormer_u_w = 120
central_dormer_upper_pts = [
    c(500 - (dormer_u_w//2), dormer_u_y + dormer_u_h), # Base Left
    c(500, dormer_u_y),                             # Apex
    c(500 + (dormer_u_w//2), dormer_u_y + dormer_u_h)  # Base Right
]
# Central (Tudor Gable - below main roof ridge)
central_tudor_w = 200
central_tudor_h = 140
central_tudor_y = main_roof_base - central