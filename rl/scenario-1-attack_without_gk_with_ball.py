"""
Scenario 1
----------
A RL single attacker gets the ball in the opponents half (at a random place).
He has to score a goal with an empty goal post (no enemy goalkeeper)

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
import random
import matplotlib.pyplot as plt

args = get_args()

pygame.init()

if args.display:
    win = pygame.display.set_mode((W, H), 0)
    clock = pygame.time.Clock()
    pygame.display.set_caption("FIFA-42")

# Define teams (Team 1 faces right by default)
team1 = OriginalAITeam(formation=args.team1_formation, color=(0, 32, 255), ids=[])
team2 = RLTeam(formation=args.team2_formation, color=(255, 128, 0), ids=[9])

'''
Hack to make RL agents work properly
'''
team2.max_ep_len = args.ep_len
team2.eval = args.eval

game = Game(team1, team2, sound=False, difficulty=args.difficulty/100, cam='full')  # initialize the game

# load agent weights (if they exist)
if not args.noload:
    game.team2.load(args.agent_dir)

reward_hist = []
avg_hist = []
plot = {
    'avg': [],
    'checkpoint': [],
}

total_reward = {
    1: [0]*NUM_TEAM,
    2: [0]*NUM_TEAM,
}

checkpoint_reward = {
    1: [0]*NUM_TEAM,
    2: [0]*NUM_TEAM,
}


reset = {
    'ball_pos': (W//2,H//2),
    1: [None]*NUM_TEAM,
    2: [None]*NUM_TEAM,
}

for ep in range(1,args.ep+1):

    x = random.randint(round(0.1*W), round(0.4*W))
    y = random.randint(0,H)
    reset[2][9] = P(x,y)
    #reset['ball_pos'] = (P(x,y) + P(random.randint(-20,20), random.randint(-20,20))).val
    reset['ball_pos'] = (x,y)

    game.reset(reset=reset)
    for count in tqdm(range(args.ep_len)):  # Game loop

        #clock.tick(args.fps)  # FPS
        if args.display:
            game.draw(win, hints=False)
            if game.pause:
                game.pause_draw(win)  # Draws on-top of the (frozen) game

        game.next()

        if args.display:
            pygame.display.update()  # refresh screen

    approx = lambda l: [round(i,3) for i in l]
    total_reward = add_rewards(total_reward, game.reward_hist)
    checkpoint_reward = add_rewards(checkpoint_reward, game.reward_hist)

    print(f'Ep {ep} - 1: {sum(game.reward_hist[1])} | 2: {sum(game.reward_hist[2])}\n')
    if ep%args.checkpoint == 0:
        game.save(args.agent_dir)
        print(f'\n ----------- Checkpoint at Ep {ep} -----------',
        f'improvement: ',
        f'\t current    : [ {sum(checkpoint_reward[1])/args.checkpoint} | {sum(checkpoint_reward[2])/args.checkpoint} ]',
        f'\t last 3     : {" ".join(reward_hist) if len(reward_hist) < 3 else " ".join(reward_hist[-3:])} ',
        f'\t prev 3 avg : {" ".join(avg_hist) if len(avg_hist) < 3 else " ".join(avg_hist[-3:])} ',
        f'Total: ',
        f'\tTeam 1: {sum(total_reward[1])/ep} | {approx(total_reward[1])}',
        f'\tTeam 2: {sum(total_reward[2])/ep} | {approx(total_reward[2])}',
        f'-------------------------------------------------------------------\n',
        sep='\n')
        plot['avg'].append(sum(total_reward[2])/ep)
        plot['checkpoint'].append(sum(checkpoint_reward[2])/args.checkpoint)
        reward_hist.append(f'[ {sum(checkpoint_reward[1])/args.checkpoint} | {sum(checkpoint_reward[2])/args.checkpoint} ]')
        avg_hist.append(f'[ {sum(total_reward[1])/ep} | {sum(total_reward[2])/ep} ]')
        checkpoint_reward = {
            1: [0]*NUM_TEAM,
            2: [0]*NUM_TEAM,
        }

game.close(args.agent_dir, save=not args.nosave)

plt.plot(plot['avg'], label='average reward')
plt.plot(plot['checkpoint'], label='checkpoint reward')
plt.legend(loc='upper left')
plt.show()
