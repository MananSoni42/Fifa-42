from team import HumanTeam
from game import Game
from utils import *

"""
Driver program to test the game
"""

win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

team = HumanTeam(formation='default-left', dir='L') # Create a team facing left (L), use the default-left formation (defined in utils.py)
game = Game(team)

pygame.key.set_repeat(1,1) # Generate multiple keydowns if a key is pressed
while not game.end:
    clock.tick(27) # FPS

    game.draw(win)
    pygame.display.update() # refresh screen

    a = team.move()
    s,r = game.next(a)
