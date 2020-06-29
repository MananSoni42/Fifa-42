from utils import *

class Ball:
    """Implements the football used in the game"""
    def __init__(self, pos):
        self.pos = P(pos)
        self.vel = P(0,0)
        self.free = True
        self.color = (50,50,50)

    def reset(self):
        """ Reset the ball - used after a goal is scored """
        self.pos = P(W//2, H//2)
        self.vel = P(0,0)
        self.free = True

    def goal_check(self):
        """ Check if a goal is scored"""
        if not (BALL_RADIUS < self.pos.x < W - BALL_RADIUS) and GOAL_POS[0]*H < self.pos.y < GOAL_POS[1]*H:
            self.reset()

    def check_capture(self, player):
        """
        If ball is captured, move according to player
        else check if captured
        """
        if not self.free:
            if player.walk_dir == 'L':
                self.pos = player.pos + P(-2, 1.5)*BALL_CENTER
            elif player.walk_dir == 'R':
                self.pos = player.pos + P(2, 1.5)*BALL_CENTER

        elif self.pos.dist(player.pos) < PLAYER_RADIUS + BALL_RADIUS:
            self.vel = P(0,0)
            self.free = False
            self.dir = player.walk_dir

    def update(self, player, a):
        """ Update the ball's state (in-game) according to specified action """
        if self.free:
            self.pos += P(BALL_SPEED,BALL_SPEED)*self.vel
            if not (BALL_RADIUS <= self.pos.x <= W - BALL_RADIUS): # Ball X overflow
                self.pos.x = min(max(BALL_RADIUS, self.pos.x),W - BALL_RADIUS)
                self.vel.x *= (-1) # Flip X velocity
            if not(BALL_RADIUS <= self.pos.y <= H - BALL_RADIUS): # Ball Y overflow
                self.pos.y = min(max(BALL_RADIUS, self.pos.y),H - BALL_RADIUS)
                self.vel.y *= (-1) # Flip Y velocity

        elif a in ['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C']: # Player shoots
            self.vel = P(act[a])
            self.free = True

            # Ball relearse mechanics (when player shoots)
            if self.dir == 'R' and act[a][0] in [0,1]:
                self.pos.x += PLAYER_RADIUS - BALL_RADIUS + 1
            elif self.dir == 'R' and act[a][0] == -1:
                self.pos.x -= (PLAYER_RADIUS + 3*BALL_RADIUS + 1)
            elif self.dir == 'L' and act[a][0] == 1:
                self.pos.x += PLAYER_RADIUS + 3*BALL_RADIUS + 1
            elif self.dir == 'L' and act[a][0] in [0,-1]:
                self.pos.x -= (PLAYER_RADIUS - BALL_RADIUS + 1)

        self.check_capture(player)

    def draw(self, win):
        # Ball boundary
        #pygame.draw.rect(win, (100,100,100), (self.pos[0]- BALL_RADIUS, self.pos[1] - BALL_RADIUS,BALL_RADIUS*2,BALL_RADIUS*2))
        win.blit(FOOTBALL_IMG, (self.pos - BALL_CENTER).val)
