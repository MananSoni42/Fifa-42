from settings import *
from const import ACT, POSSESSION, PASS_ACC, SHOT_ACC, GOALS

class Ball:
    """Implements the football used in the game"""
    def __init__(self, pos):
        self.pos = P(pos)
        self.vel = P(0,0)
        self.free = True
        self.color = (50,50,50)
        self.stats = {
            'last_player': -1,
            'last_team': -1,
            'player': -1,
            'team': -1,
        }

    def draw(self, win, debug=False):
        if debug:
            pygame.draw.rect(win, (100,100,100), (self.pos.x-BALL_RADIUS, self.pos.y-BALL_RADIUS,BALL_RADIUS*2,BALL_RADIUS*2))
        if not self.free:
            pygame.draw.circle(win, (255,0,0), self.pos.val, BALL_RADIUS+LINE_WIDTH, LINE_WIDTH)
        win.blit(FOOTBALL_IMG, (self.pos - BALL_CENTER).val)

    def reset(self, pos):
        """ Reset the ball - used after a goal is scored """
        self.pos = P(pos)
        self.vel = P(0,0)
        self.free = True
        self.stats['last_player'] = -1
        self.stats['last_team'] = -1
        self.stats['player'] = -1
        self.stats['team'] = -1

    def goal_check(self):
        """ Check if a goal is scored """
        goal = False
        reset = False
        goals_scored = {1: 0, 2: 0}

        if not (BALL_RADIUS < self.pos.x < W - BALL_RADIUS):
            reset = True
            if self.pos.x <= BALL_RADIUS:
                pos = P(PLAYER_RADIUS + BALL_RADIUS, H//2)
                goals_scored[2] += 1
            else:
                pos = P(W - PLAYER_RADIUS - BALL_RADIUS, H//2)
                goals_scored[1] += 1
            if GOAL_POS[0]*H < self.pos.y < GOAL_POS[1]*H:
                goal = True
                GOALS[1] += goals_scored[1]
                GOALS[2] += goals_scored[2]
                pos = P(W//2, H//2)

        if reset:
            self.update_stats(goal=goal)
            self.reset(pos)
        return goal

    def update_stats(self, player=None, goal=None):
        """
        Sync ball statistics with the global variables
        Activates when a player receives the ball or during a goal attempt
            - Possession: +1 if same team pass is recorded
            - Pass: +1 to succ if same team pass is recorded
                    +1 to fail if diff team pass is recorded
            - Shot: +1 to succ if a goal is scored
                    +1 to fail if goal is not scored (out of bounds) / keeper stops the ball
        """
        if player is not None: # Player receives the ball
            self.stats['last_player'] = self.stats['player']
            self.stats['last_team'] = self.stats['team']
            self.stats['player'] = player.id
            self.stats['team'] = player.team_id

            if self.stats['last_team'] == self.stats['team']: # Same team pass
                if self.stats['last_player'] != self.stats['player'] :
                    POSSESSION[self.stats['team']] += 1
                    PASS_ACC[self.stats['team']]['succ'] += 1
            else: # Different team pass
                if self.stats['last_team'] != -1:
                    if self.stats['player'] == 0: # GK of different team receives the ball
                        SHOT_ACC[self.stats['last_team']]['fail'] += 1
                    else:
                        PASS_ACC[self.stats['last_team']]['fail'] += 1

        elif goal is not None: # Called when a goal is scored
            if goal:
                SHOT_ACC[self.stats['team']]['succ'] += 1
            else:
                SHOT_ACC[self.stats['team']]['fail'] += 1

    def ball_player_collision(self, team):
        for player in team.players:
            if self.pos.dist(player.pos) < PLAYER_RADIUS + BALL_RADIUS:
                self.vel = P(0,0)
                self.free = False
                self.dir = player.walk_dir
                self.update_stats(player)

    def check_capture(self, team1, team2):
        """
        If ball is captured, move according to player
        else check if captured
        """
        if self.stats['team'] == 1:
            player = team1.players[self.stats['player']]
        elif self.stats['team'] == 2:
            player = team2.players[self.stats['player']]

        if not self.free:
            self.dir = player.walk_dir
            if self.dir == 'L':
                self.pos = player.pos + P(-1,1)*BALL_OFFSET*BALL_CENTER
            elif self.dir == 'R':
                self.pos = player.pos + BALL_OFFSET*BALL_CENTER

        else:
            self.ball_player_collision(team1)
            self.ball_player_collision(team2)

    def update(self, team1, team2, action1, action2):
        """ Update the ball's state (in-game) according to specified action """
        if self.stats['team'] == 1:
            a = action1[self.stats['player']]
        elif self.stats['team'] == 2:
            a = action2[self.stats['player']]

        if self.free:
            self.pos += P(BALL_SPEED,BALL_SPEED)*self.vel
            if not (BALL_RADIUS <= self.pos.x <= W - BALL_RADIUS): # Ball X overflow
                self.pos.x = min(max(BALL_RADIUS, self.pos.x),W - BALL_RADIUS)
                self.vel.x *= (-1) # Flip X velocity
            if not(BALL_RADIUS <= self.pos.y <= H - BALL_RADIUS): # Ball Y overflow
                self.pos.y = min(max(BALL_RADIUS, self.pos.y),H - BALL_RADIUS)
                self.vel.y *= (-1) # Flip Y velocity

        elif a in ['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C']: # Player shoots
            self.vel = P(ACT[a])
            self.free = True
            # Ball relearse mechanics (when player shoots)
            const = PLAYER_RADIUS + BALL_RADIUS + 1
            if self.dir == 'R' and ACT[a][0] >= 0:
                self.pos.x += const - BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'R' and ACT[a][0] < 0:
                self.pos.x -= const + BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'L' and ACT[a][0] > 0:
                self.pos.x += const + BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'L' and ACT[a][0] <= 0:
                self.pos.x -= const - BALL_RADIUS*BALL_OFFSET.x

        self.check_capture(team1, team2)
