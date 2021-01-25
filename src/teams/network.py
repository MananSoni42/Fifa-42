"""
Create a team that can be controlled over the network
"""

from settings import *
from const import ACT, FORM
from teams.agent import Agent
from teams.team import Team
from queue import Queue

class NetworkAgent(Agent):
    """
    Agent that can be controlled over the network (online)

    Use the ```register_keystroke()``` function to add keys from the server (socket)
    """

    # valid keystrokes (received from the client)
    valid_keys = ['q','w','e','a','d','z','x','c',
                    'up','down','left','right',
                    'space','nothing']

    def __init__(self, id, team_id, pos, dir='L'):
        '''
        Initialize the network agent

        The agent maintains a queue of the received keystrokes
        '''
        super().__init__(id, team_id, pos, dir)
        self.keys = Queue()
        self.maintain_formation = False

    def register_keystroke(self, key):
        '''
        Register a keystroke

        Use this method within the server's socket
        '''
        key = key.lower()
        if key in NetworkAgent.valid_keys:
            self.keys.put(key)
        else:
            print(f'key `{key}` not recognized, replacing with `nothing`')

    def move(self, state_prev, state, reward):
        """
        Move the network agent based on it's internal queue
        """

        if self.keys.empty():
            return 'NOTHING'
        else:
            key = self.keys.get()

            if key == 'a':
                return 'SHOOT_A'
            elif key == 'd':
                return 'SHOOT_D'
            elif key == 'w':
                return 'SHOOT_W'
            elif key == 'x':
                return 'SHOOT_X'
            elif key == 'q':
                return 'SHOOT_Q'
            elif key == 'c':
                return 'SHOOT_C'
            elif key == 'e':
                return 'SHOOT_E'
            elif key == 'z':
                return 'SHOOT_Z'
            elif key == 'left':
                return 'MOVE_L'
            elif key == 'right':
                return 'MOVE_R'
            elif key == 'up':
                return 'MOVE_U'
            elif key == 'down':
                return 'MOVE_D'
            else:
                return 'NOTHING'


class NetworkTeam(Team):
    """
    A team of network players
    """

    def set_players(self, ids):
        self.players = []
        for i in range(NUM_TEAM):
            if i in ids:
                self.players.append(NetworkAgent(
                    id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]['coord']))

        self.selected = NUM_TEAM//2
        self.next_selected = []

    def update(self, action, ball):
        """
        Select a player (based on the Ball's state) and update the team's state based on the received actions and the ball's position
        """
        self.select_player(ball)
        super().update(action, ball)

    def select_player(self, ball):
        """
        Select the player that is controlled by the keyboard

        **Working**:

        - If ball is near the D-area, keeper gets automatic control
        - Otherwise the player nearest to the ball has control (ties are broken randomly)
        """

        argsort = lambda seq: sorted(range(len(seq)), key=seq.__getitem__)
        dists = [player.pos.dist(ball.pos) + player.rnd for player in self.players]
        sorted_dists = sorted(range(len(dists)), key = lambda i: dists[i])
        self.selected = sorted_dists[0] # index of top 3
        self.next_selected = sorted_dists[1:2]

        if min(dists) > PLAYER_RADIUS + BALL_RADIUS and abs(ball.pos.x - self.goal_x) < W//5:
            # If the ball is within the D and is not very near to any other player, give control to the keeper
            self.selected = 0

    def register_keystroke(self, key):
        """
        Register a keystroke for the currently selected player
        """
        self.players[self.selected].register_keystroke(key)

    def formation_dir(self, id):
        """
        Send player (with the given ID) to his designated place in the formation

        **Working**:

        - If player is in-line (horizontally or vertically), move directly towards original point (U/L/D/R)
        - Otherwise choose 2 directions that take you closer to the original point and choose one of them randomly (UL/UR/DL/DR)
        """
        player = self.players[id]
        min_dist = 2

        if abs(player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) <= min_dist and abs(player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) <= min_dist:
            player.walk_count = 0
            return 'NOTHING'
        elif abs(player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) <= min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) > min_dist:
                return 'MOVE_U'
            else:
                return 'MOVE_D'
        elif abs(player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) <= min_dist:
            if (player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) > min_dist:
                return 'MOVE_L'
            else:
                return 'MOVE_R'
        elif (player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) > min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) > min_dist:
                return random.choice(['MOVE_L', 'MOVE_U'])
            else:
                return random.choice(['MOVE_L', 'MOVE_D'])
        elif (player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) < - min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) > min_dist:
                return random.choice(['MOVE_R', 'MOVE_U'])
            else:
                return random.choice(['MOVE_R', 'MOVE_D'])
        else:
            return 'NOTHING'

    def move(self, state_prev, state, reward):
        """
        Move a network team

        **Working**:

        - Player nearest to the ball moves through keyboard
        - All other players return to their original positions (if maintain_formation is set)
        """
        actions = []
        for i, player in enumerate(self.players):
            if i == self.selected:
                actions.append(player.move(state_prev, state, reward))
            elif self.maintain_formation:
                actions.append(self.formation_dir(i))
            else:
                player.walk_count = 0
                actions.append('NOTHING')
        return actions
