from utils import *
from abc import ABC, abstractmethod
from agents import HumanAgent

class Team(ABC):
    """
    Abstract class for a team of agents
    """
    def __init__(self, formation, dir='R'):
        self.dir = dir
        self.formation = formation
        self.maintain_formation = True
        self.set_players()

    def __str__(self):
        s = "Team:"
        for player in self.players:
            s += player.__str__()
        return s

    def set_formation(formation):
        self.formation = formation

    def formation_toggle(self):
        self.maintain_formation = not self.maintain_formation

    def draw(self,win):
        for i,player in enumerate(self.players):
            if i == self.nearest:
                player.draw(win,selected=True)
            else:
                player.draw(win)

    def set_nearest(self, ball):
        dists = [player.pos.dist(ball.pos) for player in self.players]
        self.nearest = np.argmin(dists)

    def update(self, action):
        for i,player in enumerate(self.players):
            player.update(action[i], self.players, self.dir)

    @abstractmethod
    def set_players(self):
        pass
    @abstractmethod
    def move(self):
        pass

class HumanTeam(Team):
    """A team of human players"""
    def set_players(self):
        self.players = []
        for i in range(NUM_TEAM):
            self.players.append(HumanAgent(id=i, pos=FORM[self.formation][i], dir=self.dir))

        self.nearest = NUM_TEAM//2

    def formation_dir(self, id):
        player = self.players[id]
        min_dist = 2

        if abs(player.pos.x - FORM[self.formation][id].x) <= min_dist and abs(player.pos.y - FORM[self.formation][id].y) <= min_dist:
            player.walk_count = 0
            player.walk_dir = self.dir
            return 'NOTHING'
        elif player.pos.x - FORM[self.formation][id].x > min_dist:
            return 'MOVE_L'
        elif player.pos.x - FORM[self.formation][id].x < -min_dist:
            return 'MOVE_R'
        elif abs(player.pos.x - FORM[self.formation][id].x) <= min_dist and player.pos.y - FORM[self.formation][id].y > min_dist:
            return 'MOVE_U'
        elif player.pos.x == FORM[self.formation][id].x and player.pos.y - FORM[self.formation][id].y < -min_dist:
            return 'MOVE_D'

    def move(self):
        """
        Move a human team
            * Player nearest to the ball moves through keyboard
            * All other players return to their original positions if maintain_formation is set
        """
        actions = []
        for i,player in enumerate(self.players):
            if i == self.nearest:
                actions.append(player.move(0,0))
            elif self.maintain_formation:
                actions.append(self.formation_dir(i))
            else:
                actions.append('NOTHING')
        return actions
