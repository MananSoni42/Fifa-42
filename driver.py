from team import Team
from game import Game
from utils import *

win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

team = Team(formation='default', dir='R')
game = Game(team)

pygame.key.set_repeat(1,1)
while not game.end:
    clock.tick(27)

    game.draw(win)
    pygame.display.update()

    a = []
    for i,player in enumerate(team.players):
        if i == team.nearest:
            a.append(player.move(0,0))
        else:
            a.append('NOTHING')
    s,r = game.next(a)
