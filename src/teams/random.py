"""
Create a random team i.e. team where each agent takes a random action (used for testing)
"""

from settings import *
from const import ACT,FORM
from teams.agent import Agent
from teams.team import Team


class RandomAgent(Agent):
    """
    Agents that move randomly
    """

    def move(self, state_prev, state, reward):
        """
        Move the agent randomly
        """
        if random.random() < 0.6:
            return random.choice(['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R'])
        else:
            return random.choice(['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C'])


class RandomTeam(Team):
    """
    A team of random agents
    """

    def set_players(self, ids):
        self.players = []
        for i in range(NUM_TEAM):
            if i in ids:
                self.players.append(RandomAgent(
                    id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]['coord']))

    def move(self, state_prev, state, reward):
        """
        Move each player randomly
        """
        actions = []
        for i, player in enumerate(self.players):
            actions.append(player.move(state_prev, state, reward))
        return actions
