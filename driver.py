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

"""
Define teams
    - Team 1 faces right by default
"""
team1 = HumanTeam(formation='default', color=(0,32,255))
team2 = RandomTeam(color=(255,128,0))

game = Game(team1,team2)

while not game.end:
    clock.tick(FPS) # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit
            game.end = True

    keys = pygame.key.get_pressed() # Pause
    if keys[pygame.K_ESCAPE]:
        game.pause = True
    if keys[pygame.K_BACKSPACE]:
        game.pause = False


    if game.pause:
        game.draw(win)
        game.pause_draw(win)
    else:
        game.draw(win, debug=False)
        game.next()

    pygame.display.update() # refresh screen

pygame.quit()
