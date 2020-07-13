import pygame
import numpy as np
from point import P
from screeninfo import get_monitors

"""
Settings and paths
"""

############## Settings ##############
NUM_TEAM = 11 # Number of players in a team
FONT_SIZE = 45
W = get_monitors()[0].width # Width
H = 9*get_monitors()[0].height//10 # Height
FPS = 27

PLAYER_SPEED = 3
PLAYER_RADIUS = 20
PLAYER_CENTER = P(PLAYER_RADIUS, PLAYER_RADIUS)

BALL_SPEED = 7
BALL_RADIUS = 7
BALL_CENTER = P(BALL_RADIUS, BALL_RADIUS)
BALL_OFFSET = P(2, 1.5)

GOAL_DISP_SIZE = 60
GOAL_POS = [0.3,0.7] # goalpost positions in percentage of H
LINE_WIDTH = 2
ANIM_NUM = 7 # Number of images used for running animation
WALK_DELAY = 3 # Change walking sprite after this many presses
######################################



############## Assets (images, fonts, sounds) ##############
ASSET_DIR = './assets/' # Path to assets
IMG_DIR = ASSET_DIR + 'img/'
SOUND_DIR = ASSET_DIR + 'sound/'

FONT_PATH = ASSET_DIR + 'fonts/Roboto-Black.ttf'

MENU_BG = IMG_DIR + 'menu_bg.jpg'
CONTROLS_IMG = IMG_DIR + 'controls.png'
GET_FORM_BG = lambda team_id, formation_id: IMG_DIR + f'formations/{team_id}-{formation_id}.jpg' # Get correct formation img
BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(IMG_DIR + "field.png"), (W, H)) # Background (not used currently)
FOOTBALL_IMG = pygame.transform.scale(pygame.image.load(IMG_DIR + "football.png"), (2*BALL_RADIUS, 2*BALL_RADIUS))
RUN = { # Sprites that animate the running player
    1: {
        'L': { i: pygame.transform.scale(pygame.image.load(IMG_DIR + f'running/l{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7) },
        'R': { i: pygame.transform.scale(pygame.image.load(IMG_DIR + f'running/r{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7) },
    },
    2: {
        'L': { i: pygame.transform.scale(pygame.image.load(IMG_DIR + f'running/l{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7) },
        'R': { i: pygame.transform.scale(pygame.image.load(IMG_DIR + f'running/r{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7) },
    },
}

SOUND_CROWD = SOUND_DIR + 'game/crowd.mp3'
######################################
