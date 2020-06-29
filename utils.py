import pygame
import numpy as np

"""
Utilities: Contains global settings, constants, functions and classes
"""

class P:
    """ 2-D point """

    def __init__(self, x,y=None):
        if y is None and isinstance(x,tuple):
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    @property
    def val(self):
        return (self.x, self.y)

    def __str__(self):
        return f'P({self.x}, {self.y})'

    def __add__(self, p):
        return P(self.x + p.x, self.y + p.y)

    def __iadd__(self, p):
        self.x += p.x
        self.y += p.y
        return self

    def __sub__(self, p):
        return P(self.x - p.x, self.y - p.y)

    def __isub__(self, p):
        self.x -= p.x
        self.y -= p.y
        return self

    def __mul__(self, p):
        return P(self.x * p.x, self.y * p.y)

    def __imul__(self, p):
        self.x *= p.x
        self.y *= p.y
        return self

    def dist(self, p):
        return np.sqrt((self.x-p.x)**2 + (self.y-p.y)**2)




############## Settings ##############
PLAYER_SPEED = 3
BALL_SPEED = 5
W = 1024
H = 568
BALL_RADIUS = 10
BALL_CENTER = P(BALL_RADIUS, BALL_RADIUS)
PLAYER_RADIUS = 30
PLAYER_CENTER = P(PLAYER_RADIUS, PLAYER_RADIUS)
GOAL_POS = [0.3,0.7] # goalpost positions in percentage
LINE_WIDTH = 3
ASSET_DIR = './assets/' # Path to where the images are stored
######################################



############## Images ##############
BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(ASSET_DIR + "field.png"), (W, H))
FOOTBALL_IMG = pygame.transform.scale(pygame.image.load(ASSET_DIR + "football.png"), (2*BALL_RADIUS, 2*BALL_RADIUS))
RUN = {
    'L': { i: pygame.transform.scale(pygame.image.load(ASSET_DIR + f'running/l{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(11) },
    'R': { i: pygame.transform.scale(pygame.image.load(ASSET_DIR + f'running/r{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(11) },
}
######################################



############## Custom types ##############
act = { 'NOTHING': 0,
        'MOVE_U': (0,-1), 'MOVE_D': (0,1), 'MOVE_L': (-1,0), 'MOVE_R': (1,0),
        'SHOOT_Q': (-1,-1), 'SHOOT_W': (0,-1), 'SHOOT_E': (1,-1), 'SHOOT_A': (-1,0),
        'SHOOT_D': (1,0), 'SHOOT_Z': (-1,1), 'SHOOT_X': (0,1), 'SHOOT_C': (1,1) }

#pl_type = { 'GK': 0, 'DEF': 1, 'MID': 2, 'ATK': 3 }
######################################
