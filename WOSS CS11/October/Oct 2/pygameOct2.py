import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
GREEN = (0, 255, 0)
screen.fill(GREEN)
pygame.display.flip()
# Make the screen show for 5 seconds
pygame.time.wait(5000)
pygame.quit()