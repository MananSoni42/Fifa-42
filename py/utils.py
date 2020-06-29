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

## images
BACKGROUND_IMG = "assets/field.png"
FOOTBALL_IMG = "assets/football.png"
RUN_LEFT = { i:f'assets/running/l{i}.png' for i in range(11)}
RUN_RIGHT = { i:f'assets/running/r{i}.png' for i in range(11)}

## Special types
act = { 'NOTHING': 0,
        'MOVE_U': (0,-1), 'MOVE_D': (0,1), 'MOVE_L': (-1,0), 'MOVE_R': (1,0),
        'SHOOT_Q': (-1,-1), 'SHOOT_W': (0,-1), 'SHOOT_E': (1,-1), 'SHOOT_A': (-1,0),
        'SHOOT_D': (1,0), 'SHOOT_Z': (-1,1), 'SHOOT_X': (0,1), 'SHOOT_C': (1,1) }

#pl_type = { 'GK': 0, 'DEF': 1, 'MID': 2, 'ATK': 3 }
