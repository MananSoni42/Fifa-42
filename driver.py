from team import HumanTeam, RandomTeam
from game import Game
from settings import *
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
team1 = HumanTeam(id = 1, formation='default-left', color=(0,32,255))
team2 = RandomTeam(id = 2, formation='default-right', color=(255,128,0))
game = Game(team1,team2)

pygame.key.set_repeat(1,1) # Generate multiple keydown events if a key is pressed continuously

while not game.end:
    clock.tick(FPS) # FPS
    game.draw(win, debug=False)
    #print(f'POSS: {get_possession(POSSESSION)} | PASS: {get_pass_acc(PASS_ACC)} | SHOT: {get_shot_acc(SHOT_ACC)}') # Stats
    pygame.display.update() # refresh screen

    a1 = team1.move()
    a2 = team2.move()
    s,r = game.next(a1,a2)
