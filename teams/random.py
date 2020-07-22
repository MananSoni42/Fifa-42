from settings import *
from const import ACT
from teams.agent import Agent
from teams.team import Team

class RandomAgent(Agent):
    """ Agents that move randomly """
    def move(self, state_prev, state, reward):
        if random.random() < 0.6:
            return random.choice(['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R'])
        else:
            return random.choice(['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C'])

class RandomTeam(Team):
    """A team of random agents"""
    def set_players(self):
        self.players = []
        for i in range(NUM_TEAM):
            self.players.append(RandomAgent(id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]))

    def move(self, state_prev, state, reward):
        """ Move each player randomly """
        actions = []
        for i,player in enumerate(self.players):
            actions.append(player.move(state_prev, state, reward))
        return actions
