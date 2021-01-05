"""
Create a team that learns using Reinforcement learning
"""

from settings import *
from const import ACT, FORM
from teams.agent import Agent as agent
from tensorforce.agents import Agent as rl_agent
from teams.team import Team
from tqdm import tqdm
from pprint import pprint

state_spec = dict(
        ball = dict(type='float', shape=2, min_value=0, max_value=max(W,H)),
        team1 = dict(type='float', shape=4, min_value=0, max_value=max(W,H)),
        team2 = dict(type='float', shape=4, min_value=0, max_value=max(W,H)),
    )

action_spec = dict(type='int', shape=1, num_values=len(ACT))

ACTION_MAP = list(ACT.keys())


class RLAgent(agent):
    """
    Agents that move randomly
    """

    def __init__(self, id, team_id, pos, dir='L'):
        super().__init__(id, team_id, pos, dir='L')
        self.agent = rl_agent.create(agent='reinforce',
                    states=state_spec, actions=action_spec, max_episode_timesteps=100000,
                    batch_size=1)

    def convert_state(self, state_prev, state):
        #return {'prev_state': state_prev, 'curr_state': state}
        return {
            'ball': state['ball'].pos.val,
            'team1': [pl.pos.val[j] for pl in state['team1']['players'] for j in range(2)],
            'team2': [pl.pos.val[j] for pl in state['team2']['players'] for j in range(2)],
        }

    def move(self, state_prev, state, reward, selected):
        """
        The agent observes the previous state's reward and acts on the current state
        """
        if state_prev and state:
            action = self.agent.act(states=self.convert_state(state_prev, state))[0]
            self.agent.observe(reward=reward)
            return ACTION_MAP[action]
        return 'NOTHING'


class RLTeam(Team):
    """
    A team of RL agents
    """

    def set_players(self, ids):
        self.players = []
        for i in range(NUM_TEAM):
            if i in tqdm(ids):
                self.players.append(RLAgent(
                    id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]['coord']))

    def move(self, state_prev, state, reward):
        """
        Move each player randomly
        """
        actions = []
        global_reward = reward[self.id]['global']
        for i, player in enumerate(self.players):
            actions.append(player.check_move(state_prev, state, reward[self.id]['players'][i]))
        return actions
