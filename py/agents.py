import pygame
import numpy as np
from utils import *

class HumanAgent(object):
    """Agents controlled by humans"""
    def __init__(self, id, type, pos, color=(255,0,0)):
        self.id = id
        self.type = type
        self.pos = pos
        self.color = color
        self.hasBall = False

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.pos, PLAYER_RADIUS)

    def move(self, state, reward):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if self.hasBall:
                    if event.key == pygame.K_q:
                        return 'SHOOT_Q'
                    elif event.key == pygame.K_w:
                        return 'SHOOT_Q'
                    elif event.key == pygame.K_e:
                        return 'SHOOT_E'
                    elif event.key == pygame.K_a:
                        return 'SHOOT_A'
                    elif event.key == pygame.K_d:
                        return 'SHOOT_D'
                    elif event.key == pygame.K_z:
                        return 'SHOOT_Z'
                    elif event.key == pygame.K_x:
                        return 'SHOOT_X'
                    elif event.key == pygame.K_c:
                        return 'SHOOT_C'
                    elif event.key == pygame.K_LEFT:
                        return 'MOVE_L'
                    elif event.key == pygame.K_RIGHT:
                        return 'MOVE_R'
                    elif event.key == pygame.K_UP:
                        return 'MOVE_U'
                    elif event.key == pygame.K_DOWN:
                        return 'MOVE_D'
                    else:
                        return 'NOTHING'
                else:
                    if event.key == pygame.K_LEFT:
                        return 'MOVE_L'
                    elif event.key == pygame.K_RIGHT:
                        return 'MOVE_R'
                    elif event.key == pygame.K_UP:
                        return 'MOVE_U'
                    elif event.key == pygame.K_DOWN:
                        return 'MOVE_D'
                    else:
                        return 'NOTHING'
