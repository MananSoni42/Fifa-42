import pygame
import numpy as np

def dist(p1,p2):
    #print(p1,p2)
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

PLAYER_SPEED = 3
BALL_SPEED = 3
W = 1024
H = 568
BALL_RADIUS = 10
PLAYER_RADIUS = 15
BACKGROUND_IMG = "assets/field.png"

act = {
    'NOTHING': 0,
    'MOVE_U': (0,-1),
    'MOVE_D': (0,1),
    'MOVE_L': (-1,0),
    'MOVE_R': (1,0),
    'SHOOT_Q': (-1,-1),
    'SHOOT_W': (0,-1),
    'SHOOT_E': (1,-1),
    'SHOOT_A': (-1,0),
    'SHOOT_D': (1,0),
    'SHOOT_Z': (-1,1),
    'SHOOT_X': (0,1),
    'SHOOT_C': (1,1),
}

type = {
    'GK': 0,
    'DEF': 1,
    'MID': 2,
    'ATK': 3,
}
