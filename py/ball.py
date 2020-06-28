from utils import *

class Ball:
    """Implements the football used in the game"""
    def __init__(self, pos):
        self.pos = pos
        self.vel = (0,0)
        self.free = True
        self.player_id = None
        self.color = (50,50,50)
        self.fb = pygame.transform.scale(pygame.image.load(FOOTBALL_IMG), (2*BALL_RADIUS, 2*BALL_RADIUS))

    def reset(self):
        self.pos = (0.5, 0.5)

    def draw(self, win):
        #pygame.draw.circle(win, self.color, self.pos, BALL_RADIUS)
        win.blit(self.fb, (self.pos[0]-BALL_RADIUS, self.pos[1]))
