from utils import *

class Ball:
    """Implements the football used in the game"""
    def __init__(self, pos):
        self.pos = P(pos)
        self.vel = P(0,0)
        self.free = True
        self.color = (50,50,50)
        self.player_id = -1

    def draw(self, win, debug=False):
        if debug:
            pygame.draw.rect(win, (100,100,100), (self.pos.x-BALL_RADIUS, self.pos.y-BALL_RADIUS,BALL_RADIUS*2,BALL_RADIUS*2))
        win.blit(FOOTBALL_IMG, (self.pos - BALL_CENTER).val)

    def reset(self):
        """ Reset the ball - used after a goal is scored """
        self.pos = P(W//2, H//2)
        self.vel = P(0,0)
        self.free = True

    def goal_check(self):
        """ Check if a goal is scored """
        if not (BALL_RADIUS < self.pos.x < W - BALL_RADIUS) and GOAL_POS[0]*H < self.pos.y < GOAL_POS[1]*H:
            self.reset()

    def check_capture(self, team):
        """
        If ball is captured, move according to player
        else check if captured
        """
        player = team.players[self.player_id]
        if not self.free:
            self.dir = player.walk_dir
            if self.dir == 'L':
                self.pos = player.pos + P(-1,1)*BALL_OFFSET*BALL_CENTER
            elif self.dir == 'R':
                self.pos = player.pos + BALL_OFFSET*BALL_CENTER

        else:
            for i,player in enumerate(team.players):
                if self.pos.dist(player.pos) < PLAYER_RADIUS + BALL_RADIUS:
                    self.vel = P(0,0)
                    self.free = False
                    self.player_id = i
                    self.dir = player.walk_dir

    def update(self, team, action):
        """ Update the ball's state (in-game) according to specified action """
        a = action[self.player_id]

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
            if self.dir == 'R' and ACT[a][0] in [0,1]:
                self.pos.x += const - BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'R' and ACT[a][0] == -1:
                self.pos.x -= const + BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'L' and ACT[a][0] == 1:
                self.pos.x += const + BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'L' and ACT[a][0] in [0,-1]:
                self.pos.x -= const - BALL_RADIUS*BALL_OFFSET.x

        self.check_capture(team)
