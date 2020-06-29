from utils import *
from ball import Ball

class Game:
    """Class that controls the entire game"""
    def __init__(self, player):
        self.player = player
        self.ball = Ball(pos=(W//2, H//2))
        self.end = False

    def draw_field(self,win):
        #win.blit(BACKGROUND_IMG, (0, 0)) # grass
        win.fill((14, 156, 23)) # constant green
        pygame.draw.rect(win, (255, 255, 255), (0, 0, W, LINE_WIDTH//2)) # border
        pygame.draw.rect(win, (255, 255, 255), (0, H-LINE_WIDTH//2, W, LINE_WIDTH//2)) # border
        pygame.draw.rect(win, (255, 255, 255), (0, 0, LINE_WIDTH//2, H)) # border
        pygame.draw.rect(win, (255, 255, 255), (W-LINE_WIDTH//2, 0, LINE_WIDTH//2, H)) # border
        pygame.draw.rect(win, (255, 255, 255), (W//2 - LINE_WIDTH//2, 0, LINE_WIDTH, H)) # mid line
        pygame.draw.circle(win, (255, 255, 255), (W//2, H//2), H//5, LINE_WIDTH) # mid circle
        pygame.draw.rect(win, (255, 255, 255), (19*W//20-LINE_WIDTH//2, GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH) # right goal
        pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2, GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH) # right goal

    def draw(self, win):
        self.draw_field(win) # Draw the football field
        self.player.draw(win) # players
        self.ball.draw(win) # ball

    def next(self, a):
        self.player.update(a) # Update player's state
        self.ball.update(self.player, a) # Update ball's state
        self.ball.goal_check()

        return 0,0
