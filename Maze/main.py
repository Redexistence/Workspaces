import random
import os
import msvcrt

def create_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    stack = []
    
    start_x, start_y = (1, 1)
    stack.append((start_x, start_y))
    maze[start_y][start_x] = ' '
    
    while stack:
        x, y = stack.pop()
        
        neighbors = []
        if y > 1 and maze[y - 2][x] == '#':
            neighbors.append((x, y - 2))
        if y < height - 2 and maze[y + 2][x] == '#':
            neighbors.append((x, y + 2))
        if x > 1 and maze[y][x - 2] == '#':
            neighbors.append((x - 2, y))
        if x < width - 2 and maze[y][x + 2] == '#':
            neighbors.append((x + 2, y))
            
        if neighbors:
            stack.append((x, y)) # Push current cell back to stack
            
            next_x, next_y = random.choice(neighbors)
            
            # Carve a path to the neighbor
            if next_x == x:
                maze[y + (next_y - y) // 2][x] = ' '
            else:
                maze[y][x + (next_x - x) // 2] = ' '
            
            maze[next_y][next_x] = ' '
            stack.append((next_x, next_y))
            
    # Set a clear start and end point
    maze[1][1] = 'S'
    maze[height - 2][width - 2] = 'E'
    
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))


maze_width = 21 # Must be odd
maze_height = 21 # Must be odd
    
my_maze = create_maze(maze_width, maze_height)
print_maze(my_maze)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


maze_width = 21
maze_height = 21
    
maze = create_maze(maze_width, maze_height)
    
player_x, player_y = 1, 1
end_x, end_y = maze_width - 2, maze_height - 2

# Game loop
while True:
    clear_screen()
        
    # Draw maze with player
    display_maze = [row[:] for row in maze]
    display_maze[player_y][player_x] = 'P'
    print_maze(display_maze)
        
    # Check win condition
    if player_x == end_x and player_y == end_y:
        print("Congratulations! You've escaped the maze!")
        break
            
    # Get input
    print("Use WASD to move.")
    key = msvcrt.getch().decode().lower()
        
    new_x, new_y = player_x, player_y
        
    # Update player position based on input
    if key == 'w':
        new_y -= 1
    elif key == 's':
        new_y += 1
    elif key == 'a':
        new_x -= 1
    elif key == 'd':
        new_x += 1
            
    # Check for valid move
    if 0 <= new_x < maze_width and 0 <= new_y < maze_height:
        if maze[new_y][new_x] != '#':
            player_x, player_y = new_x, new_y
                