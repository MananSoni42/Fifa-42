import pygame
import numpy as np

def dist(p1,p2):
    #print(p1,p2)
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

## Settings
PLAYER_SPEED = 3
BALL_SPEED = 5
W = 1024
H = 568
BALL_RADIUS = 10
PLAYER_RADIUS = 30
GOAL_POS = [0.3,0.7] # goalpost positions in percentage
LINE_WIDTH = 3

## images
BACKGROUND_IMG = pygame.transform.scale(pygame.image.load("assets/field.png"), (W, H))
FOOTBALL_IMG = pygame.transform.scale(pygame.image.load("assets/football.png"), (2*BALL_RADIUS, 2*BALL_RADIUS))
RUN = {
    'L': { i: pygame.transform.scale(pygame.image.load(f'assets/running/l{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(11) },
    'R': { i: pygame.transform.scale(pygame.image.load(f'assets/running/r{i}.png'), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for i in range(11) },
}

## Special types

act = { 'NOTHING': 0,
        'MOVE_U': (0,-1), 'MOVE_D': (0,1), 'MOVE_L': (-1,0), 'MOVE_R': (1,0),
        'SHOOT_Q': (-1,-1), 'SHOOT_W': (0,-1), 'SHOOT_E': (1,-1), 'SHOOT_A': (-1,0),
        'SHOOT_D': (1,0), 'SHOOT_Z': (-1,1), 'SHOOT_X': (0,1), 'SHOOT_C': (1,1) }

#pl_type = { 'GK': 0, 'DEF': 1, 'MID': 2, 'ATK': 3 }
