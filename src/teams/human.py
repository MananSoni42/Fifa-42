"""
Create a Human team i.e. controlled by the keyboard
"""

from settings import *
from math import sin,cos,pi
from const import ACT, FORM
from teams.agent import Agent
from teams.team import Team

class HumanAgent(Agent):
    """
    Agents controlled by humans
    """

    def draw(self, win, cam, team_id, selected=0, debug=False):
        """
        Draw the human agent. Also draws a red triangle on top of the selected player
        """
        cols = {
            1:(255, 0, 0),
            2:(200, 70, 70),
        }
        if selected:
            pt = self.pos - P(0, 1.5)*P(0, PLAYER_RADIUS)
            R = P(PLAYER_SELECT_RADIUS, PLAYER_SELECT_RADIUS)
            cam.polygon(win, cols[selected],
                [(pt + R*P(cos(-1*pi/6), sin(-1*pi/6))).val,
                 (pt + R*P(cos(-5*pi/6), sin(-5*pi/6))).val,
                 (pt + R*P(cos(-9*pi/6), sin(-9*pi/6))).val],
            ) # Triangle
        super().draw(win, cam, team_id, debug=debug)


    def move(self, state_prev, state, reward, selected):
        """
        Move the human agent based on the keyboard
        """

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            return 'SHOOT_A'
        elif keys[pygame.K_d]:
            return 'SHOOT_D'
        elif keys[pygame.K_w]:
            return 'SHOOT_W'
        elif keys[pygame.K_x]:
            return 'SHOOT_X'
        elif keys[pygame.K_q]:
            return 'SHOOT_Q'
        elif keys[pygame.K_c]:
            return 'SHOOT_C'
        elif keys[pygame.K_e]:
            return 'SHOOT_E'
        elif keys[pygame.K_z]:
            return 'SHOOT_Z'
        elif keys[pygame.K_LEFT]:
            return 'MOVE_L'
        elif keys[pygame.K_RIGHT]:
            return 'MOVE_R'
        elif keys[pygame.K_UP]:
            return 'MOVE_U'
        elif keys[pygame.K_DOWN]:
            return 'MOVE_D'
        else:
            return 'NOTHING'

class HumanTeam(Team):
    """
    A team of human players
    """

    def set_players(self, ids):
        self.players = []
        for i in range(NUM_TEAM):
            if i in ids:
                self.players.append(HumanAgent(
                    id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]['coord']))

        self.selected = NUM_TEAM//2
        self.next_selected = []

    def update(self, action, ball):
        """
        Select a player (based on the Ball's state) and update the team's state based on the received actions and the ball's position
        """
        self.select_player(ball)
        super().update(action, ball)

    def draw(self, win, cam, debug):
        """
        Draw the human team
        """
        for i, player in enumerate(self.players):
            if i == self.selected:
                player.draw(win, cam, self.id, selected=1, debug=debug)
            elif i in self.next_selected:
                player.draw(win, cam, self.id, selected=2, debug=debug)
            else:
                player.draw(win, cam, self.id, selected=0, debug=debug)

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

    def move(self, state_prev, state, reward):
        """
        Move a human team

        **Working**:

        - Player nearest to the ball moves through keyboard
        - All other players return to their original positions (if maintain_formation is set)
        """
        actions = []
        for i, player in enumerate(self.players):
            if i == self.selected:
                actions.append(player.check_move(state_prev, state, reward))
            elif self.maintain_formation:
                actions.append(self.formation_dir(i))
            else:
                player.walk_count = 0
                actions.append('NOTHING')
        return actions
