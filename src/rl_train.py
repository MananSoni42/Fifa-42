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
from rl_args import get_args
from pprint import pprint
from tqdm import tqdm
from const import add_rewards

args = get_args()

pygame.init()

if args.display:
    win = pygame.display.set_mode((W, H), 0)
    clock = pygame.time.Clock()
    pygame.display.set_caption("FIFA-42")

# Define teams (Team 1 faces right by default)
team1 = OriginalAITeam(formation=args.team1_formation, color=(0, 32, 255))
team2 = RLTeam(formation=args.team2_formation, color=(255, 128, 0))
game = Game(team1, team2, sound=False, difficulty=args.difficulty/100, cam='full')  # initialize the game

total_reward = {
    1: {'global': 0, 'players': [0]*NUM_TEAM},
    2: {'global': 0, 'players': [0]*NUM_TEAM},
}

print('Playing Game')
for ep in range(1,NUM_EP+1):
    game.reset()
    for count in tqdm(range(MAX_EP_LEN)):  # Game loop
        if game.end:
            print('Game ended')
            break

        #clock.tick(args.fps)  # FPS
        if args.display:
            game.draw(win)
            if game.pause:
                game.pause_draw(win)  # Draws on-top of the (frozen) game

        game.next()

        if args.display:
            pygame.display.update()  # refresh screen

    approx = lambda l: [round(i,3) for i in l]
    total_reward = add_rewards(total_reward, game.reward_hist)
    print(f'''\n ------------- Episode {ep} -------------
    Team 1: {total_reward[1]['global']} | {approx(total_reward[1]['players'])}
    Team 2: {total_reward[2]['global']} | {approx(total_reward[2]['players'])}
    \t-------------------------
    ''')
game.close()
