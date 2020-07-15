from settings import *
from const import FORM, recolor
from abc import ABC, abstractmethod
from agents import HumanAgent, RandomAgent, OriginalAIAgent

class Team(ABC):
    """
    Abstract class for a team of agents
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

class HumanTeam(Team):
    """A team of human players"""
    def draw(self,win, debug=False):
        for i,player in enumerate(self.players):
            if i == self.selected:
                player.draw(win, team_id=self.id, selected=True, debug=debug)
            else:
                player.draw(win, team_id=self.id, debug=debug)

    def update(self, action, ball):
        self.select_player(ball)
        super().update(action,ball)

    def select_player(self, ball):
        """
        Select the player that is controlled by the keyboard
            - If ball is near the D-area, keeper gets automatic control
            - Otherwise the player nearest to the ball has control (ties are broken randomly)
        """
        dists = [player.pos.dist(ball.pos) + player.rnd for player in self.players]
        self.selected = np.argmin(dists) # Default - Ball goes to nearest player

        if min(dists) > PLAYER_RADIUS + BALL_RADIUS and abs(ball.pos.x - self.goal_x) < W//5:
            # If the ball is within the D and is not very near to any other player, give control to the keeper
            self.selected = 0


    def set_players(self):
        self.players = []
        for i in range(NUM_TEAM):
            self.players.append(HumanAgent(id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]))

        self.selected = NUM_TEAM//2

    def formation_dir(self, id):
        """ Send player with given id to his designated place in the formation """
        player = self.players[id]
        min_dist = 2

        """
        If player is in-line (horizontally or vertically), move directly towards original point (U/L/D/R)
        Otherwise choose 2 directions that take you closer to the original point and choose one of them randomly (UL/UR/DL/DR)
        """
        if abs(player.pos.x - FORM[self.formation][self.dir][id].x) <= min_dist and abs(player.pos.y - FORM[self.formation][self.dir][id].y) <= min_dist:
            player.walk_count = 0
            return 'NOTHING'
        elif abs(player.pos.x - FORM[self.formation][self.dir][id].x) <= min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id].y) > min_dist:
                return 'MOVE_U'
            else:
                return 'MOVE_D'
        elif abs(player.pos.y - FORM[self.formation][self.dir][id].y) <= min_dist:
            if (player.pos.x - FORM[self.formation][self.dir][id].x) > min_dist:
                return 'MOVE_L'
            else:
                return 'MOVE_R'
        elif (player.pos.x - FORM[self.formation][self.dir][id].x) > min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id].y) > min_dist:
                return np.random.choice(['MOVE_L', 'MOVE_U'])
            else:
                return np.random.choice(['MOVE_L', 'MOVE_D'])
        elif (player.pos.x - FORM[self.formation][self.dir][id].x) < - min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id].y) > min_dist:
                return np.random.choice(['MOVE_R', 'MOVE_U'])
            else:
                return np.random.choice(['MOVE_R', 'MOVE_D'])
        else:
            return 'NOTHING'

    def move(self, state, reward):
        """
        Move a human team
            * Player nearest to the ball moves through keyboard
            * All other players return to their original positions (if maintain_formation is set)
        """
        actions = []
        for i,player in enumerate(self.players):
            if i == self.selected:
                actions.append(player.move(state, reward))
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
            self.players.append(RandomAgent(id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]))

    def move(self, state, reward):
        """ Move each player randomly """
        actions = []
        for i,player in enumerate(self.players):
            actions.append(player.move(state, reward))
        return actions

class OriginalAITeam(Team):
    """The AI team used in the original (C++) version"""
    def set_players(self):
        self.players = []
        for i in range(NUM_TEAM):
            self.players.append(OriginalAIAgent(id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]))

    def select_player(self, ball):
        """
        Select the player that is controlled by the keyboard
            - If ball is near the D-area, keeper gets automatic control
            - Otherwise the player nearest to the ball has control (ties are broken randomly)
        """
        dists = [player.pos.dist(ball.pos) + player.rnd for player in self.players]
        self.selected = np.argmin(dists) # Default - Ball goes to nearest player

        if min(dists) > PLAYER_RADIUS + BALL_RADIUS and abs(ball.pos.x - self.goal_x) < W//5:
            # If the ball is within the D and is not very near to any other player, give control to the keeper
            self.selected = 0

    def formation_dir(self, id):
        """ Send player with given id to his designated place in the formation """
        player = self.players[id]
        min_dist = 2

        """
        If player is in-line (horizontally or vertically), move directly towards original point (U/L/D/R)
        Otherwise choose 2 directions that take you closer to the original point and choose one of them randomly (UL/UR/DL/DR)
        """
        if abs(player.pos.x - FORM[self.formation][self.dir][id].x) <= min_dist and abs(player.pos.y - FORM[self.formation][self.dir][id].y) <= min_dist:
            player.walk_count = 0
            return 'NOTHING'
        elif abs(player.pos.x - FORM[self.formation][self.dir][id].x) <= min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id].y) > min_dist:
                return 'MOVE_U'
            else:
                return 'MOVE_D'
        elif abs(player.pos.y - FORM[self.formation][self.dir][id].y) <= min_dist:
            if (player.pos.x - FORM[self.formation][self.dir][id].x) > min_dist:
                return 'MOVE_L'
            else:
                return 'MOVE_R'
        elif (player.pos.x - FORM[self.formation][self.dir][id].x) > min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id].y) > min_dist:
                return np.random.choice(['MOVE_L', 'MOVE_U'])
            else:
                return np.random.choice(['MOVE_L', 'MOVE_D'])
        elif (player.pos.x - FORM[self.formation][self.dir][id].x) < - min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id].y) > min_dist:
                return np.random.choice(['MOVE_R', 'MOVE_U'])
            else:
                return np.random.choice(['MOVE_R', 'MOVE_D'])
        else:
            return 'NOTHING'

    def move(self, state, reward):
        """ Move each player """
        actions = []
        if state:
            self.select_player(state['ball'])
        else:
            self.selected = NUM_TEAM//2
        for i,player in enumerate(self.players):
            move = player.move(state,reward,self.selected)
            if move != 'FORM':
                actions.append(move)
            else:
                actions.append(self.formation_dir(i))
        return actions
