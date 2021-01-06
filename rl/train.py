"""
General program to train the RL model
"""

import sys
sys.path.insert(0, '../src')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pprint import pprint
from tqdm import tqdm
from train_args import get_args
from game import Game
from settings import *
from teams.original_ai import OriginalAITeam
from teams.rl import RLTeam
from menu import Menu
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

'''
Hack to make RL agents work properly
(refer to set_player() in teams/rl)
'''
team2.other_ids = team1.ids

game = Game(team1, team2, sound=False, difficulty=args.difficulty/100, cam='full')  # initialize the game

# load agent weights (if they exist)
game.team2.load(args.agent_dir)

total_reward = {
    1: [0]*NUM_TEAM,
    2: [0]*NUM_TEAM,
}

for ep in range(1,args.ep+1):
    game.reset()
    print(f'\nEp {ep}')
    for count in tqdm(range(MAX_EP_LEN)):  # Game loop

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
    if count%args.summary_freq == 0:
        print(f'''\n ----------- Summary till Ep {ep} -----------
        Team 1: {sum(total_reward[1])/11/ep} | {approx(total_reward[1])}
        Team 2: {sum(total_reward[2])/11/ep} | {approx(total_reward[2])}
        -------------------------''')

game.close(args.agent_dir, save=not args.nosave)
