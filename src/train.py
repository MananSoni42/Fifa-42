"""
Program to train the RL model
"""

import time
from settings import *
from pygame import mixer
from game import Game
from teams.human import HumanTeam
from teams.original_ai import OriginalAITeam
from teams.random import RandomTeam
from menu import Menu
from args import get_args

args = get_args()

pygame.init()
win = pygame.display.set_mode((W, H), 0)
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

# Init music
mixer.init(44100, -16, 2, 2048)
menu_music = mixer.Sound(MENU_MUSIC)

# Define teams (Team 1 faces right by default)
team1 = HumanTeam(formation=args.team1_formation, color=(0, 32, 255))
team2 = OriginalAITeam(formation=args.team2_formation, color=(255, 128, 0))

def play(win, team1, team2, sound, difficulty, cam):
    '''
    Play the game: This is the central function that runs the game
    '''

    mixer.stop()
    game = Game(team1, team2, sound, difficulty, cam)  # initialize the game
    game.debug = True
    
    while not game.end:  # Game loop
        clock.tick(args.fps)  # FPS

        game.draw(win)
        if game.pause:
            game.pause_draw(win)  # Draws on-top of the (frozen) game
        game.next()

        pygame.display.update()  # refresh screen

play(win, team1, team2, sound=False, difficulty=args.difficulty/100, cam='full')
