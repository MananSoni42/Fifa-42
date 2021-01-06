"""
Create a team that learns using Reinforcement learning
"""

from settings import *
from const import ACT, FORM
from teams.agent import Agent as agent
from tensorforce.agents import Agent as rl_agent
from teams.team import Team
from tqdm import tqdm

ACTION_MAP = list(ACT.keys())

class RLAgent(agent):
    """
    RL team
    """

    def __init__(self, id, team_id, pos, meta_agent, reward, dir='L'):
        super().__init__(id, team_id, pos, dir)
        self.agent = meta_agent
        self.R = reward

    def convert_state(self, state_prev, state):
        return {
            'ball': state['ball'].pos.val,
            'team1': [pl.pos.val[j] for pl in state['team1']['players'] for j in range(2) if pl],
            'team2': [pl.pos.val[j] for pl in state['team2']['players'] for j in range(2) if pl],
        }

    def move(self, state_prev, state, reward, selected):
        """
        The agent observes the previous state's reward and acts on the current state
        """
        if state_prev:
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
        type = 'reinforce'

        state_spec = dict(
                ball = dict(type='float', shape=2, min_value=0, max_value=max(W,H)),
                team1 = dict(type='float', shape=2*len(self.other_ids), min_value=0, max_value=max(W,H)), # hack to get other teams players value
                team2 = dict(type='float', shape=2*len(ids), min_value=0, max_value=max(W,H)),
            )

        action_spec = dict(type='int', shape=1, num_values=len(ACT))

        form = FORM[self.formation][self.dir]

        # meta agents move more than a single agent
        # The maximum episode length needs to be adjusted accordingly
        num = { 'GK': 0, 'DEF': 0, 'MID': 0, 'ATK': 0 }
        for id in ids:
            num[form[id]['pos']] += 1

        print(f'Initializing team {self.id} agents - GK, DEF, MID, ATK')
        self.meta_agent = dict()
        for agent in tqdm(['GK', 'DEF', 'MID', 'ATK']):
            if num[agent] > 0:
                self.meta_agent[agent] = rl_agent.create(agent=type,
                            states=state_spec, actions=action_spec,
                            max_episode_timesteps=num[agent]*MAX_EP_LEN,
                            batch_size=BATCH_SIZE)

        for i in range(NUM_TEAM):
            if i in ids:
                self.players.append(RLAgent(
                    id=i, team_id=self.id, pos=form[i]['coord'],
                    meta_agent=self.meta_agent[form[i]['pos']],
                    reward=REW[form[i]['pos']]))
            else:
                self.players.append(None)

    def move(self, state_prev, state, reward):
        """
        Move the RL team by moving each RL agent
        """
        actions = []

        for i, player in enumerate(self.players):
            if player:
                actions.append(player.check_move(state_prev, state, reward[self.id][i]))
            else:
                actions.append('NOTHING')
        return actions

    def save(self, dir):
        for name,agent in self.meta_agent.items():
            agent.save(directory=dir, filename=name, format='checkpoint')

    def load(self, dir):
        for name,agent in self.meta_agent.items():
            if os.path.exists(os.path.join(dir,name)):
                print(f'loading {name} agent from {os.path.join(dir,name)}')
                agent.load(directory=dir, filename=name, format='checkpoint')
