from utils import *

class Ball:
    """Implements the football used in the game"""
    def __init__(self, pos):
        self.pos = pos
        self.vel = (0,0)
        self.free = True
        self.color = (50,50,50)

    def reset(self):
        self.pos = (W//2, H//2)
        self.vel = (0,0)
        self.free = True

    def goal_check(self):
        if not (BALL_RADIUS < self.pos[0] < W - BALL_RADIUS) and GOAL_POS[0]*H < self.pos[1] < GOAL_POS[1]*H:
            print('GOAL....')
            self.reset()

    def check_capture(self, player):
        """
        If ball is captured, move according to player
        else check if captured
        """
        if not self.free:
            if player.walk_dir == 'L':
                self.pos = (player.pos[0] - 2*BALL_RADIUS, player.pos[1] + 3*BALL_RADIUS//2)
            elif player.walk_dir == 'R':
                self.pos = (player.pos[0] + 2*BALL_RADIUS, player.pos[1] + 3*BALL_RADIUS//2)

        elif dist(self.pos, player.pos) < PLAYER_RADIUS + BALL_RADIUS:
            self.vel = (0,0)
            self.free = False
            self.dir = player.walk_dir

    def update(self, player, a):
        if self.free:
            x,y = self.pos
            x += BALL_SPEED*self.vel[0]
            y += BALL_SPEED*self.vel[1]
            if not (BALL_RADIUS <= x <= W - BALL_RADIUS): # Ball X overflow
                x = min(max(BALL_RADIUS,x),W - BALL_RADIUS)
                self.vel = (-self.vel[0],self.vel[1]) # flip x veloity
            if not(BALL_RADIUS <= y <= H - BALL_RADIUS): # Ball Y overflow
                y = min(max(BALL_RADIUS,y),H - BALL_RADIUS)
                self.vel = (self.vel[0],-self.vel[1]) # flip y velocity
            self.pos = (x,y)

        elif a in ['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C']: # Player shoots
            self.vel = act[a]
            self.free = True

            # Ball relearse mechanics (when player shoots)
            if self.dir == 'R' and act[a][0] in [0,1]:
                xincr = PLAYER_RADIUS - BALL_RADIUS + 1
            elif self.dir == 'R' and act[a][0] == -1:
                xincr = -(PLAYER_RADIUS + 3*BALL_RADIUS + 1)
            elif self.dir == 'L' and act[a][0] == 1:
                xincr = PLAYER_RADIUS + 3*BALL_RADIUS + 1
            elif self.dir == 'L' and act[a][0] in [0,-1]:
                xincr = -(PLAYER_RADIUS - BALL_RADIUS + 1)

            self.pos = (self.pos[0]+xincr, self.pos[1])

        self.check_capture(player)

    def draw(self, win):
        # Ball boundary
        #pygame.draw.rect(win, (100,100,100), (self.pos[0]- BALL_RADIUS, self.pos[1] - BALL_RADIUS,BALL_RADIUS*2,BALL_RADIUS*2))
        win.blit(FOOTBALL_IMG, (self.pos[0] - BALL_RADIUS, self.pos[1] - BALL_RADIUS))
