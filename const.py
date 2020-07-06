from pygame import Color
from point import P
from settings import *

"""
Important constants used in the game
"""

############## Functions ##############
def recolor(surface, color=(255,128,0)):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            val = surface.get_at((x, y))
            surface.set_at((x, y), Color(r, g, b, val[3]))

def get_possession(pos):
    if pos[1]+pos[2] == 0:
        team1_pos = 0.5
    else:
        team1_pos = int(round(pos[1]/(pos[1]+pos[2]),0))
    return team1_pos, 1-team1_pos

def get_pass_acc(ballpass):
    if ballpass[1]['succ'] + ballpass[1]['fail'] == 0:
        team1_pass = 0
    else:
        team1_pass = round(ballpass[1]['succ']/(ballpass[1]['succ']+ballpass[1]['fail']),2)

    if ballpass[2]['succ'] + ballpass[2]['fail'] == 0:
        team2_pass = 0
    else:
        team2_pass = round(ballpass[2]['succ']/(ballpass[2]['succ']+ballpass[2]['fail']),2)

    return team1_pass, team2_pass

def get_shot_acc(shot):
    if shot[1]['succ'] + shot[1]['fail'] == 0:
        team1_shot = 0
    else:
        team1_shot = round(shot[1]['succ']/(shot[1]['succ']+shot[1]['fail']),2)

    if shot[2]['succ'] + shot[2]['fail'] == 0:
        team2_shot = 0
    else:
        team2_shot = round(shot[2]['succ']/(shot[2]['succ']+shot[2]['fail']),2)

    return team1_shot, team2_shot
######################################





############## Custom types ##############

# actions that can be performed by a plyer at any given time
ACT = { 'NOTHING': (0,0), None: (0,0),
        'MOVE_U': (0,-1), 'MOVE_D': (0,1), 'MOVE_L': (-1,0), 'MOVE_R': (1,0),
        'SHOOT_Q': (-0.707,-0.707), 'SHOOT_W': (0,-1), 'SHOOT_E': (0.707,-0.707), 'SHOOT_A': (-1,0),
        'SHOOT_D': (1,0), 'SHOOT_Z': (-0.707,0.707), 'SHOOT_X': (0,1), 'SHOOT_C': (0.707,0.707) }
# 0.717 = 1/sqrt(2)

"""
Team formations
    - Must start with the keeper
    - Must contain positions for both left and right sides
    - Recommended to specify completley in terms of W and H (and PLAYER_RADIUS if reqd)
"""
FORM = {
    'default': {
            'L': [P(2*PLAYER_RADIUS + BALL_RADIUS,H//2), P(W//4,H//5), P(W//4, H//2), P(W//4, 4*H//5), P(W//2,H//3), P(W//2, 2*H//3), P(3*W//4,H//2)],
            'R': [P(W - 2*PLAYER_RADIUS - BALL_RADIUS,H//2), P(3*W//4,H//5), P(3*W//4, H//2), P(3*W//4, 4*H//5), P(W//2,H//3), P(W//2, 2*H//3), P(W//4,H//2)],
        }

}

# Number of goals
GOALS = { 1: 0, 2: 0 }

# Global Stats
POSSESSION = { 1: 0, 2: 0 }

PASS_ACC = {
    1: {
        'succ': 0,
        'fail': 0
    },
    2: {
        'succ': 0,
        'fail': 0
    },
}

SHOT_ACC = {
    1: {
        'succ': 0,
        'fail': 0
    },
    2: {
        'succ': 0,
        'fail': 0
    },
}
######################################
