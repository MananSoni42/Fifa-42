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

def get_possession(pos, printpos=False):
    if pos[1]+pos[2] == 0:
        team1_pos = 50
    else:
        team1_pos = int(round(100*pos[1]/(pos[1]+pos[2]),0))
    if printpos:
        print(f'Possession: Team 1: {team1_pos} % Team 2: {100-team1_pos} %')
    return team1_pos, 100-team1_pos

def get_pass_acc(ballpass, printpass=False):
    if ballpass[1]['succ'] + ballpass[1]['fail'] == 0:
        team1_pass = 0
    else:
        team1_pass = round(100*ballpass[1]['succ']/(ballpass[1]['succ']+ballpass[1]['fail']),2)

    if ballpass[2]['succ'] + ballpass[2]['fail'] == 0:
        team2_pass = 0
    else:
        team2_pass = round(100*ballpass[2]['succ']/(ballpass[2]['succ']+ballpass[2]['fail']),2)
    if printpass:
        print(f'Passing accuracy: Team 1: {team1_pass} % Team 2: {team2_pass} %')
    return team1_pass, team2_pass

def get_shot_acc(shot, printshot=False):
    if shot[1]['succ'] + shot[1]['fail'] == 0:
        team1_shot = 0
    else:
        team1_shot = round(100*shot[1]['succ']/(shot[1]['succ']+shot[1]['fail']),2)

    if shot[2]['succ'] + shot[2]['fail'] == 0:
        team2_shot = 0
    else:
        team2_shot = round(100*shot[2]['succ']/(shot[2]['succ']+shot[2]['fail']),2)
    if printshot:
        print(f'Passing accuracy: Team 1: {team1_shot} % Team 2: {team2_shot} %')
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
    - Recommended to specify completley in terms of W and H (and PLAYER_RADIUS if reqd)
"""
FORM = {
    'default-left': [P(PLAYER_RADIUS + W//100,H//2), P(W//4,H//5), P(W//4, H//2), P(W//4, 4*H//5), P(W//2,H//3), P(W//2, 2*H//3), P(3*W//4,H//2)],
    'default-right': [P(99*W//100 - PLAYER_RADIUS,H//2), P(3*W//4,H//5), P(3*W//4, H//2), P(3*W//4, 4*H//5), P(W//2,H//3), P(W//2, 2*H//3), P(W//4,H//2)],
}

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
