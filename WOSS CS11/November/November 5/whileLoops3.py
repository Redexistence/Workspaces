import pygame
i = 1
while i <= 5:
    i += 1
    if i == 4:
        continue
    print(i)
# the problem here is that the continue statement skips the print statement when i is equal to 4, so 4 will not be printed. The output will be:
# 2
# 3
# 5
# To make it correct: here is the right implementation:
i = 1
while i <= 5:
    if i == 4:
        i += 1
        continue
    print(i)
    i += 1

x = 1
y = 1
w = 1
h = 1
# Why is the screen not working?
# Fix:
pygame.init()
screen = pygame.display.set_mode((800, 600))
for x in range(0,600,10):
    pygame.draw.rect(screen, "red", (x, y, w, h))
    h += 10
    pygame.display.flip()
    pygame.time.delay(1000)
# Rewriting the for loop to a while loop:
x = 0
while x < 600:
    pygame.draw.rect(screen, "red", (x, y, w, h))
    h += 10
    pygame.display.flip()
    pygame.time.delay(1000)
    x += 10