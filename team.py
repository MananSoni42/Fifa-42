from utils import *
from agents import HumanAgent

class Team:
    """ A team of agents """
    def __init__(self, formation, dir='R'):
        self.dir = dir
        self.players = []
        for i in range(NUM_TEAM):
            self.players.append(HumanAgent(id=i, pos=form[formation][i], dir=dir))
        self.nearest = NUM_TEAM//2

    def __str__(self):
        s = "Team:"
        for player in self.players:
            s += player.__str__()
        return s
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
            player.update(action[i], self.dir)
