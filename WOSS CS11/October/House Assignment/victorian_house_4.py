# House drawing script using pygame
# Note to self: remember to clean up globals later, surf is acting weird if not global
import math
import sys
import pygame

# window / rendering setup - tweaked dimensions slightly
WIDTH, HEIGHT = 800, 1000
SS = 2                       # supersampling factor
SCALE = 0.74
OFF_X, OFF_Y = 19, 21        # screen offset
DESIGN_X0, DESIGN_Y0 = 40, 50

BG = (255, 255, 255)
INK = (22, 22, 22)

# Colour palette
SKY = (200, 228, 246) # Light Blue
TREE = (104, 156, 84) # Green
WOOD = (176, 134, 92) # Brown
ROOF = (84, 92, 118) # Slate Gray
BRICK = (168, 82, 62) # Brick Red
BRICK_DARK = (126, 60, 46) # Dark Brick Red
STONE = (196, 190, 178) # Stone Gray
STONE_LIGHT = (222, 218, 208) # Light Stone Gray
SOOT = (70, 66, 64) # Soot Black
WALL = (246, 232, 200) # Cream Wall
TIMBER = (112, 72, 46) # Timber Brown
TRIM = (250, 250, 246) # Trim White
GLASS = (168, 206, 230) # Glass Blue
GOLD = (212, 176, 82) # Gold
DOOR = (128, 38, 44) # Door Red
DOOR_LIGHT = (156, 58, 62) # Door Light Red
LAWN = (122, 182, 86) # Lawn Green
STEP = (214, 208, 196) # Step Gray
PAVING = (226, 210, 178) # Paving Stone
PAVER = (190, 112, 82) # Paver Brick
CURB = (178, 178, 176) # Curb Gray
CURB_DARK = (150, 150, 150) # Darker Curb Gray
ROAD = (110, 112, 118) # Road Gray

W_MAIN = 5.0                 # line widths in design units
W_MED = 4.0
W_THIN = 3.0

AXIS = 555                   # vertical symmetry axis of the house
L_TOWER, R_TOWER = 257, 2 * AXIS - 257
L_CHIMNEY, R_CHIMNEY = 393, 2 * AXIS - 393

surf = None                  # supersampled drawing surface (set in render())


# Drawing primitives (all coordinates are in design units)
def P(x, y):
    # coordinate transform formula
    xx = (OFF_X + (x - DESIGN_X0) * SCALE) * SS
    yy = (OFF_Y + (y - DESIGN_Y0) * SCALE) * SS
    return (xx, yy)


def px(w):
    return max(1.0, w * SCALE * SS)


def mx(x):
    # mirror x across the center axis
    return 2 * AXIS - x


def mirror(points):
    # TODO: check if this flips properly for all cases
    mirrored_pts = []
    for x, y in points:
        mirrored_pts.append((mx(x), y))
    return mirrored_pts


def _seg(a, b, w, color=INK):
    (x1, y1), (x2, y2) = P(*a), P(*b)
    r = px(w) / 2
    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)
    if length > 0:
        nx, ny = -dy / length * r, dx / length * r
        pygame.draw.polygon(surf, color, [(x1 + nx, y1 + ny), (x2 + nx, y2 + ny),
                                        (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)])
    pygame.draw.circle(surf, color, (x1, y1), r)
    pygame.draw.circle(surf, color, (x2, y2), r)


def line(a, b, w=W_MAIN):
    _seg(a, b, w)


def lines(points, w=W_MAIN, color=INK, closed=False):
    pts = list(points)
    if closed:
        pts.append(points[0])
        
    for i in range(len(pts) - 1):
        _seg(pts[i], pts[i+1], w, color)


def fill(points, color=BG):
    converted_pts = []
    for p in points:
        converted_pts.append(P(*p))
    pygame.draw.polygon(surf, color, converted_pts)


def shape(points, w=W_MAIN, color=BG):
    # Filled closed polygon with an ink outline (hides what is behind).
    fill(points, color)
    lines(points, w, closed=True)


def box(x1, y1, x2, y2, w=W_MAIN, color=BG):
    shape([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], w, color)


def rbox(x1, y1, x2, y2, radius, w=W_MED, color=BG):
    # Filled rounded rectangle.
    a, b = P(x1, y1), P(x2, y2)
    rect = pygame.Rect(round(a[0]), round(a[1]), round(b[0] - a[0]), round(b[1] - a[1]))
    rr = round(px(radius))
    pygame.draw.rect(surf, color, rect, border_radius=rr)
    pygame.draw.rect(surf, INK, rect, width=max(1, round(px(w))), border_radius=rr)


def smooth(points, steps=8):
    if len(points) < 3:
        return list(points)
    pts = [points[0]] + list(points) + [points[-1]]
    out = []
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        for s in range(steps):
            t = s / steps
            t2 = t * t
            t3 = t * t * t
            
            # Spline math calculation
            calc_pts = []
            for k in range(2):
                val = 0.5 * ((2 * p1[k]) + (-p0[k] + p2[k]) * t \
                            + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2 \
                            + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t3)
                calc_pts.append(val)
            out.append(tuple(calc_pts))
            
    out.append(points[-1])
    return out


def curve(points, w=W_MAIN):
    lines(smooth(points), w)


def lerp(a, b, t):
    res_x = a[0] + (b[0] - a[0]) * t
    res_y = a[1] + (b[1] - a[1]) * t
    return (res_x, res_y)


def quad_pt(q, u, v):
    tl, tr, br, bl = q
    top_lerp = lerp(tl, tr, u)
    bot_lerp = lerp(bl, br, u)
    return lerp(top_lerp, bot_lerp, v)


def sub_quad(q, u1, v1, u2, v2):
    return [quad_pt(q, u1, v1), quad_pt(q, u2, v1), quad_pt(q, u2, v2), quad_pt(q, u1, v2)]


def beam(a, b, width, w=W_MED, color=TIMBER):
    # A timber brace drawn as a white strip with two outlines.
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = math.hypot(dx, dy)
    if length == 0:
        length = 0.001 # quick fix for division by zero crash
    nx, ny = -dy / length * width / 2, dx / length * width / 2
    shape([(a[0] + nx, a[1] + ny), (b[0] + nx, b[1] + ny),
           (b[0] - nx, b[1] - ny), (a[0] - nx, a[1] - ny)], w, color)


def scallops(points, bulge=0.35, w=W_MAIN, fill_to=None, color=TREE):
    # Bumpy foliage outline: an arc bulging to the left of travel per segment.
    out = [points[0]]
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        dx, dy = x2 - x1, y2 - y1
        cx, cy = (x1 + x2) / 2 + dy * bulge, (y1 + y2) / 2 - dx * bulge
        for i in range(1, 11):
            t = i / 10
            px_val = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx + t * t * x2
            py_val = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy + t * t * y2
            out.append((px_val, py_val))
    if fill_to:
        fill(out + fill_to, color)
    lines(out, w)


def squiggle(points, w=W_THIN):
    curve(points, w)


def tuft(x, y):
    squiggle([(x - 11, y + 3), (x - 7, y - 3), (x - 2, y + 2), (x + 3, y - 3),
              (x + 7, y + 2), (x + 11, y - 1)])


# Scene parts
def draw_trees_and_fences():
    # Left tree canopy outline (runs from the page edge to the left spire)
    scallops([(40, 152), (62, 138), (86, 118), (100, 98), (126, 94), (140, 126),
              (147, 157), (172, 178), (200, 195), (220, 214), (229, 250), (252, 292)],
             fill_to=[(252, 930), (40, 930)])
    # Right tree canopy outline (runs from the roof corner to the page edge)
    scallops([(917, 346), (930, 318), (950, 280), (963, 256), (972, 230),
              (999, 197), (1020, 170), (1031, 146), (1047, 124), (1062, 127),
              (1070, 145)], fill_to=[(1070, 930), (917, 930)])

    # Leaf / bark texture marks - manually added coordinates lol
    squiggle([(58, 184), (63, 178), (68, 183), (73, 178), (78, 183)])
    squiggle([(129, 284), (140, 289), (147, 296), (157, 301), (146, 308)])
    squiggle([(72, 405), (82, 402), (90, 410), (102, 416)])
    squiggle([(50, 704), (52, 714), (62, 716), (75, 721)])
    squiggle([(44, 790), (52, 786), (57, 792), (52, 798), (64, 797)])
    squiggle([(1037, 157), (1042, 165), (1047, 172)])
    squiggle([(985, 228), (992, 222), (1000, 227), (1008, 222), (1015, 226)])
    squiggle([(968, 356), (976, 350), (985, 353), (993, 348), (1001, 351)])
    squiggle([(1036, 424), (1040, 433), (1045, 440), (1053, 443)])
    squiggle([(1031, 612), (1037, 606), (1043, 611), (1049, 606), (1055, 612)])
    squiggle([(1040, 692), (1047, 700), (1040, 706), (1048, 713)])
    squiggle([(1036, 782), (1043, 776), (1051, 783), (1059, 778)])

    # Garden fences peeking out on both sides
    for side in (lambda p: p, mirror):
        top = [(42, 826), (58, 831), (74, 839), (88, 848)]
        fill(side(smooth(top) + [(88, 925), (42, 925)]), WOOD)
        curve(side(top), W_MED)
        fence_coords = [(48, 828), (60, 832), (72, 838), (84, 845)]
        for x, y in fence_coords:
            lines(side([(x, y), (x, 925)]), W_MED)


def draw_main_roof():
    outline = [(52, 565), (50, 552), (65, 490), (177, 345),
               (mx(177), 345), (mx(65), 490), (mx(50), 552), (mx(52), 565)]
    fill(outline, ROOF)
    lines(outline)
    fill([(50, 552), (mx(50), 552), (mx(52), 565), (52, 565)], TRIM)
    line((50, 552), (mx(50), 552))   # fascia
    line((52, 565), (mx(52), 565))


def draw_chimney(cx):
    box(cx - 27, 347, cx + 27, 400, color=STONE)    # flashing / base
    box(cx - 18, 302, cx + 18, 384, color=BRICK)    # stack
    rbox(cx - 22, 287, cx + 22, 303, 6, W_MAIN, STONE_LIGHT)  # crown
    box(cx - 8, 274, cx + 8, 288, color=BRICK_DARK)  # pot
    
    vent_positions = [322, 343, 365]
    for y in vent_positions:                        # little vents
        rbox(cx - 7, y, cx + 7, y + 9, 3, W_THIN, SOOT)


def draw_dormer():
    c = AXIS
    box(c - 69, 425, c + 69, 442, color=TRIM)       # soffit
    line((c - 69, 432), (c + 69, 432), W_THIN)
    box(c - 65, 440, c + 65, 482, color=WALL)       # window wall
    line((c, 440), (c, 482), W_MED)
    box(c - 72, 396, c + 72, 425, color=ROOF)       # roof slab
    
    for x1 in (c - 48, c + 12):
        box(x1, 447, x1 + 36, 476, W_MED, TRIM)
        for ix in range(2):
            for iy in range(2):
                bx = x1 + 4 + ix * 15
                by = 451 + iy * 12
                rbox(bx, by, bx + 13, by + 9, 3, W_THIN, GLASS)


def draw_turret(tx):
    def side(pts):
        res = []
        for dx, y in pts:
            res.append((tx + dx, y))
        return res

    left = smooth([(-8, 297), (-35, 350), (-62, 410), (-88, 465), (-115, 505),
                   (-145, 530), (-160, 543)])
                   
    right = []
    for dx, y in left:
        right.append((-dx, y))
        
    cone = side(left + [(-76, 537), (76, 537)] + right[::-1])
    fill(cone, ROOF)
    lines(side(left))
    lines(side(right))
    facet = [(-6, 297), (-32, 375), (-52, 460), (-68, 510), (-76, 537)]
    curve(side(facet), W_MED)
    
    rev_facet = []
    for dx, y in facet:
        rev_facet.append((-dx, y))
    curve(side(rev_facet), W_MED)
    
    shape(side([(0, 266), (12, 298), (-12, 298)]), color=GOLD)  # finial

    # Eave band around the bottom of the cone
    band = [(-160, 543), (-76, 537), (76, 537), (160, 543),
            (170, 563), (76, 557), (-76, 557), (-170, 563)]
    shape(side(band), color=TRIM)
    lines(side([(-163, 550), (-76, 546), (76, 546), (163, 550)]), W_MED)
    
    for dx in (-76, 76):
        lines(side([(dx, 537), (dx, 557)]), W_MED)


def window(q, rows, transom=None, mullion_top=0.0, sill=False):
    shape(q, W_MAIN, TRIM)
    inner = sub_quad(q, 0.08, 0.04, 0.92, 0.96)
    fill(inner, GLASS)
    lines(inner, W_THIN, closed=True)
    if transom:
        for v in transom:
            line(quad_pt(inner, 0, v), quad_pt(inner, 1, v), W_MED)
    for v in rows:
        line(quad_pt(inner, 0, v), quad_pt(inner, 1, v), W_THIN)
    line(quad_pt(inner, 0.5, mullion_top), quad_pt(inner, 0.5, 1), W_MED)
    if sill:
        tl, tr, br, bl = q
        fill([(bl[0] - 4, bl[1]), (bl[0] - 4, bl[1] + 7),
              (br[0] + 4, br[1] + 7), (br[0] + 4, br[1])], TRIM)
        lines([(bl[0] - 4, bl[1]), (bl[0] - 4, bl[1] + 7),
               (br[0] + 4, br[1] + 7), (br[0] + 4, br[1])], W_MED)


def draw_tower(tx):
    def side(pts):
        res = []
        for dx, y in pts:
            res.append((tx + dx, y))
        return res

    fill(side([(-140, 560), (140, 560), (140, 930), (-140, 930)]), WALL)
    for x1, x2 in ((-140, -133), (-63, -56), (56, 63), (133, 140)):   # corner posts
        fill(side([(x1, 560), (x2, 560), (x2, 930), (x1, 930)]), TIMBER)
    
    vertical_lines = (-140, -133, -63, -56, 56, 63, 133, 140)
    for dx in vertical_lines:
        lines(side([(dx, 560), (dx, 930)]), W_MED)

    # Upper floor windows
    left_up = [(-112, 591), (-72, 586), (-72, 686), (-112, 691)]
    upper = dict(rows=[0.47, 0.73], transom=[0.12, 0.2], mullion_top=0.2)
    window(side(left_up), **upper)
    window(side([(-45, 581), (45, 581), (45, 682), (-45, 682)]), **upper)
    window(side([(72, 586), (112, 591), (112, 691), (72, 686)]), **upper)

    # Half-timbered band with diagonal braces
    braces = [((-130, 703), (-61, 753)), ((-58, 753), (0, 696)),
              ((0, 696), (58, 753)), ((61, 753), (130, 703))]
    for a, b in braces:
        beam(side([a])[0], side([b])[0], 10)
        
    for y in (698, 756):                            # timber rails
        top = [(-140, y), (-60, y - 8 + (y == 756) * 2), (60, y - 8 + (y == 756) * 2), (140, y)]
        fill(side(top + [(x, yy + 7) for x, yy in top[::-1]]), TIMBER)
    for off in (0, 7):
        lines(side([(-140, 698 + off), (-60, 690 + off), (60, 690 + off), (140, 698 + off)]), W_MED)
        lines(side([(-140, 756 + off), (-60, 750 + off), (60, 750 + off), (140, 756 + off)]), W_MED)
        
    for dx in vertical_lines:
        if abs(dx) < 100:
            y_top = 690
        else:
            y_top = 698
        lines(side([(dx, y_top), (dx, y_top + 70)]), W_MED)

    # Ground floor windows
    lower = dict(rows=[0.1, 0.4, 0.7], sill=True)
    window(side([(-120, 777), (-70, 771), (-70, 890), (-120, 896)]), **lower)
    window(side([(-50, 766), (50, 766), (50, 891), (-50, 891)]), **lower)
    window(side([(70, 771), (120, 777), (120, 896), (70, 890)]), **lower)


def draw_side_walls():
    for side in (lambda p: p, mirror):
        fill(side([(75, 566), (117, 566), (117, 930), (75, 930)]), WALL)
        fill(side([(90, 566), (98, 566), (98, 930), (90, 930)]), TIMBER)
        lines(side([(75, 566), (75, 655), (90, 655)]), W_MED)
        for x in (90, 98):
            lines(side([(x, 566), (x, 930)]), W_MED)
        shape(side([(98, 698), (117, 698), (117, 706), (98, 706)]), W_MED, TIMBER)


def draw_center_wall():
    fill([(397, 566), (713, 566), (713, 930), (397, 930)], WALL)


def draw_gable():
    c = AXIS
    fill([(c, 480), (441, 584), (451, 595), (451, 676), (mx(451), 676), (mx(451), 595), (mx(441), 584)], WALL)
    
    for side in (lambda p: p, mirror):
        fill(side([(497, 500 + (c - 497) * 0.91), (509, 500 + (c - 509) * 0.91), (509, 676), (497, 676)]), TIMBER)
        lines(side([(455, 592), (455, 676)]), W_MED)
        lines(side([(470, 592), (470, 676)]), W_THIN)
        for x in (497, 509):                        # timber posts
            calc_y = 500 + (c - x) * 0.91
            lines(side([(x, calc_y), (x, 676)]), W_MED)
            
    fill([(c - 6, 503), (c + 6, 503), (c + 6, 578), (c - 6, 578)], TIMBER)
    lines([(c - 6, 503), (c - 6, 578)], W_MED)      # king post
    lines([(c + 6, 503), (c + 6, 578)], W_MED)
    shape([(469, 578), (mx(469), 578), (mx(456), 590), (456, 590)], W_MED, TIMBER)  # collar beam

    # French doors onto the balcony
    box(c - 40, 598, c + 40, 676, color=TRIM)
    box(c - 35, 604, c - 2, 676, W_MED, GLASS)
    box(c + 2, 604, c + 35, 676, W_MED, GLASS)
    pygame.draw.circle(surf, INK, P(c - 7, 640), px(2.8))
    pygame.draw.circle(surf, INK, P(c + 7, 640), px(2.8))

    # Barge boards
    for side in (lambda p: p, mirror):
        shape(side([(c, 480), (441, 584), (451, 595), (c, 500)]), color=TIMBER)


def draw_balcony_and_entrance():
    c = AXIS
    box(c - 165, 675, c + 165, 720, color=TRIM)     # balcony front
    line((c - 165, 713), (c + 165, 713), W_THIN)
    box(c - 165, 745, c + 165, 757, color=TIMBER)   # porch beam
    rbox(c - 178, 727, c + 178, 745, 7, W_MAIN, STONE)  # balcony floor slab
    line((c - 172, 736), (c + 172, 736), W_THIN)

    # Porch side walls and door surround
    line((466, 757), (477, 776), W_MED)
    line((mx(466), 757), (mx(477), 776), W_MED)
    box(477, 776, mx(477), 930, color=TRIM)
    
    quoin_y_vals = [782, 808, 834, 860, 886]
    for y in quoin_y_vals:                          # quoin stones
        rbox(452, y, 477, y + 15, 4, W_MED, STONE)
        rbox(mx(477), y, mx(452), y + 15, 4, W_MED, STONE)

    for side in (lambda p: p, mirror):
        # Side lights
        shape(side([(480, 782), (506, 782), (506, 930), (480, 930)]), W_MED, DOOR)
        shape(side([(485, 790), (501, 790), (501, 888), (485, 888)]), W_THIN, GLASS)
        shape(side([(486, 894), (502, 894), (502, 910), (486, 910)]), W_THIN, DOOR_LIGHT)
        # Door leaves with arched kick panels
        shape(side([(508, 780), (553, 780), (553, 930), (508, 930)]), W_MED, DOOR)
        shape(side([(514, 790), (547, 790), (547, 882), (514, 882)]), W_THIN, DOOR_LIGHT)
        ax, ay = side([(530.5, 913)])[0]
        a, b = P(ax - 15, ay - 15), P(ax + 15, ay + 15)
        pygame.draw.arc(surf, INK, pygame.Rect(a[0], a[1], b[0] - a[0], b[1] - a[1]),
                        0, math.pi, round(px(W_THIN)))
        lines(side([(545, 836), (545, 850)]), W_THIN)  # handles


def draw_lawn_and_steps():
    # Lawn with bushy top edge
    bush_points = []
    for x in range(216, mx(216) + 1, 12):
        val = 915 + 2.5 * math.sin(x * 0.09) + 1.5 * math.sin(x * 0.23 + 1.3)
        bush_points.append((x, val))
        
    bush = smooth(bush_points, 4)
    fill([(42, 1058), (1068, 1058), (1068, 1244), (42, 1244)], PAVING)
    fill([(40, 1244), (1070, 1244), (1070, 1266), (40, 1266)], CURB)
    fill([(40, 1266), (1070, 1266), (1070, 1291), (40, 1291)], CURB_DARK)
    fill([(40, 1291), (1070, 1291), (1070, 1345), (40, 1345)], ROAD)
    fill(bush + [(mx(216), 1058), (216, 1058)], LAWN)
    lines(bush, W_MED)
    
    tuft_coords = [
        (311, 986), (434, 1038), (632, 1029), (783, 929), 
        (852, 968), (448, 938), (565, 981), (680, 939), (817, 1045)
    ]
    for x, y in tuft_coords:
        tuft(x, y)

    # Side staircases
    for side in (lambda p: p, mirror):
        fill(side([(42, 922), (216, 922), (216, 1058), (42, 1058)]), STEP)
        lines(side([(55, 922), (216, 922)]), W_MED)
        lines(side([(66, 930), (216, 930)]), W_MED)
        lines(side([(55, 922), (44, 1058)]))
        lines(side([(66, 930), (57, 1058)]), W_MED)
        
        step_y_vals = [963, 996, 1028]
        for y in step_y_vals:
            offset_x = 66 - (y - 930) * 0.07
            lines(side([(offset_x, y), (198, y)]), W_MED)
        shape(side([(198, 918), (216, 918), (216, 1060), (198, 1060)]), color=STONE)

    line((44, 1058), (mx(44), 1058))

    # Central steps down to the street
    fill([(458, 1058), (mx(458), 1058), (mx(458), 1244), (458, 1244)], STEP)
    
    central_steps_y = [1082, 1112, 1146, 1180, 1215]
    for y in central_steps_y:
        line((480, y), (mx(480), y), W_MED)
        
    for side in (lambda p: p, mirror):
        shape(side([(458, 1050), (480, 1050), (480, 1244), (458, 1244)]), color=STONE)

    # Paving stones (hardcoded grid list)
    bricks = [(76, 1072, 1), (236, 1071, 1), (392, 1068, 0), (438, 1094, 0),
              (339, 1131, 1), (52, 1132, 1), (127, 1215, 0), (279, 1210, 1),
              (310, 1228, 0), (60, 1225, 0), (425, 1222, 1), (672, 1072, 1),
              (713, 1137, 0), (672, 1200, 0), (704, 1222, 1), (817, 1072, 1),
              (870, 1069, 0), (767, 1090, 0), (1018, 1080, 1), (918, 1127, 1),
              (792, 1192, 1), (905, 1226, 0), (1025, 1190, 1), (1040, 1228, 0)]
              
    for x, y, pair in bricks:
        rbox(x - 15, y - 6, x + 15, y + 6, 5, W_MED, PAVER)
        if pair == 1:
            rbox(x - 4, y + 2.5, x + 24, y + 14.5, 5, W_MED, PAVER)

    # Kerb and street lines
    street_lines = [1244, 1266, 1291]
    for y in street_lines:
        line((40, y), (1070, y))


# Halloween decorations (fixed, hand-picked positions)
NIGHT_TOP = (34, 18, 72)          # deep purple
NIGHT_MID = (112, 40, 120)        # magenta dusk
NIGHT_LOW = (255, 132, 52)        # orange glow near the horizon
STAR = (255, 240, 150)
MOON = (255, 238, 170)
MOON_SHADE = (236, 212, 138)
PUMPKIN = (255, 122, 20)
PUMPKIN_DARK = (226, 92, 10)
STEM = (86, 132, 50)
GLOW = (255, 222, 60)
GHOST = (246, 246, 255)
BAT = (40, 26, 52)
EYE_RED = (230, 30, 40)
SPIDER = (30, 22, 34)
WEB = (236, 236, 244)
GRAVE = (150, 150, 168)
GRAVE_DARK = (110, 110, 128)

def ellipse(cx, cy, rx, ry, color, w=W_MED):
    a = P(cx - rx, cy - ry)
    rect = pygame.Rect(round(a[0]), round(a[1]), round(2 * rx * SCALE * SS), round(2 * ry * SCALE * SS))
    pygame.draw.ellipse(surf, color, rect)
    if w:
        pygame.draw.ellipse(surf, INK, rect, max(1, round(px(w))))


def place(pts, cx, cy, size, angle=0.0, flip=False):
    # Turn unit-shape points into design coordinates (scale, rotate, move).
    out = []
    ca, sa = math.cos(angle), math.sin(angle)
    for x, y in pts:
        if flip:
            x = -x
        out.append((cx + (x * ca - y * sa) * size, cy + (x * sa + y * ca) * size))
    return out


def draw_night_sky():
    top, bottom = P(0, 50)[1], P(0, 420)[1]
    for y in range(round(top), round(bottom) + 1):
        t = (y - top) / (bottom - top)
        if t < 0.55:
            a, b, k = NIGHT_TOP, NIGHT_MID, t / 0.55
        else:
            a, b, k = NIGHT_MID, NIGHT_LOW, (t - 0.55) / 0.45
        color = [round(a[i] + (b[i] - a[i]) * k) for i in range(3)]
        pygame.draw.line(surf, color, (P(40, 0)[0], y), (P(1070, 0)[0], y))


def draw_star(x, y, size):
    pts = []
    for i in range(8):
        r = size if i % 2 == 0 else size * 0.35
        a = i * math.pi / 4
        pts.append((x + r * math.cos(a), y + r * math.sin(a)))
    fill(pts, STAR)


def draw_moon(x, y, r):
    ellipse(x, y, r, r, MOON, W_MAIN)
    for dx, dy, cr in ((-0.35, -0.25, 0.22), (0.3, 0.1, 0.16), (-0.05, 0.45, 0.12)):
        ellipse(x + dx * r, y + dy * r, cr * r, cr * r, MOON_SHADE, W_THIN)


BAT_WING = [(0.12, -0.18), (0.35, -0.42), (0.65, -0.5), (1.0, -0.3), (0.85, -0.1),
            (0.82, 0.12), (0.62, 0.0), (0.52, 0.2), (0.34, 0.06), (0.22, 0.26), (0.12, 0.1)]
BAT_SHAPE = BAT_WING + [(-x, y) for x, y in reversed(BAT_WING)]


def draw_bat(x, y, size, angle):
    shape(place(BAT_SHAPE, x, y, size, angle), W_THIN, BAT)
    for flip in (False, True):
        shape(place([(0.02, -0.2), (0.1, -0.38), (0.14, -0.14)], x, y, size, angle, flip), W_THIN, BAT)
    ellipse(x, y, 0.14 * size, 0.24 * size, BAT, W_THIN)
    for ex, ey in place([(-0.05, -0.1), (0.05, -0.1)], x, y, size, angle):
        ellipse(ex, ey, 0.035 * size, 0.035 * size, GLOW, 0)


def draw_ghost(x, y, size, angle, flip):
    outline = [(-0.5, -0.3)]
    for i in range(1, 12):
        a = math.pi + i * math.pi / 12
        outline.append((0.5 * math.cos(a), -0.3 + 0.5 * math.sin(a)))
    outline += [(0.5, -0.3), (0.55, 0.15), (0.62, 0.55)]
    for i in range(1, 9):
        outline.append((0.62 - i * 1.24 / 8, 0.55 - 0.12 * (i % 2)))
    outline.append((-0.55, 0.15))
    pts = place(outline, x, y, size, angle, flip)
    shape(pts, W_MED, GHOST)
    for ex, ey in place([(-0.17, -0.35), (0.17, -0.35)], x, y, size, angle, flip):
        ellipse(ex, ey, 0.07 * size, 0.11 * size, INK, 0)
    mx_, my_ = place([(0, -0.08)], x, y, size, angle, flip)[0]
    ellipse(mx_, my_, 0.09 * size, 0.12 * size, INK, 0)


def draw_pumpkin(x, y, size, face):
    for dx in (-0.45, 0.45):
        ellipse(x + dx * size, y, 0.55 * size, 0.7 * size, PUMPKIN_DARK)
    ellipse(x, y, 0.6 * size, 0.75 * size, PUMPKIN)
    shape([(x - 0.08 * size, y - 0.68 * size), (x + 0.1 * size, y - 0.68 * size),
           (x + 0.2 * size, y - 1.0 * size), (x + 0.05 * size, y - 1.02 * size)], W_THIN, STEM)
    if face:
        for flip in (False, True):
            shape(place([(-0.42, -0.12), (-0.12, -0.12), (-0.27, -0.42)], x, y, size, flip=flip), W_THIN, GLOW)
        shape(place([(0, -0.12), (0.09, 0.05), (-0.09, 0.05)], x, y, size), W_THIN, GLOW)
        mouth = [(-0.6, 0.18), (-0.4, 0.28), (-0.3, 0.2), (-0.15, 0.3), (0, 0.22), (0.15, 0.3),
                 (0.3, 0.2), (0.4, 0.28), (0.6, 0.18), (0.4, 0.5), (0.2, 0.42), (0, 0.55),
                 (-0.2, 0.42), (-0.4, 0.5)]
        shape(place(mouth, x, y, size * 0.8), W_THIN, GLOW)
    else:
        for dx in (-0.25, 0.25):
            curve([(x + dx * size, y - 0.6 * size), (x + dx * 1.2 * size, y),
                   (x + dx * size, y + 0.6 * size)], W_THIN)


def draw_tombstone(x, y, size):
    top = [(0.4 * math.cos(math.pi + i * math.pi / 10), -0.6 + 0.4 * math.sin(math.pi + i * math.pi / 10))
           for i in range(11)]
    shape(place(top + [(0.4, 0.4), (-0.4, 0.4)], x, y, size), W_MED, GRAVE)
    box(x - 0.55 * size, y + 0.4 * size, x + 0.55 * size, y + 0.52 * size, W_MED, GRAVE_DARK)
    font = pygame.font.Font(None, max(8, round(px(size * 0.42))))
    text = font.render("RIP", True, INK)
    cx, cy = P(x, y - 0.42 * size)
    surf.blit(text, text.get_rect(center=(cx, cy)))
    lines([(x - 0.18 * size, y - 0.1 * size), (x + 0.18 * size, y - 0.1 * size)], W_THIN)
    lines([(x - 0.12 * size, y + 0.1 * size), (x + 0.12 * size, y + 0.1 * size)], W_THIN)
    tuft(x - 0.5 * size, y + 0.5 * size)
    tuft(x + 0.5 * size, y + 0.5 * size)


def draw_spider(x, top, y, size):
    lines([(x, top), (x, y - 0.5 * size)], 1.5)
    for flip in (False, True):
        for k in range(4):
            a = -0.7 + k * 0.45
            knee = place([(0.5 + 0.2 * math.cos(a), -0.35 + 0.6 * math.sin(a))], x, y, size, flip=flip)[0]
            foot = place([(0.75 + 0.15 * math.cos(a), 0.15 + 0.7 * math.sin(a))], x, y, size, flip=flip)[0]
            lines([(x, y), knee, foot], W_THIN)
    ellipse(x, y + 0.1 * size, 0.38 * size, 0.42 * size, SPIDER, W_THIN)
    ellipse(x, y - 0.35 * size, 0.22 * size, 0.2 * size, SPIDER, W_THIN)
    for dx in (-0.09, 0.09):
        ellipse(x + dx * size, y - 0.38 * size, 0.05 * size, 0.05 * size, EYE_RED, 0)


def draw_cobweb(cx, cy, size, sx, sy):
    # Web in a frame corner; sx/sy (+1/-1) point from the corner into the picture.
    spokes = 6
    ends = []
    for i in range(spokes):
        a = i * (math.pi / 2) / (spokes - 1)
        ends.append((math.cos(a), math.sin(a)))
    for ex, ey in ends:
        lines([(cx, cy), (cx + sx * ex * size, cy + sy * ey * size)], 1.5, WEB)
    for ring in (0.3, 0.55, 0.8, 1.0):
        r = ring * size
        for (ax, ay), (bx, by) in zip(ends, ends[1:]):
            mid_x, mid_y = (ax + bx) / 2 * 0.85, (ay + by) / 2 * 0.85
            lines([(cx + sx * ax * r, cy + sy * ay * r), (cx + sx * mid_x * r, cy + sy * mid_y * r),
                   (cx + sx * bx * r, cy + sy * by * r)], 1.5, WEB)


HALLOWEEN_LAYOUT = {
    "moon": (555, 150, 50),                                   # x, y, radius
    "stars": [(110, 95, 7), (250, 80, 6), (420, 70, 8), (480, 200, 5), (620, 230, 6),
              (690, 75, 7), (830, 95, 5), (1000, 110, 8), (300, 240, 5), (980, 200, 6),
              (160, 210, 6), (560, 290, 5), (760, 290, 6), (380, 300, 5), (870, 230, 7),
              (520, 95, 5), (1030, 300, 5), (220, 300, 6)],          # x, y, size
    "ghosts": [(180, 170, 70, -0.2, False), (900, 150, 72, 0.2, True),
               (760, 115, 55, 0.1, False)],                   # x, y, size, tilt, mirrored
    "bats": [(330, 110, 40, -0.2), (450, 250, 34, 0.25), (650, 90, 38, 0.1),
             (690, 220, 32, -0.3), (960, 260, 36, 0.2), (130, 290, 30, -0.1),
             (1000, 310, 28, 0.3)],                           # x, y, size, tilt
    "spiders": [(300, 566, 650, 30), (820, 566, 630, 28)],    # x, thread top, y, size
    "ground": [                                               # listed back to front
        ("tomb", 360, 980, 62), ("tomb", 740, 985, 66),
        ("pumpkin", 470, 1020, 32, True), ("pumpkin", 290, 1030, 30, True),
        ("pumpkin", 820, 1030, 34, True), ("pumpkin", 590, 1030, 28, False),
        ("pumpkin", 950, 1140, 34, True), ("pumpkin", 180, 1150, 38, True),
        ("pumpkin", 800, 1190, 40, True), ("pumpkin", 320, 1200, 32, False),
    ],
    "webs": [(40, 50, 150, 1, 1), (1070, 50, 130, -1, 1)],    # corner x, y, size, dir x, dir y
}


def draw_sky_decorations(layout):
    for x, y, s in layout["stars"]:
        draw_star(x, y, s)
    draw_moon(*layout["moon"])


def draw_ghosts(layout):
    for ghost in layout["ghosts"]:
        draw_ghost(*ghost)


def draw_front_decorations(layout):
    for item in layout["ground"]:
        if item[0] == "tomb":
            draw_tombstone(*item[1:])
        else:
            draw_pumpkin(*item[1:])
    for spider in layout["spiders"]:
        draw_spider(*spider)
    for bat in layout["bats"]:
        draw_bat(*bat)
    for web in layout["webs"]:
        draw_cobweb(*web)


def render(layout=HALLOWEEN_LAYOUT):
    # Draw the whole picture and return it as a WIDTH x HEIGHT surface.
    global surf
    surf = pygame.Surface((WIDTH * SS, HEIGHT * SS))
    surf.fill(BG)
    pygame.font.init()
    draw_night_sky()
    draw_sky_decorations(layout)

    draw_trees_and_fences()
    draw_ghosts(layout)
    draw_main_roof()
    draw_chimney(L_CHIMNEY)
    draw_chimney(R_CHIMNEY)
    draw_dormer()
    
    for tx in (L_TOWER, R_TOWER):
        draw_turret(tx)
        
    draw_side_walls()
    draw_center_wall()
    
    for tx in (L_TOWER, R_TOWER):
        draw_tower(tx)
        
    draw_gable()
    draw_balcony_and_entrance()
    draw_lawn_and_steps()
    draw_front_decorations(layout)

    lines([(40, 50), (1070, 50), (1070, 1345), (40, 1345)], W_MAIN, closed=True)
    return pygame.transform.smoothscale(surf, (WIDTH, HEIGHT))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Halloween Victorian House - ESC: exit, S: save")
    
    picture = render()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_s:
                    pygame.image.save(picture, "victorian_house.png")
                    print("Saved image as victorian_house.png!") # added print for feedback
                    
        screen.blit(picture, (0, 0))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()