from team import HumanTeam, RandomTeam
from game import Game
from settings import *
import time

"""
Driver program to test the game
"""
pygame.init()
win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

# Define teams (Team 1 faces right by default)
team1 = HumanTeam(formation='default', color=(0,32,255))
team2 = RandomTeam(color=(255,128,0))

game = Game(team1,team2)

while not game.end:
    clock.tick(FPS) # FPS

    game.check_interruptions() # Check for pause or quit keys

    if game.pause:
        game.draw(win)
        game.pause_draw(win) # Draws on-top of the (frozen) game
    else:
        game.draw(win, debug=False)
        game.next() # Move the game forward

    pygame.display.update() # refresh screen

pygame.quit()
