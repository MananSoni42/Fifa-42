"""
Global game settings

Defines image / sound paths and all constants used in the game

Can be freely changed
"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from point import P
from screeninfo import get_monitors
import pygame
import random
import math
import sys

"""
Settings and paths
"""

# Required for pyinstaller
if getattr(sys, 'frozen', False):  # PyInstaller adds this attribute
    # Running in a bundle
    CurrentPath = sys._MEIPASS
else:
    # Running in normal Python environment
    CurrentPath = os.path.dirname(__file__)


############## Settings ##############
NUM_TEAM = 11  # Number of players in a team
FONT_SIZE = 45
W = get_monitors()[0].width  # Width
H = get_monitors()[0].height  # Height

PLAYER_SELECT_RADIUS = 5
PLAYER_SPEED = 3
PLAYER_RADIUS = 20
PLAYER_CENTER = P(PLAYER_RADIUS, PLAYER_RADIUS)

BALL_SPEED = 7
BALL_RADIUS = 7
BALL_CENTER = P(BALL_RADIUS, BALL_RADIUS)
BALL_OFFSET = P(2, 1.5)

GOAL_DISP_SIZE = 60
GOAL_POS = [0.3, 0.7]  # goalpost positions in percentage of H
LINE_WIDTH = 2
ANIM_NUM = 7  # Number of images used for running animation
WALK_DELAY = 3  # Change walking sprite after this many presses

# Orginal AI related - Difficulty (between 0 and 1) - Easy (0.1) | Medium (0.5) | Hard (0.8)
AI_FAR_RADIUS = lambda diff: round((2 + 11*diff)*PLAYER_RADIUS) # Far radius to look for ball
AI_NEAR_RADIUS = lambda diff: round((2 + 2*diff)*PLAYER_RADIUS) # Near radius to ward off enemy players
AI_SHOOT_RADIUS = W//4  # Dist from center of goal post within which AI starts shooting
AI_MIN_PASS_DIST = 25  # Min perpendicular distance to consider for a successfull pass
AI_PASS_PROB = 0.95  # Probability that AI moves instead of passing


######################################


############## Assets (images, fonts, sounds) ##############
ASSET_DIR = os.path.join(CurrentPath, 'assets')  # Path to assets
IMG_DIR = os.path.join(ASSET_DIR, 'img')
SOUND_DIR = os.path.join(ASSET_DIR, 'sounds')

FONT_ROBOTO = os.path.join(ASSET_DIR, 'fonts', 'Roboto-Black.ttf')
FONT_8BIT = os.path.join(ASSET_DIR, 'fonts', '8bit.ttf')
FONT_NEVIS = os.path.join(ASSET_DIR, 'fonts', 'nevis.ttf')
FONT_MONO = os.path.join(ASSET_DIR, 'fonts', 'mono.ttf')

MENU_BG = os.path.join(IMG_DIR, 'menu_bg.jpg')
CONTROLS_IMG = os.path.join(IMG_DIR, 'controls.png')

def GET_FORM_BG(team_id, formation_id): return os.path.join(
    IMG_DIR, 'formations', f'{team_id}-{formation_id}.jpg')  # Get correct formation img


# BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'field.png')), (W, H)) # Background (not used currently)
FOOTBALL_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join(IMG_DIR, 'football.png')), (2*BALL_RADIUS, 2*BALL_RADIUS))
RUN = {  # Sprites that animate the running player
    1: {
        'L': {i: pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'running', f'l{i}.png')), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7)},
        'R': {i: pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'running', f'r{i}.png')), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7)},
    },
    2: {
        'L': {i: pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'running', f'l{i}.png')), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7)},
        'R': {i: pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'running', f'r{i}.png')), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(7)},
    },
}

# Sounds
APPLAUSE = os.path.join(SOUND_DIR, 'applause2.wav')
KICK = os.path.join(SOUND_DIR, 'FOOTBALLKICK.wav')
MENU_MUSIC = os.path.join(SOUND_DIR, 'menu-music.wav')
SINGLE_SHORT_WHISTLE = os.path.join(SOUND_DIR, 'single-short-whistle.wav')
SINGLE_LONG_WHISLTE = os.path.join(SOUND_DIR, 'single-long-whistle.wav')
THREE_WHISTLES = os.path.join(SOUND_DIR, 'three-whistles.wav')
TWO_KICKS = os.path.join(SOUND_DIR, 'two-kicks.wav')
GOAL = os.path.join(SOUND_DIR, 'goal.wav')
CLICK = os.path.join(SOUND_DIR, 'click.wav')
BOOING = os.path.join(SOUND_DIR, 'boo.wav')
BOUNCE = os.path.join(SOUND_DIR, 'bounce2.wav')

######################################
