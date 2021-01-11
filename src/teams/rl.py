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

    def __init__(self, id, team_id, pos, meta_agent, reward, dir='L', eval=False):
        super().__init__(id, team_id, pos, dir)
        self.agent = meta_agent
        self.R = reward
        self.eval = eval

    def polar(self, p0, p):
        '''
        Convert a point to polar coordinates
        '''
        r = p0.dist(p) / max(W,H) # between 0 and 1
        th = math.atan2(p.y-p0.y, p.x-p0.x) / math.pi # between -1 and 1
        return [r, th]

    def convert_state(self, state_prev, state):
        return {
            'owned': [not state['ball'].free and state['ball'].ball_stats['player'] == self.id],
            'goal': [GOAL_POS[0]*H, GOAL_POS[1]*H],
            'pos': self.pos.val,
            'ball': self.polar(self.pos, state['ball'].pos),
            'team1': [self.polar(self.pos, pl.pos)[j] if pl else 0.0 for pl in state['team1']['players'] for j in range(2)],
            'team2': [self.polar(self.pos, pl.pos)[j] if pl else 0.0 for pl in state['team2']['players'] for j in range(2)],
        }

    def move(self, state_prev, state, reward, selected):
        """
        The agent observes the previous state's reward and acts on the current state
        """
        if state_prev:
            if self.eval:
                action = self.agent.act(states=self.convert_state(state_prev, state),
                                        independent=True, internals=self.agent.initial_internals())[0][0]
            else:
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

        state_spec = dict(
                owned = dict(type='bool', shape=1),
                goal  = dict(type='float', shape=2, min_value=0, max_value=max(W,H)),
                pos   = dict(type='float', shape=2, min_value=0, max_value=max(W,H)),
                ball  = dict(type='float', shape=2, min_value=-1, max_value=1),
                team1 = dict(type='float', shape=2*NUM_TEAM, min_value=-1, max_value=1),
                team2 = dict(type='float', shape=2*NUM_TEAM, min_value=-1, max_value=1),
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
                '''
                self.meta_agent[agent] = rl_agent.create(
                    agent='ppo',
                    network='auto',
                    states=state_spec, actions=action_spec,
                    max_episode_timesteps=num[agent]*self.max_ep_len,
                    batch_size=BATCH_SIZE)
                '''
                self.meta_agent[agent] = rl_agent.create(
                    agent='tensorforce',
                    states=state_spec, actions=action_spec,
                    max_episode_timesteps=num[agent]*self.max_ep_len,
                    update=dict(unit='timesteps', batch_size=BATCH_SIZE),
                    optimizer=dict(optimizer='adam', learning_rate=1e-3),
                    objective='action_value',
                    reward_estimation=dict(horizon=100),
                    exploration=1e-3,
                    )

        for i in range(NUM_TEAM):
            if i in ids:
                self.players.append(RLAgent(
                    id=i, team_id=self.id, pos=form[i]['coord'],
                    meta_agent=self.meta_agent[form[i]['pos']],
                    reward=REW[form[i]['pos']], eval=self.eval))
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
        for name in self.meta_agent.keys():
            try:
                self.meta_agent[name] = rl_agent.load(directory=dir, filename=name, format='checkpoint')
                print(f'loaded {name} agent from {os.path.join(dir,name)}')
            except:
                pass
