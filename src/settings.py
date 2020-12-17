import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
from point import P

"""
Settings and paths
"""

############## Settings ##############
NUM_TEAM = 7 # Number of players in a team
W = 1024 # Width
H = 568 # Height
FPS = 42
ASSET_DIR = './assets/' # Path to assets
FONT_PATH = ASSET_DIR + 'Roboto-Black.ttf' # Path to font file

SCALE = 5
GX,GY,GZ = (W/SCALE, 0, H/SCALE)
CAM_ADD = (-GX/2, 0, -150)
CAM_POS = CAM_ADD
CAM_ANG = 35
CAM_POST = (0,10,-20)

PLAYER_SPEED = 3
PLAYER_RADIUS = 20
PLAYER_CENTER = P(PLAYER_RADIUS, PLAYER_RADIUS)
PLAYER_WIDTH = 7

BALL_SPEED = 7
BALL_RADIUS = 7
BALL_CENTER = P(BALL_RADIUS, BALL_RADIUS)
BALL_OFFSET = P(2.5,0)

GOAL_DISP_SIZE = 60
FONT_SIZE = 45
GOAL_POS = [0.3,0.7] # goalpost positions in percentage of H
LINE_WIDTH = 2
ANIM_NUM = 7 # Number of images used for running animation
WALK_DELAY = 3 # Change walking sprite after this many presses
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
