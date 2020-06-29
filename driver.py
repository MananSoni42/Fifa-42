from team import HumanTeam
from game import Game
from utils import *

win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

team = HumanTeam(formation='default-left', dir='L')
game = Game(team)

pygame.key.set_repeat(1,1)
while not game.end:
    clock.tick(27)

    game.draw(win)
    pygame.display.update()

    a = team.move()
    s,r = game.next(a)
