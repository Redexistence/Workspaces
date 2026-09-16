#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
掼蛋计分器 (Guandan Scoreboard)
================================

A clean, self-contained Pygame scoreboard for the Chinese card game Guandan (掼蛋).

GUANDAN LEVEL RULES ENCODED HERE
---------------------------------
Both teams start at level "2". The level track is:
    2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A1, A2, A3

Each round (hand), four players finish in order: 1st, 2nd, 3rd, 4th place.
Only the team containing the 1st-place finisher can advance levels, based on
where their partner finished:

    双上 (Double Up)   -> partner finished 2nd  -> team advances +3 levels
    1st & 3rd           -> partner finished 3rd  -> team advances +2 levels
    1st & 4th           -> partner finished 4th  -> team advances +1 level

The losing team does not move.

SPECIAL "A" (ACE) RULE
-----------------------
Reaching level A is special. The first time a team crosses into the A zone
(from K or below), they always land on exactly A1, no matter how big the
jump was that round.

Once a team is already sitting at A1 / A2 / A3 at the START of a round:
    - A 双上 or 1st-&-3rd result WINS THE ENTIRE GAME immediately.
    - A 1st-&-4th (weak) result does NOT win the game - it only nudges the
      team up one A sub-stage (A1 -> A2 -> A3). At A3, a weak win keeps the
      team at A3 (they must land a strong result to close out the game).

This mirrors the real Guandan rule that "打A" (playing at Ace) requires a
clean/strong win to actually finish the match - a narrow win just isn't
good enough once you're defending at Ace level.

Run with:  python guandan_scoreboard.py
Requires:  pygame  (pip install pygame)
Note: for the Chinese text to render correctly, your system needs a CJK
font installed (e.g. Microsoft YaHei / SimHei on Windows, PingFang SC on
macOS, Noto Sans CJK on Linux). The script tries several common names.
"""

import os
import sys
import pygame

# Must be set before pygame.init() - tells SDL to let the OS draw the IME
# composition/candidate window. Without this, some IMEs (notably Microsoft
# Pinyin on Windows) silently fail to compose text in SDL windows.
os.environ.setdefault("SDL_IME_SHOW_UI", "1")

# --------------------------------------------------------------------------
# Setup
# --------------------------------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("掼蛋计分器 - Guandan Scoreboard")
clock = pygame.time.Clock()
FPS = 60

# Make sure text input (needed for IME composition) starts disabled until
# a text box is actually focused - see set_active_input() below.
pygame.key.stop_text_input()

# ---- Colors ----------------------------------------------------------------
BG = (245, 246, 250)
PANEL_LEFT = (232, 240, 253)
PANEL_RIGHT = (253, 236, 233)
ACCENT_LEFT = (52, 108, 214)
ACCENT_RIGHT = (214, 92, 62)
TEXT_DARK = (40, 44, 52)
TEXT_MUTED = (120, 126, 138)
WHITE = (255, 255, 255)
DIVIDER = (210, 213, 220)
BTN_GREEN = (61, 174, 118)
BTN_GREEN_HOVER = (48, 152, 100)
BTN_BLUE = (66, 133, 224)
BTN_BLUE_HOVER = (48, 112, 202)
BTN_GRAY = (150, 158, 172)
BTN_GRAY_HOVER = (128, 136, 150)
BTN_DARK = (60, 66, 78)
BTN_DARK_HOVER = (44, 49, 60)
GOLD = (222, 176, 63)
CHIP_BG = (255, 255, 255)
CHIP_BORDER = (215, 218, 226)

# ---- Fonts (try to find a CJK-capable font) --------------------------------
CJK_CANDIDATES = [
    "Noto Sans CJK SC", "Noto Sans CJK", "Microsoft YaHei", "SimHei",
    "PingFang SC", "PingFang", "Heiti SC", "WenQuanYi Zen Hei",
    "Droid Sans Fallback", "Arial Unicode MS",
]

def find_cjk_font_path():
    for name in CJK_CANDIDATES:
        path = pygame.font.match_font(name)
        if path:
            return path
    return None

_CJK_PATH = find_cjk_font_path()

def font(size, bold=False):
    if _CJK_PATH:
        f = pygame.font.Font(_CJK_PATH, size)
        f.set_bold(bold)
        return f
    f = pygame.font.SysFont(None, size)
    f.set_bold(bold)
    return f

FONT_TITLE = font(72, bold=True)
FONT_SUBTITLE = font(24)
FONT_H2 = font(34, bold=True)
FONT_TEAM_NAME = font(30, bold=True)
FONT_LEVEL_BIG = font(120, bold=True)
FONT_LEVEL_BIG_A = font(84, bold=True)  # smaller for "A1"/"A2"/"A3" (wider text)
FONT_BTN = font(24, bold=True)
FONT_BTN_SMALL = font(18)
FONT_CHIP = font(16, bold=True)
FONT_SMALL = font(18)
FONT_TINY = font(15)
FONT_WIN = font(64, bold=True)

# --------------------------------------------------------------------------
# Game data
# --------------------------------------------------------------------------
LEVELS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
          "A1", "A2", "A3"]
A_ZONE_START = 12  # index of "A1"

def make_team(default_name):
    return {"name": default_name, "level_idx": 0, "won": False}

teams = [make_team("队伍一"), make_team("队伍二")]

STATE_TITLE = "title"
STATE_NAMES = "names"
STATE_GAME = "game"
STATE_WIN = "win"
state = STATE_TITLE

active_input = None  # 0 or 1 while on the names screen
history = []          # stack of (team_index, prev_level_idx, prev_won) for undo
show_rules_overlay = False
winner_name = ""

# --------------------------------------------------------------------------
# Core scoring logic
# --------------------------------------------------------------------------
def apply_result(team_idx, points):
    """Apply a round result (points = 3, 2, or 1) to the given team."""
    global state, winner_name
    team = teams[team_idx]
    history.append((team_idx, team["level_idx"], team["won"]))

    idx = team["level_idx"]
    if idx < A_ZONE_START:
        new_idx = idx + points
        if new_idx >= A_ZONE_START:
            # Crossing into the A zone always lands exactly on A1
            team["level_idx"] = A_ZONE_START
        else:
            team["level_idx"] = new_idx
    else:
        # Already defending at A1/A2/A3
        if points >= 2:
            team["won"] = True
            winner_name = team["name"]
            state = STATE_WIN
        else:
            if idx >= A_ZONE_START + 2:
                # Weak win at A3 fails the Ace attempt entirely - back to level 2
                team["level_idx"] = 0
            else:
                team["level_idx"] = idx + 1


def undo_last():
    global state
    if not history:
        return
    team_idx, prev_idx, prev_won = history.pop()
    teams[team_idx]["level_idx"] = prev_idx
    teams[team_idx]["won"] = prev_won
    if state == STATE_WIN:
        state = STATE_GAME


def reset_all():
    global state, history, teams
    teams[0]["level_idx"] = 0
    teams[0]["won"] = False
    teams[1]["level_idx"] = 0
    teams[1]["won"] = False
    history.clear()
    state = STATE_TITLE


# --------------------------------------------------------------------------
# Drawing helpers
# --------------------------------------------------------------------------
def draw_text(surface, text, fnt, color, center=None, topleft=None):
    surf = fnt.render(text, True, color)
    rect = surf.get_rect()
    if center:
        rect.center = center
    if topleft:
        rect.topleft = topleft
    surface.blit(surf, rect)
    return rect


def rounded_button(surface, rect, text, base_color, hover_color, fnt,
                    text_color=WHITE, mouse_pos=(0, 0), subtext=None):
    hovered = rect.collidepoint(mouse_pos)
    color = hover_color if hovered else base_color
    pygame.draw.rect(surface, color, rect, border_radius=14)
    if subtext:
        t1 = fnt.render(text, True, text_color)
        t2 = FONT_BTN_SMALL.render(subtext, True, text_color)
        r1 = t1.get_rect(center=(rect.centerx, rect.centery - 10))
        r2 = t2.get_rect(center=(rect.centerx, rect.centery + 14))
        surface.blit(t1, r1)
        surface.blit(t2, r2)
    else:
        draw_text(surface, text, fnt, text_color, center=rect.center)
    return rect, hovered


def draw_star(surface, center, outer_r, color, rotation=-90):
    import math
    cx, cy = center
    inner_r = outer_r * 0.42
    points = []
    for i in range(10):
        angle_deg = rotation + i * 36
        r = outer_r if i % 2 == 0 else inner_r
        angle = math.radians(angle_deg)
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    pygame.draw.polygon(surface, color, points)


def draw_level_track(surface, level_idx, cx, top_y, accent):
    """Small horizontal chip track showing all 15 levels with current one highlighted."""
    n = len(LEVELS)
    chip_w, chip_h, gap = 26, 26, 4
    total_w = n * chip_w + (n - 1) * gap
    x0 = cx - total_w // 2
    for i, lab in enumerate(LEVELS):
        x = x0 + i * (chip_w + gap)
        rect = pygame.Rect(x, top_y, chip_w, chip_h)
        if i == level_idx:
            pygame.draw.rect(surface, accent, rect, border_radius=6)
            txt_color = WHITE
        else:
            pygame.draw.rect(surface, CHIP_BG, rect, border_radius=6)
            pygame.draw.rect(surface, CHIP_BORDER, rect, 1, border_radius=6)
            txt_color = TEXT_MUTED
        label = lab if len(lab) <= 2 else lab
        fnt = FONT_TINY if len(lab) <= 2 else FONT_TINY
        draw_text(surface, label, fnt, txt_color, center=rect.center)


# --------------------------------------------------------------------------
# Screen: Title
# --------------------------------------------------------------------------
title_start_btn = pygame.Rect(0, 0, 240, 74)
title_start_btn.center = (WIDTH // 2, HEIGHT - 130)

def draw_title_screen(mouse_pos):
    screen.fill(BG)
    draw_text(screen, "掼蛋计分器", FONT_TITLE, TEXT_DARK,
               center=(WIDTH // 2, HEIGHT // 2 - 110))
    draw_text(screen, "Guandan Score Tracker", FONT_SUBTITLE, TEXT_MUTED,
               center=(WIDTH // 2, HEIGHT // 2 - 40))
    rounded_button(screen, title_start_btn, "Start", BTN_BLUE, BTN_BLUE_HOVER,
                   FONT_H2, mouse_pos=mouse_pos)
    draw_text(screen, "从 2 开始，一路打到 A，先双上/一三名过 A 者获胜",
              FONT_TINY, TEXT_MUTED, center=(WIDTH // 2, HEIGHT - 40))


def handle_title_click(pos):
    global state
    if title_start_btn.collidepoint(pos):
        state = STATE_NAMES


# --------------------------------------------------------------------------
# Screen: Team name entry
# --------------------------------------------------------------------------
input_box_left = pygame.Rect(0, 0, 380, 60)
input_box_left.center = (WIDTH // 4, HEIGHT // 2)
input_box_right = pygame.Rect(0, 0, 380, 60)
input_box_right.center = (WIDTH * 3 // 4, HEIGHT // 2)
confirm_btn = pygame.Rect(0, 0, 240, 70)
confirm_btn.center = (WIDTH // 2, HEIGHT - 110)

def draw_names_screen(mouse_pos):
    screen.fill(BG)
    # panels
    pygame.draw.rect(screen, PANEL_LEFT, (0, 0, WIDTH // 2, HEIGHT))
    pygame.draw.rect(screen, PANEL_RIGHT, (WIDTH // 2, 0, WIDTH // 2, HEIGHT))
    pygame.draw.line(screen, DIVIDER, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

    draw_text(screen, "输入队伍名称", FONT_H2, TEXT_DARK,
               center=(WIDTH // 2, 80))

    draw_text(screen, "队伍一", FONT_TEAM_NAME, ACCENT_LEFT,
               center=(WIDTH // 4, HEIGHT // 2 - 90))
    draw_text(screen, "队伍二", FONT_TEAM_NAME, ACCENT_RIGHT,
               center=(WIDTH * 3 // 4, HEIGHT // 2 - 90))

    for i, box in enumerate([input_box_left, input_box_right]):
        is_active = (active_input == i)
        pygame.draw.rect(screen, WHITE, box, border_radius=10)
        border_color = (ACCENT_LEFT if i == 0 else ACCENT_RIGHT) if is_active else CHIP_BORDER
        pygame.draw.rect(screen, border_color, box, 3 if is_active else 1, border_radius=10)
        name = teams[i]["name"]
        display = name if name else ("点击输入队名" if not is_active else "")
        color = TEXT_DARK if name else TEXT_MUTED
        draw_text(screen, display, FONT_TEAM_NAME, color,
                   center=(box.centerx, box.centery))
        if is_active:
            # blinking cursor feel: draw a simple bar after text
            txt_w = FONT_TEAM_NAME.size(name)[0]
            cursor_x = box.centerx + txt_w // 2 + 4
            if (pygame.time.get_ticks() // 500) % 2 == 0:
                pygame.draw.line(screen, TEXT_DARK,
                                  (cursor_x, box.centery - 18),
                                  (cursor_x, box.centery + 18), 2)

    rounded_button(screen, confirm_btn, "开始记分", BTN_GREEN, BTN_GREEN_HOVER,
                   FONT_H2, mouse_pos=mouse_pos)
    draw_text(screen, "留空则使用默认队名「队伍一 / 队伍二」",
              FONT_TINY, TEXT_MUTED, center=(WIDTH // 2, HEIGHT - 50))


def set_active_input(idx):
    """Focus (idx=0/1) or unfocus (idx=None) a name box, and tell SDL
    where to anchor the IME composition/candidate window. This is required
    for IMEs such as Microsoft Pinyin to work inside a pygame window."""
    global active_input
    active_input = idx
    if idx is None:
        pygame.key.stop_text_input()
    else:
        box = input_box_left if idx == 0 else input_box_right
        pygame.key.start_text_input()
        pygame.key.set_text_input_rect(box)


def handle_names_click(pos):
    global state
    if input_box_left.collidepoint(pos):
        set_active_input(0)
    elif input_box_right.collidepoint(pos):
        set_active_input(1)
    elif confirm_btn.collidepoint(pos):
        if not teams[0]["name"].strip():
            teams[0]["name"] = "队伍一"
        if not teams[1]["name"].strip():
            teams[1]["name"] = "队伍二"
        set_active_input(None)
        state = STATE_GAME
    else:
        set_active_input(None)


def handle_names_key(event):
    global state
    if active_input is None:
        return
    if event.key == pygame.K_BACKSPACE:
        teams[active_input]["name"] = teams[active_input]["name"][:-1]
    elif event.key == pygame.K_TAB:
        set_active_input(1 - active_input)
    elif event.key == pygame.K_RETURN:
        handle_names_click(confirm_btn.center)


def handle_names_textinput(event):
    if active_input is None:
        return
    if len(teams[active_input]["name"]) < 12:
        teams[active_input]["name"] += event.text


# --------------------------------------------------------------------------
# Screen: Main scoreboard / game
# --------------------------------------------------------------------------
def make_result_buttons(cx, top_y):
    """Return list of (rect, points, label, sublabel) for the 3 result buttons."""
    w, h, gap = 260, 64, 14
    labels = [
        (3, "双上", "两人第 1、2 名  +3 级"),
        (2, "一三名", "第 1、3 名  +2 级"),
        (1, "一四名", "第 1、4 名  +1 级"),
    ]
    buttons = []
    y = top_y
    for points, label, sub in labels:
        rect = pygame.Rect(0, 0, w, h)
        rect.center = (cx, y)
        buttons.append((rect, points, label, sub))
        y += h + gap
    return buttons

undo_btn = pygame.Rect(0, 0, 150, 50)
undo_btn.topleft = (24, HEIGHT - 74)
restart_btn = pygame.Rect(0, 0, 150, 50)
restart_btn.topright = (WIDTH - 24, HEIGHT - 74)
rules_btn = pygame.Rect(0, 0, 40, 40)
rules_btn.topright = (WIDTH - 24, 24)

def draw_game_screen(mouse_pos):
    screen.fill(BG)
    pygame.draw.rect(screen, PANEL_LEFT, (0, 0, WIDTH // 2, HEIGHT))
    pygame.draw.rect(screen, PANEL_RIGHT, (WIDTH // 2, 0, WIDTH // 2, HEIGHT))
    pygame.draw.line(screen, DIVIDER, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

    centers = [WIDTH // 4, WIDTH * 3 // 4]
    accents = [ACCENT_LEFT, ACCENT_RIGHT]

    left_buttons = make_result_buttons(centers[0], 470)
    right_buttons = make_result_buttons(centers[1], 470)
    all_buttons = [left_buttons, right_buttons]

    for i in range(2):
        cx = centers[i]
        accent = accents[i]
        team = teams[i]

        # Team name banner
        draw_text(screen, team["name"], FONT_TEAM_NAME, accent, center=(cx, 46))

        # Level track (mini chips)
        draw_level_track(screen, team["level_idx"], cx, 84, accent)

        # Big level number
        label = LEVELS[team["level_idx"]]
        big_font_to_use = FONT_LEVEL_BIG if len(label) == 1 or label in ("10", "J", "Q", "K") else FONT_LEVEL_BIG_A
        draw_text(screen, label, big_font_to_use, TEXT_DARK, center=(cx, 245))

        if team["level_idx"] >= A_ZONE_START:
            draw_text(screen, "打 A 中：双上/一三名 直接获胜！", FONT_TINY, GOLD,
                       center=(cx, 320))
        if team["level_idx"] == A_ZONE_START + 2:
            draw_text(screen, "注意：A3 再打一四名将打 A 失败，打回级别 2！",
                       FONT_TINY, ACCENT_RIGHT, center=(cx, 344))

        # Result buttons
        for rect, points, lab, sub in all_buttons[i]:
            base = BTN_GREEN if points == 3 else (BTN_BLUE if points == 2 else BTN_GRAY)
            hov = BTN_GREEN_HOVER if points == 3 else (BTN_BLUE_HOVER if points == 2 else BTN_GRAY_HOVER)
            rounded_button(screen, rect, f"{lab}  +{points}", hov if rect.collidepoint(mouse_pos) else base,
                            hov, FONT_BTN, mouse_pos=mouse_pos, subtext=sub)

    # bottom bar buttons
    rounded_button(screen, undo_btn, "撤销", BTN_DARK, BTN_DARK_HOVER, FONT_BTN_SMALL, mouse_pos=mouse_pos)
    rounded_button(screen, restart_btn, "再来一局", BTN_DARK, BTN_DARK_HOVER, FONT_BTN_SMALL, mouse_pos=mouse_pos)
    rounded_button(screen, rules_btn, "?", BTN_DARK, BTN_DARK_HOVER, FONT_BTN, mouse_pos=mouse_pos)

    if show_rules_overlay:
        draw_rules_overlay(mouse_pos)

    return all_buttons


def draw_rules_overlay(mouse_pos):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    panel = pygame.Rect(0, 0, 700, 460)
    panel.center = (WIDTH // 2, HEIGHT // 2)
    pygame.draw.rect(screen, WHITE, panel, border_radius=18)
    pygame.draw.rect(screen, CHIP_BORDER, panel, 2, border_radius=18)

    draw_text(screen, "掼蛋升级规则", FONT_H2, TEXT_DARK, center=(panel.centerx, panel.top + 45))

    lines = [
        "级别顺序：2→3→4→...→10→J→Q→K→A1→A2→A3",
        "",
        "每局结束按本方两人的名次决定升级：",
        "  双上 (1、2 名)      本队 +3 级",
        "  一三名 (1、3 名)    本队 +2 级",
        "  一四名 (1、4 名)    本队 +1 级",
        "输的一方本局不掉级，级别不变。",
        "",
        "打 A 特别规则：",
        "从 K 及以下升到 A，一律先落在 A1。",
        "已经处于 A1 / A2 / A3 时：",
        "  双上 或 一三名 → 直接获胜，游戏结束！",
        "  一四名 → 只能小升一档 (A1→A2→A3)，不能获胜。",
        "  若已在 A3 时再打一四名 → 打 A 失败，",
        "           等级直接打回 2，需要重新开始爬升。",
    ]
    y = panel.top + 90
    for line in lines:
        draw_text(screen, line, FONT_SMALL, TEXT_DARK, topleft=(panel.left + 40, y))
        y += 26

    draw_text(screen, "点击「?」关闭", FONT_TINY, TEXT_MUTED,
               center=(panel.centerx, panel.bottom - 26))


def handle_game_click(pos, all_buttons):
    global show_rules_overlay
    if show_rules_overlay:
        if rules_btn.collidepoint(pos):
            show_rules_overlay = False
        return
    if rules_btn.collidepoint(pos):
        show_rules_overlay = True
        return
    if undo_btn.collidepoint(pos):
        undo_last()
        return
    if restart_btn.collidepoint(pos):
        reset_all()
        return
    for team_idx, buttons in enumerate(all_buttons):
        for rect, points, lab, sub in buttons:
            if rect.collidepoint(pos):
                apply_result(team_idx, points)
                return


# --------------------------------------------------------------------------
# Screen: Win
# --------------------------------------------------------------------------
play_again_btn = pygame.Rect(0, 0, 260, 70)
play_again_btn.center = (WIDTH // 2, HEIGHT - 140)

def draw_win_screen(mouse_pos):
    screen.fill((28, 32, 40))
    star_cx = WIDTH // 2
    star_cy = HEIGHT // 2 - 190
    draw_star(screen, (star_cx - 90, star_cy + 20), 16, GOLD)
    draw_star(screen, (star_cx + 100, star_cy + 10), 20, GOLD)
    draw_star(screen, (star_cx, star_cy), 34, GOLD)
    draw_text(screen, f"{winner_name}  获胜！", FONT_WIN, GOLD,
               center=(WIDTH // 2, HEIGHT // 2 - 60))
    draw_text(screen, "恭喜获得本局最终胜利", FONT_SUBTITLE, WHITE,
               center=(WIDTH // 2, HEIGHT // 2 + 10))
    rounded_button(screen, play_again_btn, "再来一局", BTN_GREEN, BTN_GREEN_HOVER,
                   FONT_H2, mouse_pos=mouse_pos)


def handle_win_click(pos):
    if play_again_btn.collidepoint(pos):
        reset_all()


# --------------------------------------------------------------------------
# Main loop
# --------------------------------------------------------------------------
def main():
    global state
    pending_buttons = None
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == STATE_TITLE:
                    handle_title_click(event.pos)
                elif state == STATE_NAMES:
                    handle_names_click(event.pos)
                elif state == STATE_GAME:
                    if pending_buttons is not None:
                        handle_game_click(event.pos, pending_buttons)
                elif state == STATE_WIN:
                    handle_win_click(event.pos)

            elif event.type == pygame.KEYDOWN:
                if state == STATE_NAMES:
                    handle_names_key(event)
                elif event.key == pygame.K_ESCAPE and state == STATE_GAME:
                    global show_rules_overlay
                    show_rules_overlay = False

            elif event.type == pygame.TEXTINPUT:
                if state == STATE_NAMES:
                    handle_names_textinput(event)

        if state == STATE_TITLE:
            draw_title_screen(mouse_pos)
        elif state == STATE_NAMES:
            draw_names_screen(mouse_pos)
        elif state == STATE_GAME:
            pending_buttons = draw_game_screen(mouse_pos)
        elif state == STATE_WIN:
            draw_win_screen(mouse_pos)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()