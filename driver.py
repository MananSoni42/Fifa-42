from team import HumanTeam, RandomTeam
from game import Game
from settings import *
import time

# from const import * # Enable for possession stats and goals

"""
Driver program to test the game
"""
pygame.init()
win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

"""
Define teams
    - One needs to be AI, other can be human or AI
    - ids need to be 1 and 2 only
    - Team 1 faces right by default
"""

team1 = HumanTeam(color=(255,128,0))
team2 = RandomTeam(formation='default', color=(0,32,255))

game = Game(team1,team2)

while not game.end:

    clock.tick(FPS) # FPS

    """ # Stats
    print(f'POSS: {get_possession(POSSESSION)} | PASS: {get_pass_acc(PASS_ACC)} | SHOT: {get_shot_acc(SHOT_ACC)}') # Stats
    """

    game.draw(win, debug=False)
    pygame.display.update() # refresh screen

    a1 = team1.move()
    a2 = team2.move()
    s,r = game.next(a1,a2)
