# create a green bordered rectangle in a black background
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

screen.fill(BLACK)

# Draw a green rectangle with a black border
pygame.draw.rect(screen, GREEN, (100, 100, 200, 150), 5)

pygame.display.flip()

# Make the screen show for 5 seconds
pygame.time.wait(5000)

pygame.quit()