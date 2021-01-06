"""
Game specific functions and constants

Do not change these constants directly as other parts of the game rely on their correct format
"""

from pygame import Color
from point import P
from settings import *
from form import FORM

############## Custom types ##############

# actions that can be performed by a plyer at any given time
ACT = {'NOTHING': P(0, 0), None: P(0, 0),
       'MOVE_U': P(0, -1), 'MOVE_D': P(0, 1), 'MOVE_L': P(-1, 0), 'MOVE_R': P(1, 0),
       'SHOOT_Q': P(-0.707, -0.707), 'SHOOT_W': P(0, -1), 'SHOOT_E': P(0.707, -0.707), 'SHOOT_A': P(-1, 0),
       'SHOOT_D': P(1, 0), 'SHOOT_Z': P(-0.707, 0.707), 'SHOOT_X': P(0, 1), 'SHOOT_C': P(0.707, 0.707)}
# 0.717 = 1/sqrt(2)

"""
Meta actions that a player can perform

necessary for multiplayer modes  as these actions must be
checked at the player / team level instead of the game level
"""
META_ACT = {'QUIT', 'PAUSE', 'TOGGLE_FORM', 'TOGGLE_DEBUG', 'FORM'}

############## Functions ##############

def add_rewards(d1, d2):
    return {
        1: [d1[1][i] + d2[1][i]for i in range(NUM_TEAM)],
        2: [d1[2][i] + d2[2][i]for i in range(NUM_TEAM)],
    }

def recolor(surface, color=(255, 108, 0)):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            val = surface.get_at((x, y))
            surface.set_at((x, y), Color(r, g, b, val[3]))


def draw_form(win, curr_form):
    win.fill((14, 156, 23))  # constant green
    pygame.draw.rect(win, (255, 255, 255), (0, 0, W -
                                            LINE_WIDTH, H - LINE_WIDTH), LINE_WIDTH)  # border
    pygame.draw.rect(win, (255, 255, 255),
                     (W//2 - LINE_WIDTH//2, 0, LINE_WIDTH, H))  # mid line
    pygame.draw.circle(win, (255, 255, 255), (W//2, H//2),
                       H//5, LINE_WIDTH)  # mid circle
    pygame.draw.rect(win, (255, 255, 255), (4*W//5-LINE_WIDTH //
                                            2, 0.1*H, W//5, 0.8*H), LINE_WIDTH)  # right D
    pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2,
                                            0.1*H, W//5, 0.8*H), LINE_WIDTH)  # left D
    pygame.draw.rect(win, (255, 255, 255), (19*W//20-LINE_WIDTH//2,
                                            GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH)  # right goal
    pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2,
                                            GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH)  # right goal
    for pos in FORM[curr_form]['L']:
        win.blit(RUN[1]['L'][0]['full'], (pos - PLAYER_CENTER).val)

######################################
