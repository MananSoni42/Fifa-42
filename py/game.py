import pygame
from utils import *

class Game:
    """Class that controls the entire game"""
    def __init__(self, player):
        self.player = player
        self.end = False

    def draw(self, win):
        win.fill((0,255,0)) # green background
        pygame.draw.rect(win, (255, 255, 255), (0, 0, WIDTH, 3)) # border
        pygame.draw.rect(win, (255, 255, 255), (0, HEIGHT-3, WIDTH, 3)) # border
        pygame.draw.rect(win, (255, 255, 255), (0, 0, 3, HEIGHT)) # border
        pygame.draw.rect(win, (255, 255, 255), (WIDTH-3, 0, 3, HEIGHT)) # border
        pygame.draw.rect(win, (255, 255, 255), (WIDTH//2 - 3, 0, 6, HEIGHT)) # mid line
        pygame.draw.circle(win, (255, 255, 255), (WIDTH//2, HEIGHT//2), HEIGHT//5, 6) # mid circle        
        #TODO - entire field
        self.player.draw(win)

    def next(self, a):
        if a in ['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']:
            x,y = self.player.pos
            x += act[a][0]
            y += act[a][1]
            if PLAYER_RADIUS <= x <= WIDTH - PLAYER_RADIUS and PLAYER_RADIUS <= y <= HEIGHT - PLAYER_RADIUS:
                self.player.pos = (x,y)
        return 0,0
