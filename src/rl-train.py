"""
Program to train the RL model
"""

import time
from settings import *
from pygame import mixer
from game import Game
from teams.human import HumanTeam
from teams.original_ai import OriginalAITeam
from teams.rl import RLTeam
from menu import Menu
from args import get_args
from pprint import pprint
from tqdm import tqdm

args = get_args()

pygame.init()
win = pygame.display.set_mode((W, H), 0)
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

# Init music
mixer.init(44100, -16, 2, 2048)
menu_music = mixer.Sound(MENU_MUSIC)

# Define teams (Team 1 faces right by default)
team1 = OriginalAITeam(formation=args.team1_formation, color=(0, 32, 255))
team2 = RLTeam(formation=args.team2_formation, color=(255, 128, 0))

game = Game(team1, team2, sound=False, difficulty=args.difficulty/100, cam='full')  # initialize the game
game.debug = True

print('Playing Game')
for count in tqdm(range(MAX_EP_LEN)):  # Game loop
    if game.end:
        print('Game ended')
        break

    #clock.tick(args.fps)  # FPS
    game.draw(win)
    if game.pause:
        game.pause_draw(win)  # Draws on-top of the (frozen) game
    game.next()

    pygame.display.update()  # refresh screen

pprint(game.reward_hist)
