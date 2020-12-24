"""
Driver program

Use this to play the game
"""

import time
from settings import *
from pygame import mixer
import pygame_menu
from game import Game
from teams.human import HumanTeam
from teams.original_ai import OriginalAITeam
from teams.random import RandomTeam
from menu import play_with_menu
from args import get_args

args = get_args()

pygame.init()
win = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

# Init music
mixer.init(44100, -16, 2, 2048)
menu_music = mixer.Sound(MENU_MUSIC)

# Define teams (Team 1 faces right by default)
if args.team1.lower() == 'random':
    team1 = RandomTeam(formation=args.team1_formation, color=(0, 32, 255))
elif args.team1.lower() == 'ai':
    team1 = OriginalAITeam(formation=args.team1_formation, color=(0, 32, 255))
elif args.team1.lower() == 'human':
    team1 = HumanTeam(formation=args.team1_formation, color=(0, 32, 255))
else:
    raise Exception(f'No team named `{args.team1}`')

if args.team2.lower() == 'ai':
    team2 = OriginalAITeam(formation=args.team2_formation, color=(255, 128, 0))
elif args.team2.lower() == 'random':
    team2 = RandomTeam(formation=args.team2_formation, color=(255, 128, 0))
else:
    raise Exception(f'No team named `{args.team2}`')

no_team = RandomTeam(ids=[])

def play(win, team1, team2, sound, difficulty, cam):  # Play the entire game
    mixer.stop()
    game = Game(team1, team2, sound, difficulty, cam)  # initialize the game
    """ Game loop """
    while not game.end:  # Game loop
        clock.tick(args.fps)  # FPS

        game.check_interruptions()  # Check for special keys (quit, pause, etc)

        if game.pause:  # game is paused - display pause menu
            game.draw(win)
            game.pause_draw(win)  # Draws on-top of the (frozen) game
        else:  # Continue with the game
            game.draw(win)
            game.next()

        pygame.display.update()  # refresh screen

    global game_menu
    if not args.menu_off:
        game_menu.start()  # Return to main menu

def practice():
    mixer.stop()

    game = Game(team1, no_team, sound=False)  # initialize the game
    """ Game loop """
    while not game.end:  # Game loop
        clock.tick(args.fps)  # FPS

        game.check_interruptions()  # Check for special keys (quit, pause, etc)

        game.draw(win, hints=False)
        game.practice_instr_draw(win)
        game.next()

        pygame.display.update()  # refresh screen

    global game_menu
    game_menu.start()  # Return to main menu

# Run the game
if args.menu_off:
    play(win, team1, team2, sound=not args.sound_off, difficulty=args.difficulty/100, cam=args.camera)
else:
    game_menu = play_with_menu(win, team1, team2, play, practice,
            sound=not args.sound_off, difficulty=args.difficulty/100, cam=args.camera)
    game_menu.start()
