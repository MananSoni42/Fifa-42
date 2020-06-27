import pygame
from agents import HumanAgent
from game import Game
from utils import *
win = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

player1 = HumanAgent(id=1, type=type["ATK"], pos=(WIDTH//3,HEIGHT//2))
game = Game(player1)

pygame.key.set_repeat(10,10)
while not game.end:
    clock.tick(27)

    game.draw(win)
    pygame.display.update()

    a = player1.move(0,0)
    s,r = game.next(a)
