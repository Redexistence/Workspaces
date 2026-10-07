import pygame
import sys
import math


pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pacman Animation")


BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


clock = pygame.time.Clock()


radius = 40
x_pos = -radius  
y_pos = SCREEN_HEIGHT // 2  
speed = 3


mouth_angle = 0
opening = True
max_mouth_angle = 45  


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    x_pos += speed

    if x_pos > SCREEN_WIDTH + radius:
        x_pos = -radius


    if opening:
        mouth_angle += 2
        if mouth_angle >= max_mouth_angle:
            opening = False
    else:
        mouth_angle -= 2
        if mouth_angle <= 0:
            opening = True


    screen.fill(BLACK)


    points = [(x_pos, y_pos)]
    

    start_angle = mouth_angle
    end_angle = 360 - mouth_angle
    
    for theta in range(int(start_angle), int(end_angle) + 1):
        rad = math.radians(theta)
        px = x_pos + radius * math.cos(rad)
        py = y_pos - radius * math.sin(rad)
        points.append((px, py))
        
    pygame.draw.polygon(screen, YELLOW, points)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
