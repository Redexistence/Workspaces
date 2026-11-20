import pygame
# Changed: named constants make the window, colours, speed, and radius easy to tune.
pygame.init()

WIDTH = 500
HEIGHT = 300
BACKGROUND = (0, 0, 0)
CIRCLE_COLOUR = (255, 0, 0)
CIRCLE_RADIUS = 10
CIRCLE_Y = HEIGHT - 100
MOVE_SPEED = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Movement")
clock = pygame.time.Clock()

# Changed: movement and drawing are separate functions for clarity and reusability.
def draw_screen(location, vertical_location):
    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, CIRCLE_COLOUR, (location, vertical_location), CIRCLE_RADIUS)
    pygame.display.flip()

def main():
    x = float(WIDTH // 2)
    y = float(CIRCLE_Y)
    running = True

    while running:
        # Changed: frame-rate-independent movement is consistent on fast/slow computers.
        delta_time = clock.tick(60) / 1000

        # Changed: events are handled only once and window closing is handled explicitly.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        if not running:
            break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x -= MOVE_SPEED * delta_time
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += MOVE_SPEED * delta_time
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y -= MOVE_SPEED * delta_time
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y += MOVE_SPEED * delta_time

        x = max(CIRCLE_RADIUS, min(WIDTH - CIRCLE_RADIUS, x))
        y = max(CIRCLE_RADIUS, min(HEIGHT - CIRCLE_RADIUS, y))
        draw_screen(round(x), round(y))

    pygame.quit()

# Changed: main() only runs when this file is executed, not when imported.
if __name__ == "__main__":
    main()
