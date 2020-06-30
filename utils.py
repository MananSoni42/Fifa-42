import pygame
import numpy as np
from point import P

"""
Utilities: Contains global settings and constants
"""

############## Settings ##############
NUM_TEAM = 7 # Number of players in a team
W = 1024 # Width
H = 568 # Height
FPS = 27

PLAYER_SPEED = 3
PLAYER_RADIUS = 30
PLAYER_CENTER = P(PLAYER_RADIUS, PLAYER_RADIUS)

BALL_SPEED = 5
BALL_RADIUS = 10
BALL_CENTER = P(BALL_RADIUS, BALL_RADIUS)
BALL_OFFSET = P(3, 1.5)

GOAL_POS = [0.3,0.7] # goalpost positions in percentage
LINE_WIDTH = 2
ASSET_DIR = './assets/' # Path to where the images are stored
ANIM_NUM = 7 # Number of images used for running animation
WALK_DELAY = 3 # Change walking sprite after X presses
######################################



############## Functions ##############
def recolor(surface, color=(255,128,0)):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            val = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(r, g, b, val[3]))

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




############## Images ##############
BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(ASSET_DIR + "field.png"), (W, H))
FOOTBALL_IMG = pygame.transform.scale(pygame.image.load(ASSET_DIR + "football.png"), (2*BALL_RADIUS, 2*BALL_RADIUS))
RUN = {
    1: {
        'L': { i: pygame.transform.scale(pygame.image.load(ASSET_DIR + f'running/l{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7) },
        'R': { i: pygame.transform.scale(pygame.image.load(ASSET_DIR + f'running/r{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7) },
    },
    2: {
        'L': { i: pygame.transform.scale(pygame.image.load(ASSET_DIR + f'running/l{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7) },
        'R': { i: pygame.transform.scale(pygame.image.load(ASSET_DIR + f'running/r{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7) },
    },
}
######################################



############## Custom types ##############

# actions that can be performed by a plyer at any given time
ACT = { 'NOTHING': (0,0), None: (0,0),
        'MOVE_U': (0,-1), 'MOVE_D': (0,1), 'MOVE_L': (-1,0), 'MOVE_R': (1,0),
        'SHOOT_Q': (-0.707,-0.707), 'SHOOT_W': (0,-1), 'SHOOT_E': (0.707,-0.707), 'SHOOT_A': (-1,0),
        'SHOOT_D': (1,0), 'SHOOT_Z': (-0.707,0.707), 'SHOOT_X': (0,1), 'SHOOT_C': (0.707,0.707) }
# 0.717 = 1/sqrt(2)

# Possible team formations
FORM = {
    'default-left': [P(50,H//2), P(W//4,H//5), P(W//4, H//2), P(W//4, 4*H//5), P(W//2,H//3), P(W//2, 2*H//3), P(3*W//4,H//2)],
    'default-right': [P(W-50,H//2), P(3*W//4,H//5), P(3*W//4, H//2), P(3*W//4, 4*H//5), P(W//2,H//3), P(W//2, 2*H//3), P(W//4,H//2)],
}

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
