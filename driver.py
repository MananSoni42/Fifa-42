import time
from settings import *
from pygame import mixer
import pygame_menu
from game import Game
from teams.no import NoTeam
from teams.human import HumanTeam
from teams.original_ai import OriginalAITeam
from menu import Menu
"""
Driver program to test the game
"""

pygame.init()
win = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

# Init music
mixer.init(44100, -16, 2, 2048)
menu_music = mixer.Sound(MENU_MUSIC)

# Define teams (Team 1 faces right by default)
team1 = HumanTeam(formation='default', color=(0, 32, 255))
team2 = OriginalAITeam(formation='balanced-1', color=(255, 128, 0))
no_team = NoTeam()


def play(sound):  # Play the entire game
    mixer.stop()

    game = Game(team1, team2, sound)  # initialize the game
    """ Game loop """
    while not game.end:  # Game loop
        clock.tick(FPS)  # FPS

        game.check_interruptions()  # Check for special keys (quit, pause, etc)

        if game.pause:  # game is paused - display pause menu
            game.draw(win)
            game.pause_draw(win)  # Draws on-top of the (frozen) game
        else:  # Continue with the game
            game.draw(win)
            game.next()

        pygame.display.update()  # refresh screen

    game_menu.start()  # Return to main menu


def practice():
    mixer.stop()

    game = Game(team1, no_team, sound=False)  # initialize the game
    """ Game loop """
    while not game.end:  # Game loop
        clock.tick(FPS)  # FPS

        game.check_interruptions()  # Check for special keys (quit, pause, etc)

        game.draw(win, hints=False)
        game.practice_instr_draw(win)
        game.next()

        pygame.display.update()  # refresh screen

    game_menu.start()  # Return to main menu


# The menu
game_menu = Menu(win, team1, team2)
game_menu.create_main_menu(play, practice)
game_menu.start()
