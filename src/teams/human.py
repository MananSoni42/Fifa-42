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

    def draw(self, win, cam, team_id, selected=False, debug=False):
        """
        Draw the human agent. Also draws a red triangle on top of the selected player
        """
        if selected:
            pt = self.pos - P(0, 1.5)*P(0, PLAYER_RADIUS)
            R = P(PLAYER_SELECT_RADIUS, PLAYER_SELECT_RADIUS)
            cam.polygon(win, (255, 0, 0),
                [(pt + R*P(cos(-1*pi/6), sin(-1*pi/6))).val,
                 (pt + R*P(cos(-5*pi/6), sin(-5*pi/6))).val,
                 (pt + R*P(cos(-9*pi/6), sin(-9*pi/6))).val],
            ) # Triangle
        super().draw(win, cam, team_id, debug=debug)

    def move(self, state_prev, state, reward):
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
            player.draw(win, cam, self.id, selected=(
                i == self.selected), debug=debug)

    def select_player(self, ball):
        """
        Select the player that is controlled by the keyboard

        **Working**:

        - If ball is near the D-area, keeper gets automatic control
        - Otherwise the player nearest to the ball has control (ties are broken randomly)
        """
        dists = [player.pos.dist(ball.pos) +
                 player.rnd for player in self.players]
        # Default - Ball goes to nearest player
        self.selected = dists.index(min(dists))

        if min(dists) > PLAYER_RADIUS + BALL_RADIUS and abs(ball.pos.x - self.goal_x) < W//5:
            # If the ball is within the D and is not very near to any other player, give control to the keeper
            self.selected = 0

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
        Move a human team

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
