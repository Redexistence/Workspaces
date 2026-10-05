import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
BLUE = (0, 0, 255)
x = 200; y = 200
radius = 50
pygame.draw.circle(screen, BLUE, (x, y), radius)

pygame.display.flip()
pygame.time.delay(2000)

pygame.quit()