from agents import HumanAgent
from game import Game
from utils import *

win = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

player1 = HumanAgent(id=0, type="ATK", pos=(W//4, H//2))
game = Game(player1)

pygame.key.set_repeat(1,1)
while not game.end:
    clock.tick(27)

    game.draw(win)
    pygame.display.update()

    a = player1.move(0,0)
    s,r = game.next(a)
