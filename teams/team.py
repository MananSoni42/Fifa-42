from settings import *
from const import FORM, recolor
from abc import ABC, abstractmethod

class Team(ABC):
    """
    Abstract class for a team of agents
    Implement the move and set_players methods to instantiate
    """
    def __init__(self, color, formation='default'):
        """ call the init method to complete the proccess"""
        self.color = color
        self.formation = formation
        self.maintain_formation = True

    def __str__(self):
        s = f'Team {self.id}:'
        for player in self.players:
            s += player.__str__()
        return s

    def init(self, id, dir):
        """
        Sets the teams id and direction assigns colored sprites + formations to that id
        """
        self.id = id
        self.dir = dir

        if self.dir == 'L':
            self.goal_x = 0
        else:
            self.goal_x = W

        self.set_players()
        self.set_color()

    def set_color(self):
        for k in RUN[self.id]['L'].keys():
            recolor(RUN[self.id]['L'][k], color=self.color)
            recolor(RUN[self.id]['R'][k], color=self.color)

    def set_formation(self,formation):
        self.formation = formation

    def formation_toggle(self):
        self.maintain_formation = not self.maintain_formation

    def draw(self,win, debug=False):
        for player in self.players:
            player.draw(win, team_id=self.id, debug=debug)

    def update(self, action, ball):
        for i,player in enumerate(self.players):
            player.update(action[i], self.players)

    @abstractmethod
    def set_players(self):
        """
        Add players (of relevant class) to the team
        Requirements:
            - Players are added to a list: self.players
            - Their ids match their respective index in the array
        """
        pass

    @abstractmethod
    def move(self, state, reward):
        """ Move the entire team (may use the player's move method) """
        pass
