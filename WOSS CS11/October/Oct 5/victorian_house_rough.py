import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Victorian House Line Art - Press ESC to Exit")

# Colors
BG_COLOR = (248, 248, 246)  # Warm paper white background
LINE_COLOR = (20, 20, 20)    # Dark charcoal ink line color

clock = pygame.time.Clock()


def draw_squiggles(surface, points):
    """Draws squiggly tree/grass contour lines."""
    pygame.draw.lines(surface, LINE_COLOR, False, points, 2)


def draw_house_lineart(surface):
    surface.fill(BG_COLOR)

    # 1. Outer Frame & Background Trees
    # Outer Border Box
    pygame.draw.rect(surface, LINE_COLOR, (40, 20, 720, 930), 2)

    # Left Tree Outline
    draw_squiggles(surface, [(40, 110), (55, 90), (95, 65), (120, 110), (160, 125), (200, 180)])
    draw_squiggles(surface, [(40, 300), (70, 250), (45, 200), (90, 140)])
    draw_squiggles(surface, [(40, 520), (60, 480), (50, 440)])
    # Tree detail marks (left)
    draw_squiggles(surface, [(50, 110), (68, 120)])
    draw_squiggles(surface, [(105, 130), (125, 140)])
    draw_squiggles(surface, [(110, 185), (138, 195)])
    draw_squiggles(surface, [(62, 255), (88, 268)])

    # Right Tree Outline
    draw_squiggles(surface, [(760, 110), (745, 90), (705, 65), (680, 110), (640, 125), (600, 180)])
    draw_squiggles(surface, [(760, 300), (730, 250), (755, 200), (710, 140)])
    draw_squiggles(surface, [(760, 520), (740, 480), (750, 440)])
    # Tree detail marks (right)
    draw_squiggles(surface, [(750, 110), (732, 120)])
    draw_squiggles(surface, [(695, 130), (675, 140)])
    draw_squiggles(surface, [(690, 185), (662, 195)])
    draw_squiggles(surface, [(738, 255), (712, 268)])

    # 2. Main Roof & Chimneys
    # Main Connecting Roof Line behind turrets
    pygame.draw.line(surface, LINE_COLOR, (140, 218), (660, 218), 3)

    # Left Chimney
    pygame.draw.rect(surface, LINE_COLOR, (253, 170, 38, 70), 3)
    pygame.draw.rect(surface, LINE_COLOR, (249, 165, 46, 7), 3)
    pygame.draw.rect(surface, LINE_COLOR, (262, 180, 20, 12), 2)
    pygame.draw.rect(surface, LINE_COLOR, (262, 196, 20, 12), 2)
    pygame.draw.rect(surface, LINE_COLOR, (262, 212, 20, 12), 2)

    # Right Chimney
    pygame.draw.rect(surface, LINE_COLOR, (463, 170, 38, 70), 3)
    pygame.draw.rect(surface, LINE_COLOR, (459, 165, 46, 7), 3)
    pygame.draw.rect(surface, LINE_COLOR, (472, 180, 20, 12), 2)
    pygame.draw.rect(surface, LINE_COLOR, (472, 196, 20, 12), 2)
    pygame.draw.rect(surface, LINE_COLOR, (472, 212, 20, 12), 2)

    # Center Dormer Structure
    pygame.draw.polygon(surface, LINE_COLOR, [(330, 250), (470, 250), (470, 305), (330, 305)], 3)
    pygame.draw.polygon(surface, LINE_COLOR, [(322, 250), (478, 250), (478, 243), (322, 243)], 3)
    # Dormer Windows
    pygame.draw.rect(surface, LINE_COLOR, (345, 260, 50, 35), 2)
    pygame.draw.rect(surface, LINE_COLOR, (405, 260, 50, 35), 2)
    # Dormer Grid (left window)
    pygame.draw.line(surface, LINE_COLOR, (370, 260), (370, 295), 1)
    pygame.draw.line(surface, LINE_COLOR, (345, 277), (395, 277), 1)
    # Dormer Grid (right window)
    pygame.draw.line(surface, LINE_COLOR, (430, 260), (430, 295), 1)
    pygame.draw.line(surface, LINE_COLOR, (405, 277), (455, 277), 1)

    # 3. Turret Roofs (Conical Peaks)
    # Left Tower Roof Peak
    pygame.draw.polygon(surface, LINE_COLOR, [(182, 160), (72, 340), (292, 340)], 3)
    pygame.draw.line(surface, LINE_COLOR, (72, 340), (115, 348), 3)
    pygame.draw.line(surface, LINE_COLOR, (292, 340), (249, 348), 3)

    # Right Tower Roof Peak
    pygame.draw.polygon(surface, LINE_COLOR, [(562, 160), (452, 340), (672, 340)], 3)
    pygame.draw.line(surface, LINE_COLOR, (452, 340), (495, 348), 3)
    pygame.draw.line(surface, LINE_COLOR, (672, 340), (629, 348), 3)

    # 4. Upper Floor Architecture & Windows
    # Belt/Divider Horizontals
    pygame.draw.line(surface, LINE_COLOR, (85, 348), (660, 348), 3)
    pygame.draw.line(surface, LINE_COLOR, (65, 455), (680, 455), 3)

    # Left Tower Upper Bay Windows
    bay_x = [98, 142, 222]
    bay_w = [36, 72, 36]
    for x, w in zip(bay_x, bay_w):
        pygame.draw.rect(surface, LINE_COLOR, (x, 360, w, 82), 2)
        # Panes
        pygame.draw.line(surface, LINE_COLOR, (x, 395), (x + w, 395), 1)
        pygame.draw.line(surface, LINE_COLOR, (x, 420), (x + w, 420), 1)
        if w > 40:
            pygame.draw.line(surface, LINE_COLOR, (x + w // 2, 360), (x + w // 2, 442), 1)

    # Right Tower Upper Bay Windows
    bay_x_r = [488, 532, 612]
    for x, w in zip(bay_x_r, bay_w):
        pygame.draw.rect(surface, LINE_COLOR, (x, 360, w, 82), 2)
        pygame.draw.line(surface, LINE_COLOR, (x, 395), (x + w, 395), 1)
        pygame.draw.line(surface, LINE_COLOR, (x, 420), (x + w, 420), 1)
        if w > 40:
            pygame.draw.line(surface, LINE_COLOR, (x + w // 2, 360), (x + w // 2, 442), 1)

    # Central Upper Gable (Tudor Style)
    pygame.draw.polygon(surface, LINE_COLOR, [(370, 305), (310, 365), (430, 365)], 3)
    pygame.draw.line(surface, LINE_COLOR, (370, 305), (370, 365), 2)
    pygame.draw.line(surface, LINE_COLOR, (335, 340), (370, 365), 2)
    pygame.draw.line(surface, LINE_COLOR, (405, 340), (370, 365), 2)
    pygame.draw.line(surface, LINE_COLOR, (345, 365), (370, 335), 2)
    pygame.draw.line(surface, LINE_COLOR, (395, 365), (370, 335), 2)

    # Upper Center French Doors (Fixed tuple format here)
    pygame.draw.rect(surface, LINE_COLOR, (350, 365, 40, 55), 2)
    pygame.draw.line(surface, LINE_COLOR, (370, 365), (370, 420), 2)

    # Upper Tudor Half-Timber Accents (Left & Right Mid Section)
    # Left Timber Chevron
    pygame.draw.polygon(surface, LINE_COLOR, [(85, 455), (145, 430), (145, 455)], 2)
    pygame.draw.polygon(surface, LINE_COLOR, [(145, 430), (205, 455), (145, 455)], 2)
    pygame.draw.polygon(surface, LINE_COLOR, [(205, 455), (265, 430), (265, 455)], 2)
    # Right Timber Chevron
    pygame.draw.polygon(surface, LINE_COLOR, [(480, 455), (540, 430), (540, 455)], 2)
    pygame.draw.polygon(surface, LINE_COLOR, [(540, 430), (600, 455), (600, 455)], 2)
    pygame.draw.polygon(surface, LINE_COLOR, [(600, 455), (660, 430), (660, 455)], 2)

    # 5. Lower Floor Architecture & Main Entrance
    # Lower Outer Side Walls
    pygame.draw.line(surface, LINE_COLOR, (65, 455), (65, 590), 3)
    pygame.draw.line(surface, LINE_COLOR, (680, 455), (680, 590), 3)

    # Lower Left Windows
    for x, w in zip([92, 136, 218], [38, 74, 38]):
        pygame.draw.rect(surface, LINE_COLOR, (x, 475, w, 95), 2)
        pygame.draw.line(surface, LINE_COLOR, (x, 520), (x + w, 520), 1)
        if w > 40:
            pygame.draw.line(surface, LINE_COLOR, (x + w // 2, 475), (x + w // 2, 570), 1)

    # Lower Right Windows
    for x, w in zip([488, 532, 612], [38, 74, 38]):
        pygame.draw.rect(surface, LINE_COLOR, (x, 475, w, 95), 2)
        pygame.draw.line(surface, LINE_COLOR, (x, 520), (x + w, 520), 1)
        if w > 40:
            pygame.draw.line(surface, LINE_COLOR, (x + w // 2, 475), (x + w // 2, 570), 1)

    # Main Entrance Roof Overhang
    pygame.draw.line(surface, LINE_COLOR, (255, 465), (490, 465), 3)
    pygame.draw.line(surface, LINE_COLOR, (250, 473), (495, 473), 3)

    # Main Entrance Frame
    pygame.draw.rect(surface, LINE_COLOR, (315, 480, 115, 90), 3)
    # Double Doors
    pygame.draw.rect(surface, LINE_COLOR, (342, 490, 30, 80), 2)
    pygame.draw.rect(surface, LINE_COLOR, (372, 490, 30, 80), 2)
    # Door Handles
    pygame.draw.circle(surface, LINE_COLOR, (367, 535), 2)
    pygame.draw.circle(surface, LINE_COLOR, (377, 535), 2)

    # Side Pillar Sidelights (Left & Right of Main Door)
    for y_off in range(4):
        pygame.draw.rect(surface, LINE_COLOR, (318, 490 + (y_off * 19), 18, 14), 2)
        pygame.draw.rect(surface, LINE_COLOR, (408, 490 + (y_off * 19), 18, 14), 2)

    # Bottom Wall Line of House
    pygame.draw.line(surface, LINE_COLOR, (65, 590), (680, 590), 3)

    # 6. Lawn, Staircases, Cobblestones, & Ground Base
    # Curved Lawn Contours
    draw_squiggles(surface, [(140, 580), (180, 588), (280, 580), (320, 586), (380, 578), (440, 585), (510, 578), (580, 586)])
    draw_squiggles(surface, [(200, 620), (220, 630), (290, 620), (380, 640), (420, 630), (520, 638)])

    # Center Staircase
    for i in range(8):
        pygame.draw.rect(surface, LINE_COLOR, (310 - (i * 4), 650 + (i * 12), 125 + (i * 8), 12), 2)

    # Left Side Steps
    for i in range(5):
        pygame.draw.rect(surface, LINE_COLOR, (25 - (i * 2), 590 + (i * 11), 110 + (i * 4), 11), 2)

    # Right Side Steps
    for i in range(5):
        pygame.draw.rect(surface, LINE_COLOR, (610 - (i * 2), 590 + (i * 11), 110 + (i * 4), 11), 2)

    # Ground Separation Line
    pygame.draw.line(surface, LINE_COLOR, (25, 715), (300, 715), 3)
    pygame.draw.line(surface, LINE_COLOR, (445, 715), (720, 715), 3)

    # Cobblestone Details
    stones = [
        (220, 700, 22, 10), (500, 660, 20, 10), (610, 685, 30, 12),
        (515, 725, 20, 10), (540, 735, 18, 9), (210, 760, 26, 11),
        (170, 765, 28, 11), (215, 820, 22, 10), (700, 710, 24, 10)
    ]
    for x, y, w, h in stones:
        pygame.draw.rect(surface, LINE_COLOR, (x, y, w, h), 2)

    # Base Pavement Lines
    pygame.draw.line(surface, LINE_COLOR, (15, 835), (730, 835), 3)
    pygame.draw.line(surface, LINE_COLOR, (15, 860), (730, 860), 3)
    pygame.draw.line(surface, LINE_COLOR, (15, 895), (730, 895), 3)

    # Footer Watermark Text Representation
    font = pygame.font.SysFont("arial", 20)
    text = font.render("MondayMandala.com", True, LINE_COLOR)
    surface.blit(text, (480, 838))



# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    draw_house_lineart(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()