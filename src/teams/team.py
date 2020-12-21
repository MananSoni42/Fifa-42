"""
Defines how a team is created, drawn and updated

Override the ```set_players``` and ```move``` method to create a valid custom team

(You can use a custom agent in your custom team)
"""

from settings import *
from const import recolor
from abc import ABC, abstractmethod


class Team(ABC):
    """
    Abstract class that controls a team of agents.

    Implement the move and set_players methods to instantiate
    """

    def __init__(self, color=(0, 0, 0), formation='default', ids=list(range(NUM_TEAM))):
        """
        Initialize the teams (not completely, some paramters are set using the ```init()``` method)

        Attributes:
            color (tuple): The RGB value of the team
            formation (string): The team's formation of the team. Must be a key of ```FORM``` from ```const.py```
            ids ([int]): Players to include in the team (identified by their ids)
        """
        self.color = color
        self.formation = formation
        self.maintain_formation = True
        self.ids = ids

    def __str__(self):
        s = f'Team {self.id}:'
        for player in self.players:
            s += player.__str__()
        return s

    def init(self, id, dir, diff):
        """
        Set the teams id, direction and difficulty (only for AI teams)
        Also recolor the sprites based on the team's chosen color

        Attributes:
            id (int): The team's id (must be either 1 or 2)
            dir (str): The team's direction (must be either 'L' or 'R')
            diff (float): The game difficult (between 0-1)

        Calls ```set_players()``` and ```set_color()```
        """
        self.id = id
        self.dir = dir
        self.difficulty = diff

        if self.dir == 'L':
            self.goal_x = 0
        else:
            self.goal_x = W

        self.set_players(self.ids)
        self.set_color()

    def set_color(self):
        """
        Recolor the sprites using this team's color
        """
        for k in RUN[self.id]['L'].keys():
            for key in RUN[self.id]['L'][k].keys():
                recolor(RUN[self.id]['L'][k][key], color=self.color)
                recolor(RUN[self.id]['R'][k][key], color=self.color)

    def set_formation(self, formation):
        """
        Set the teams formation
        """
        self.formation = formation

    def formation_toggle(self):
        """
        Toggle whether the team maintains its formation
        """
        self.maintain_formation = not self.maintain_formation

    def draw(self, win, cam, debug=False):
        """
        Draw the team

        Basically calls each players' ```draw()``` method
        """
        for player in self.players:
            player.draw(win, cam, team_id=self.id, debug=debug)

    def update(self, action, ball):
        """
        Update the team's state

        Basically calls each players' ```update()``` method
        """

        for i, player in enumerate(self.players):
            player.update(action[i], self.players)

    @abstractmethod
    def set_players(self, ids=list(range(NUM_TEAM))):
        """
        Implement this method to instantiate a valid team.

        Add players (of relevant class) to the team

        Attributes:
            ids (list): IDs of players to include in the team (defaults to all the players)

        **Requirements:**

        * Players are added to a list called players
        * Their ids match their respective index in the array
        """
        pass

    @abstractmethod
    def move(self, state_prev, state, reward):
        """
        Implement this method for a valid team

        Attributes:
            state_prev (dict): The lsat to last game state
            state (dict): The last game state
            reward (list): Reward returned from this state (Not implemented)

        Should return a list of valid actions (in the same order as each of the players)
        """
        pass
