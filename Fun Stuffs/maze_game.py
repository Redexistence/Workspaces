"""
LABYRINTH ESCAPE
=================
A large, multi-level, hard-difficulty maze game built with pygame.

Features
--------
- Procedurally generated mazes (randomized recursive backtracker) — every
  playthrough is different.
- 8 levels of escalating size & difficulty (bigger mazes, tighter timers,
  and a shrinking vision radius).
- "Fog of war" vision radius that shrinks as you progress — true hard mode.
- Friendly, polished UI: animated menu, hover buttons, HUD with timer /
  lives / level / minimap, pause overlay, level-complete & game-over
  screens, and an in-game help/instructions screen.
- Full keyboard control (arrow keys / WASD), pause with ESC or P.

Run:
    python3 maze_game.py

Controls:
    Arrow Keys / WASD  - move
    ESC / P            - pause
    M                  - toggle minimap size (in-game)
    R                  - restart current level (when paused or dead)
"""

import sys
import math
import random
import collections
import pygame

# -----------
# Basic setup
# -----------
pygame.init()
pygame.display.set_caption("Labyrinth Escape")

SCREEN_W, SCREEN_H = 1000, 720
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
FPS = 60

FONT_TITLE = pygame.font.SysFont("georgia", 64, bold=True)
FONT_BIG = pygame.font.SysFont("verdana", 40, bold=True)
FONT_MED = pygame.font.SysFont("verdana", 26, bold=True)
FONT_SMALL = pygame.font.SysFont("verdana", 18)
FONT_HUD = pygame.font.SysFont("verdana", 20, bold=True)

# -------------------------------------------------------------
# Palette (soft, friendly, high-contrast-enough to read easily)
# -------------------------------------------------------------
COL_BG_TOP = (24, 28, 46)
COL_BG_BOTTOM = (12, 14, 26)
COL_PANEL = (34, 40, 64)
COL_PANEL_LIGHT = (46, 54, 84)
COL_ACCENT = (94, 214, 190)
COL_ACCENT_DARK = (56, 158, 140)
COL_WARN = (240, 120, 100)
COL_GOLD = (247, 197, 87)
COL_WALL = (232, 236, 245)
COL_WALL_SHADOW = (150, 158, 180)
COL_FLOOR = (20, 24, 40)
COL_FLOOR_VISITED = (30, 36, 58)
COL_FLOOR_ALT = (24, 29, 48)
COL_TEXT = (235, 238, 245)
COL_TEXT_DIM = (160, 168, 190)
COL_PLAYER = (94, 214, 190)
COL_GOAL = (247, 197, 87)

# -------------
# Small helpers
# -------------

def lerp(a, b, t):
    return a + (b - a) * t


def lerp_color(c1, c2, t):
    return tuple(int(lerp(c1[i], c2[i], t)) for i in range(3))


def draw_vertical_gradient(surface, top_color, bottom_color):
    h = surface.get_height()
    for y in range(h):
        t = y / h
        pygame.draw.line(surface, lerp_color(top_color, bottom_color, t), (0, y), (surface.get_width(), y))


def draw_text(surface, text, font, color, center, shadow=True):
    if shadow:
        shadow_surf = font.render(text, True, (0, 0, 0))
        rect = shadow_surf.get_rect(center=(center[0] + 3, center[1] + 3))
        shadow_surf.set_alpha(90)
        surface.blit(shadow_surf, rect)
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=center)
    surface.blit(surf, rect)
    return rect


class Button:
    """A friendly rounded, hover-animated button."""

    def __init__(self, rect, text, font=FONT_MED, base_color=COL_PANEL_LIGHT,
                 hover_color=COL_ACCENT_DARK, text_color=COL_TEXT):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.hover_t = 0.0  # animated hover amount 0..1

    def update(self, mouse_pos):
        target = 1.0 if self.rect.collidepoint(mouse_pos) else 0.0
        self.hover_t = lerp(self.hover_t, target, 0.25)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, surface):
        color = lerp_color(self.base_color, self.hover_color, self.hover_t)
        grow = int(4 * self.hover_t)
        r = self.rect.inflate(grow, grow)
        pygame.draw.rect(surface, color, r, border_radius=14)
        pygame.draw.rect(surface, COL_ACCENT, r, width=2, border_radius=14)
        draw_text(surface, self.text, self.font, self.text_color, r.center)

    def clicked(self, mouse_pos, mouse_click):
        return mouse_click and self.rect.collidepoint(mouse_pos)


# --------------------------------------------------
# Maze generation (randomized recursive backtracker)
class Maze:
    DIRS = {
        'N': (0, -1),
        'S': (0, 1),
        'E': (1, 0),
        'W': (-1, 0),
    }
    OPPOSITE = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        # each cell stores which walls are OPEN (passable)
        self.open = {(x, y): set() for x in range(cols) for y in range(rows)}
        self._generate()
        self.visited_by_player = set()  # cells the player has seen (for minimap trail)

    def _generate(self):
        stack = [(0, 0)]
        visited = {(0, 0)}
        while stack:
            x, y = stack[-1]
            neighbors = []
            for d, (dx, dy) in self.DIRS.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.cols and 0 <= ny < self.rows and (nx, ny) not in visited:
                    neighbors.append((d, nx, ny))
            if not neighbors:
                stack.pop()
                continue
            d, nx, ny = random.choice(neighbors)
            self.open[(x, y)].add(d)
            self.open[(nx, ny)].add(self.OPPOSITE[d])
            visited.add((nx, ny))
            stack.append((nx, ny))

        # Add a handful of extra connections so the maze has loops / branch
        # choices instead of a single perfect path -> harder to reason about.
        extra_links = max(1, (self.cols * self.rows) // 18)
        for _ in range(extra_links):
            x = random.randint(0, self.cols - 1)
            y = random.randint(0, self.rows - 1)
            d, (dx, dy) = random.choice(list(self.DIRS.items()))
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.cols and 0 <= ny < self.rows:
                self.open[(x, y)].add(d)
                self.open[(nx, ny)].add(self.OPPOSITE[d])

    def can_move(self, pos, direction):
        return direction in self.open[pos]

    def neighbors(self, pos):
        x, y = pos
        result = []
        for d, (dx, dy) in self.DIRS.items():
            if d in self.open[pos]:
                result.append((x + dx, y + dy))
        return result

    def bfs_path(self, start, goal):
        """Shortest path from start to goal using BFS. Returns list of cells."""
        if start == goal:
            return [start]
        frontier = collections.deque([start])
        came_from = {start: None}
        while frontier:
            current = frontier.popleft()
            if current == goal:
                break
            for nxt in self.neighbors(current):
                if nxt not in came_from:
                    came_from[nxt] = current
                    frontier.append(nxt)
        if goal not in came_from:
            return [start]
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = came_from[cur]
        path.reverse()
        return path


# ----------------------------------------------------------------------------
# Level configuration — escalating size, timer pressure, and a shrinking
# fog-of-war vision radius. This is what makes the later levels genuinely
# hard.
# ----------------------------------------------------------------------------
LEVELS = [
    # cols, rows, time_limit_sec, vision_radius
    dict(cols=16, rows=12, time=90, vision=6),
    dict(cols=24, rows=18, time=110, vision=5),
    dict(cols=32, rows=24, time=130, vision=5),
    dict(cols=40, rows=30, time=150, vision=4),
    dict(cols=48, rows=36, time=175, vision=4),
    dict(cols=56, rows=42, time=200, vision=4),
    dict(cols=64, rows=48, time=225, vision=3),
    dict(cols=72, rows=54, time=250, vision=3),
]
MAX_LEVEL = len(LEVELS)


# ----------------------------------------------------------------------------
# Game states
# ----------------------------------------------------------------------------
STATE_MENU = "menu"
STATE_INSTRUCTIONS = "instructions"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_LEVEL_COMPLETE = "level_complete"
STATE_GAME_OVER = "game_over"
STATE_WIN = "win"


class Game:
    def __init__(self):
        self.state = STATE_MENU
        self.level_index = 0
        self.lives = 3
        self.score = 0
        self.moves = 0
        self.bg_t = 0.0

        # Buttons for the various screens
        cx = SCREEN_W // 2
        self.menu_buttons = [
            Button((cx - 140, 330, 280, 60), "Start Game"),
            Button((cx - 140, 405, 280, 60), "How To Play"),
            Button((cx - 140, 480, 280, 60), "Quit"),
        ]
        self.instructions_back = Button((cx - 140, 620, 280, 55), "Back")
        self.pause_buttons = [
            Button((cx - 140, 330, 280, 55), "Resume"),
            Button((cx - 140, 400, 280, 55), "Restart Level"),
            Button((cx - 140, 470, 280, 55), "Main Menu"),
        ]
        self.gameover_buttons = [
            Button((cx - 140, 420, 280, 55), "Try Again"),
            Button((cx - 140, 490, 280, 55), "Main Menu"),
        ]
        self.win_buttons = [
            Button((cx - 140, 480, 280, 55), "Play Again"),
            Button((cx - 140, 550, 280, 55), "Main Menu"),
        ]
        self.next_level_button = Button((cx - 140, 470, 280, 55), "Next Level")

        self.load_level(0)

    # ---------------- level lifecycle ----------------
    def load_level(self, index):
        self.level_index = index
        cfg = LEVELS[index]
        self.maze = Maze(cfg['cols'], cfg['rows'])
        self.player_pos = (0, 0)
        self.goal_pos = (cfg['cols'] - 1, cfg['rows'] - 1)
        self.vision_radius = cfg['vision']
        self.time_limit = cfg['time']
        self.time_left = float(cfg['time'])
        self.moves = 0
        self.move_cooldown = 0
        self.explored = {self.player_pos}
        self.player_anim_pos = list(self.player_pos)  # smooth screen movement
        self.state = STATE_PLAYING
        self.death_reason = ""

    def restart_level(self):
        self.load_level(self.level_index)

    # ---------------- input / update ----------------
    def try_move_player(self, direction):
        if self.move_cooldown > 0:
            return
        if self.maze.can_move(self.player_pos, direction):
            dx, dy = Maze.DIRS[direction]
            self.player_pos = (self.player_pos[0] + dx, self.player_pos[1] + dy)
            self.explored.add(self.player_pos)
            self.moves += 1
            self.move_cooldown = 8  # frames of input lock for crisp, controllable movement

    def update_playing(self, dt):
        self.bg_t += dt
        if self.move_cooldown > 0:
            self.move_cooldown -= 1

        # smooth animated position toward logical cell (for nice rendering)
        for i in range(2):
            self.player_anim_pos[i] = lerp(self.player_anim_pos[i], self.player_pos[i], 0.35)

        self.time_left -= dt
        if self.time_left <= 0:
            self.time_left = 0
            self.lose_life("Time's up!")
            return

        if self.player_pos == self.goal_pos:
            bonus = int(self.time_left * 8)
            self.score += 100 + bonus
            if self.level_index + 1 >= MAX_LEVEL:
                self.state = STATE_WIN
            else:
                self.state = STATE_LEVEL_COMPLETE

    def lose_life(self, reason):
        self.lives -= 1
        self.death_reason = reason
        if self.lives <= 0:
            self.state = STATE_GAME_OVER
        else:
            # respawn at start of same level, keep maze but reset positions/time
            cfg = LEVELS[self.level_index]
            self.player_pos = (0, 0)
            self.player_anim_pos = [0.0, 0.0]
            self.time_left = float(cfg['time'])
            self.move_cooldown = 20

    def full_restart(self):
        self.lives = 3
        self.score = 0
        self.load_level(0)

    # ---------------- rendering ----------------
    def compute_view_metrics(self):
        cfg = LEVELS[self.level_index]
        # reserve room for HUD at top
        play_h = SCREEN_H - 110
        cell = min((SCREEN_W - 40) / cfg['cols'], (play_h - 20) / cfg['rows'])
        cell = max(10, min(cell, 46))
        maze_w = cell * cfg['cols']
        maze_h = cell * cfg['rows']
        return cell, maze_w, maze_h, play_h

    def draw_background(self, surface):
        draw_vertical_gradient(surface, COL_BG_TOP, COL_BG_BOTTOM)

    def draw_maze(self, surface):
        cell, maze_w, maze_h, play_h = self.compute_view_metrics()
        ox = (SCREEN_W - maze_w) / 2
        oy = 100 + (play_h - maze_h) / 2

        cols, rows = self.maze.cols, self.maze.rows

        # floor panel behind maze
        panel_rect = pygame.Rect(ox - 14, oy - 14, maze_w + 28, maze_h + 28)
        pygame.draw.rect(surface, COL_PANEL, panel_rect, border_radius=10)

        vision = self.vision_radius

        for y in range(rows):
            for x in range(cols):
                dist = math.hypot(x - self.player_anim_pos[0], y - self.player_anim_pos[1])
                if dist > vision + 1.5 and (x, y) not in self.explored:
                    continue  # hidden by fog of war entirely -> skip drawing
                cx0 = ox + x * cell
                cy0 = oy + y * cell
                visible_now = dist <= vision
                if visible_now:
                    floor_col = COL_FLOOR if (x + y) % 2 else COL_FLOOR_ALT
                else:
                    floor_col = COL_FLOOR_VISITED
                pygame.draw.rect(surface, floor_col, (cx0, cy0, cell, cell))

        # walls
        for y in range(rows):
            for x in range(cols):
                dist = math.hypot(x - self.player_anim_pos[0], y - self.player_anim_pos[1])
                if dist > vision + 1.5 and (x, y) not in self.explored:
                    continue
                cx0 = ox + x * cell
                cy0 = oy + y * cell
                openset = self.maze.open[(x, y)]
                lw = max(2, int(cell * 0.09))
                if 'N' not in openset:
                    pygame.draw.line(surface, COL_WALL, (cx0, cy0), (cx0 + cell, cy0), lw)
                if 'W' not in openset:
                    pygame.draw.line(surface, COL_WALL, (cx0, cy0), (cx0, cy0 + cell), lw)
                if 'S' not in openset and y == rows - 1:
                    pygame.draw.line(surface, COL_WALL, (cx0, cy0 + cell), (cx0 + cell, cy0 + cell), lw)
                if 'E' not in openset and x == cols - 1:
                    pygame.draw.line(surface, COL_WALL, (cx0 + cell, cy0), (cx0 + cell, cy0 + cell), lw)

        # goal (draw only if explored/visible)
        gx, gy = self.goal_pos
        gdist = math.hypot(gx - self.player_anim_pos[0], gy - self.player_anim_pos[1])
        if gdist <= vision + 1.5 or self.goal_pos in self.explored:
            gcx = ox + gx * cell + cell / 2
            gcy = oy + gy * cell + cell / 2
            pulse = 0.5 + 0.5 * math.sin(self.bg_t * 4)
            r = cell * (0.28 + 0.05 * pulse)
            pygame.draw.circle(surface, COL_GOAL, (gcx, gcy), r)
            pygame.draw.circle(surface, (255, 255, 255), (gcx, gcy), r, 2)

        # player
        pcx = ox + self.player_anim_pos[0] * cell + cell / 2
        pcy = oy + self.player_anim_pos[1] * cell + cell / 2
        glow_r = cell * 0.55
        glow_surf = pygame.Surface((glow_r * 2, glow_r * 2), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (*COL_PLAYER, 70), (glow_r, glow_r), glow_r)
        surface.blit(glow_surf, (pcx - glow_r, pcy - glow_r))
        pygame.draw.circle(surface, COL_PLAYER, (pcx, pcy), cell * 0.30)
        pygame.draw.circle(surface, (255, 255, 255), (pcx, pcy), cell * 0.30, 2)

        # vignette / fog darkening beyond radius for atmosphere
        fog = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        fog.fill((5, 6, 12, 235))
        light_r = int((vision + 0.6) * cell)
        pygame.draw.circle(fog, (0, 0, 0, 0), (int(pcx), int(pcy)), light_r)
        # soften edge with a couple of translucent rings
        for i in range(3):
            rr = light_r + i * 10
            pygame.draw.circle(fog, (5, 6, 12, 90), (int(pcx), int(pcy)), rr, 10)
        surface.blit(fog, (0, 0))

        pygame.draw.rect(surface, COL_ACCENT, panel_rect, width=2, border_radius=10)

    def draw_hud(self, surface):
        pygame.draw.rect(surface, COL_PANEL, (0, 0, SCREEN_W, 90))
        pygame.draw.line(surface, COL_ACCENT, (0, 90), (SCREEN_W, 90), 2)

        draw_text(surface, f"Level {self.level_index + 1} / {MAX_LEVEL}", FONT_HUD, COL_TEXT, (110, 30))
        cfg = LEVELS[self.level_index]
        draw_text(surface, f"{cfg['cols']}x{cfg['rows']} maze", FONT_SMALL, COL_TEXT_DIM, (110, 58))

        timer_color = COL_WARN if self.time_left < 10 else COL_TEXT
        mins = int(self.time_left) // 60
        secs = int(self.time_left) % 60
        draw_text(surface, f"Time  {mins:01d}:{secs:02d}", FONT_HUD, timer_color, (SCREEN_W // 2 - 140, 30))
        draw_text(surface, f"Moves  {self.moves}", FONT_SMALL, COL_TEXT_DIM, (SCREEN_W // 2 - 140, 58))

        draw_text(surface, f"Score  {self.score}", FONT_HUD, COL_GOLD, (SCREEN_W // 2 + 110, 30))

        # lives as hearts
        for i in range(3):
            hx = SCREEN_W - 160 + i * 40
            hy = 30
            col = COL_WARN if i < self.lives else (70, 74, 90)
            self._draw_heart(surface, hx, hy, 14, col)

        draw_text(surface, "ESC/P Pause", FONT_SMALL, COL_TEXT_DIM, (SCREEN_W - 90, 62))

        self.draw_minimap(surface)

    def _draw_heart(self, surface, x, y, size, color):
        points = []
        for t in range(0, 360, 12):
            rad = math.radians(t)
            hx = size * (16 * math.sin(rad) ** 3) / 16
            hy = -size * (13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)) / 16
            points.append((x + hx, y + hy))
        pygame.draw.polygon(surface, color, points)

    def draw_minimap(self, surface):
        cfg = LEVELS[self.level_index]
        map_w, map_h = 150, 110
        mx, my = SCREEN_W - map_w - 20, SCREEN_H - map_h - 16
        panel = pygame.Rect(mx - 6, my - 6, map_w + 12, map_h + 12)
        s = pygame.Surface((panel.w, panel.h), pygame.SRCALPHA)
        pygame.draw.rect(s, (10, 12, 22, 210), (0, 0, panel.w, panel.h), border_radius=8)
        surface.blit(s, panel.topleft)
        pygame.draw.rect(surface, COL_ACCENT, panel, width=1, border_radius=8)

        cw = map_w / cfg['cols']
        ch = map_h / cfg['rows']
        for (x, y) in self.explored:
            pygame.draw.rect(surface, (60, 66, 92), (mx + x * cw, my + y * ch, max(1, cw), max(1, ch)))
        gx, gy = self.goal_pos
        if self.goal_pos in self.explored:
            pygame.draw.circle(surface, COL_GOAL, (mx + gx * cw + cw / 2, my + gy * ch + ch / 2), 3)
        px, py = self.player_pos
        pygame.draw.circle(surface, COL_PLAYER, (mx + px * cw + cw / 2, my + py * ch + ch / 2), 3)

    # ---------------- screens ----------------
    def draw_menu(self, surface, mouse_pos):
        self.draw_background(surface)
        t = pygame.time.get_ticks() / 1000
        for i in range(6):
            r = 40 + i * 70 + 10 * math.sin(t + i)
            alpha = 40 - i * 5
            s = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*COL_ACCENT, max(0, alpha)), (r, r), r, 2)
            surface.blit(s, (SCREEN_W // 2 - r, 190 - r))

        draw_text(surface, "LABYRINTH ESCAPE", FONT_TITLE, COL_ACCENT, (SCREEN_W // 2, 190))
        draw_text(surface, "8 levels · shrinking vision · escalating pressure", FONT_SMALL, COL_TEXT_DIM,
                   (SCREEN_W // 2, 245))
        for b in self.menu_buttons:
            b.update(mouse_pos)
            b.draw(surface)
        draw_text(surface, "A very hard maze escape game", FONT_SMALL, COL_TEXT_DIM, (SCREEN_W // 2, 660))

    def draw_instructions(self, surface, mouse_pos):
        self.draw_background(surface)
        draw_text(surface, "How To Play", FONT_BIG, COL_ACCENT, (SCREEN_W // 2, 90))
        lines = [
            "Move with Arrow Keys or WASD.",
            "Reach the glowing GOLD ORB to complete each level.",
            "",
            "Your vision is limited by a fog of war — it shrinks as levels progress.",
            "Explored paths stay dimly visible on the minimap (bottom-right).",
            "",
            "Beat the clock! Running out of time costs a life.",
            "",
            "You have 3 lives. Lose them all and it's game over.",
            "Finish faster and with fewer moves for a higher score!",
        ]
        y = 160
        for line in lines:
            color = COL_TEXT if line else COL_TEXT
            draw_text(surface, line, FONT_SMALL, color, (SCREEN_W // 2, y))
            y += 32
        self.instructions_back.update(mouse_pos)
        self.instructions_back.draw(surface)

    def draw_pause(self, surface, mouse_pos):
        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        overlay.fill((5, 6, 12, 210))
        surface.blit(overlay, (0, 0))
        draw_text(surface, "Paused", FONT_BIG, COL_ACCENT, (SCREEN_W // 2, 230))
        for b in self.pause_buttons:
            b.update(mouse_pos)
            b.draw(surface)

    def draw_level_complete(self, surface, mouse_pos):
        overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
        overlay.fill((5, 6, 12, 220))
        surface.blit(overlay, (0, 0))
        draw_text(surface, "Level Complete!", FONT_BIG, COL_GOLD, (SCREEN_W // 2, 260))
        draw_text(surface, f"Score: {self.score}", FONT_MED, COL_TEXT, (SCREEN_W // 2, 330))
        draw_text(surface, f"Moves used: {self.moves}", FONT_SMALL, COL_TEXT_DIM, (SCREEN_W // 2, 375))
        self.next_level_button.update(mouse_pos)
        self.next_level_button.draw(surface)

    def draw_game_over(self, surface, mouse_pos):
        self.draw_background(surface)
        draw_text(surface, "Game Over", FONT_BIG, COL_WARN, (SCREEN_W // 2, 260))
        draw_text(surface, self.death_reason or "You ran out of lives.", FONT_SMALL, COL_TEXT_DIM,
                   (SCREEN_W // 2, 320))
        draw_text(surface, f"Final Score: {self.score}", FONT_MED, COL_TEXT, (SCREEN_W // 2, 365))
        for b in self.gameover_buttons:
            b.update(mouse_pos)
            b.draw(surface)

    def draw_win(self, surface, mouse_pos):
        self.draw_background(surface)
        t = pygame.time.get_ticks() / 300
        for i in range(40):
            x = (i * 53 + int(t * 20)) % SCREEN_W
            y = (i * 91) % SCREEN_H
            col = [COL_GOLD, COL_ACCENT, COL_WARN][i % 3]
            pygame.draw.circle(surface, col, (x, y), 3)
        draw_text(surface, "You Escaped!", FONT_TITLE, COL_GOLD, (SCREEN_W // 2, 220))
        draw_text(surface, "You conquered all 8 labyrinths.", FONT_MED, COL_TEXT, (SCREEN_W // 2, 300))
        draw_text(surface, f"Final Score: {self.score}", FONT_MED, COL_ACCENT, (SCREEN_W // 2, 350))
        for b in self.win_buttons:
            b.update(mouse_pos)
            b.draw(surface)


# ---------
# Main loop
# ---------

def main():
    game = Game()
    running = True

    KEYMAP = {
        pygame.K_UP: 'N', pygame.K_w: 'N',
        pygame.K_DOWN: 'S', pygame.K_s: 'S',
        pygame.K_RIGHT: 'E', pygame.K_d: 'E',
        pygame.K_LEFT: 'W', pygame.K_a: 'W',
    }

    while running:
        dt = clock.tick(FPS) / 1000.0
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True
            elif event.type == pygame.KEYDOWN:
                if event.key in KEYMAP and game.state == STATE_PLAYING:
                    game.try_move_player(KEYMAP[event.key])
                elif event.key in (pygame.K_ESCAPE, pygame.K_p):
                    if game.state == STATE_PLAYING:
                        game.state = STATE_PAUSED
                    elif game.state == STATE_PAUSED:
                        game.state = STATE_PLAYING
                elif event.key == pygame.K_r and game.state in (STATE_PAUSED,):
                    game.restart_level()

        # Poll held movement keys as well as handling KEYDOWN.  The cooldown
        # keeps this responsive without making a held key move too quickly.
        if game.state == STATE_PLAYING:
            held = pygame.key.get_pressed()
            for key, direction in (
                (pygame.K_UP, 'N'), (pygame.K_w, 'N'),
                (pygame.K_DOWN, 'S'), (pygame.K_s, 'S'),
                (pygame.K_RIGHT, 'E'), (pygame.K_d, 'E'),
                (pygame.K_LEFT, 'W'), (pygame.K_a, 'W'),
            ):
                if held[key]:
                    game.try_move_player(direction)
                    break

        # ---- state machine ----
        if game.state == STATE_MENU:
            game.draw_menu(screen, mouse_pos)
            if game.menu_buttons[0].clicked(mouse_pos, mouse_click):
                game.full_restart()
            elif game.menu_buttons[1].clicked(mouse_pos, mouse_click):
                game.state = STATE_INSTRUCTIONS
            elif game.menu_buttons[2].clicked(mouse_pos, mouse_click):
                running = False

        elif game.state == STATE_INSTRUCTIONS:
            game.draw_instructions(screen, mouse_pos)
            if game.instructions_back.clicked(mouse_pos, mouse_click):
                game.state = STATE_MENU

        elif game.state == STATE_PLAYING:
            game.update_playing(dt)
            game.draw_background(screen)
            game.draw_maze(screen)
            game.draw_hud(screen)

        elif game.state == STATE_PAUSED:
            # keep the frozen maze visible behind the overlay
            game.draw_background(screen)
            game.draw_maze(screen)
            game.draw_hud(screen)
            game.draw_pause(screen, mouse_pos)
            if game.pause_buttons[0].clicked(mouse_pos, mouse_click):
                game.state = STATE_PLAYING
            elif game.pause_buttons[1].clicked(mouse_pos, mouse_click):
                game.restart_level()
            elif game.pause_buttons[2].clicked(mouse_pos, mouse_click):
                game.state = STATE_MENU

        elif game.state == STATE_LEVEL_COMPLETE:
            game.draw_background(screen)
            game.draw_maze(screen)
            game.draw_hud(screen)
            game.draw_level_complete(screen, mouse_pos)
            if game.next_level_button.clicked(mouse_pos, mouse_click):
                game.load_level(game.level_index + 1)

        elif game.state == STATE_GAME_OVER:
            game.draw_game_over(screen, mouse_pos)
            if game.gameover_buttons[0].clicked(mouse_pos, mouse_click):
                game.full_restart()
            elif game.gameover_buttons[1].clicked(mouse_pos, mouse_click):
                game.state = STATE_MENU

        elif game.state == STATE_WIN:
            game.draw_win(screen, mouse_pos)
            if game.win_buttons[0].clicked(mouse_pos, mouse_click):
                game.full_restart()
            elif game.win_buttons[1].clicked(mouse_pos, mouse_click):
                game.state = STATE_MENU

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()