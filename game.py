from utils import *
from ball import Ball

class Game:
    """ Class that controls the entire game """
    def __init__(self, player):
        self.player = player
        self.ball = Ball(pos=(W//2, H//2))
        self.end = False # True when the game ends (never probably)

    def draw_field(self,win):
        """ Draw the football pitch """
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
        """ Draw everything """
        self.draw_field(win)
        self.player.draw(win)
        self.ball.draw(win)

    def next(self, a):
        """ Next loop that is the heart of the game - takes an action from the player and returns the new state and reward """
        self.player.update(a) # Update player's state
        self.ball.update(self.player, a) # Update ball's state
        self.ball.goal_check() # Check for goals
        return 0,0
