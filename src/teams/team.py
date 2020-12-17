from settings import *
from const import FORM, recolor
from abc import ABC, abstractmethod
from teams.agent import HumanAgent, RandomAgent

class Team(ABC):
    """
    Abstract class for a team of agents
    """
    def __init__(self, id, formation, color):
        self.id = id
        self.color = color
        self.formation = formation
        self.maintain_formation = True
        self.set_players()
        #self.set_color()

    def __str__(self):
        s = f'Team {self.id}:'
        for player in self.players:
            s += player.__str__()
        return s

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
            player.draw(win, self.color, debug=debug)

    def update(self, action):
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
    def move(self):
        """ Move the entire team (may use the player's move method) """
        pass

class HumanTeam(Team):
    """A team of human players"""
    def draw(self,win, debug=False):
        for i,player in enumerate(self.players):
            if i == self.nearest:
                player.draw(win, (1,1,1), selected=True, debug=debug)
            else:
                player.draw(win, self.color, debug=debug)


    def set_nearest(self, ball):
        dists = [player.pos.dist(ball.pos) + 0.01*np.random.rand() for player in self.players]
        self.nearest = np.argmin(dists)

    def set_players(self):
        self.players = []
        for i in range(NUM_TEAM):
            self.players.append(HumanAgent(id=i, team_id=self.id, pos=FORM[self.formation][i]))

        self.nearest = NUM_TEAM/2

    def formation_dir(self, id):
        """ Send player with given id to his designated place in the formation """
        player = self.players[id]
        min_dist = 2

        """
        If player is in-line (horizontally or vertically), move directly towards original point (U/L/D/R)
        Otherwise choose 2 directions that take you closer to the original point and choose one of them randomly (UL/UR/DL/DR)
        """
        if abs(player.pos.x - FORM[self.formation][id].x) <= min_dist and abs(player.pos.y - FORM[self.formation][id].y) <= min_dist:
            player.walk_count = 0
            return 'NOTHING'
        elif abs(player.pos.x - FORM[self.formation][id].x) <= min_dist:
            if (player.pos.y - FORM[self.formation][id].y) > min_dist:
                return 'MOVE_U'
            else:
                return 'MOVE_D'
        elif abs(player.pos.y - FORM[self.formation][id].y) <= min_dist:
            if (player.pos.x - FORM[self.formation][id].x) > min_dist:
                return 'MOVE_L'
            else:
                return 'MOVE_R'
        elif (player.pos.x - FORM[self.formation][id].x) > min_dist:
            if (player.pos.y - FORM[self.formation][id].y) > min_dist:
                return np.random.choice(['MOVE_L', 'MOVE_U'])
            else:
                return np.random.choice(['MOVE_L', 'MOVE_D'])
        elif (player.pos.x - FORM[self.formation][id].x) < -min_dist:
            if (player.pos.y - FORM[self.formation][id].y) > min_dist:
                return np.random.choice(['MOVE_R', 'MOVE_U'])
            else:
                return np.random.choice(['MOVE_R', 'MOVE_D'])

    def move(self):
        """
        Move a human team
            * Player nearest to the ball moves through keyboard
            * All other players return to their original positions (if maintain_formation is set)
        """
        actions = []
        for i,player in enumerate(self.players):
            if i == self.nearest:
                actions.append(player.move(0,0))
            elif self.maintain_formation:
                actions.append(self.formation_dir(i))
            else:
                player.walk_count = 0
                actions.append('NOTHING')
        return actions

class RandomTeam(Team):
    """A team of random players"""
    def set_players(self):
        self.players = []
        for i in range(NUM_TEAM):
            self.players.append(RandomAgent(id=i, team_id=self.id, pos=FORM[self.formation][i]))

        self.nearest = NUM_TEAM/2

    def move(self):
        """ Move each player randomly """
        actions = []
        for i,player in enumerate(self.players):
            actions.append(player.move(0,0))
        return actions
