"""
Create a team with no players (deprecated - Use the ```ids``` arguement in the ```set_players``` method instead)
"""

from settings import *
from const import ACT
from teams.agent import Agent
from teams.team import Team


class NoTeam(Team):
    """
    A team with no players (XD)
    """

    def set_players(self):
        self.players = []

    def move(self, state_prev, state, reward):
        """ Moves the entire team """
        return []
