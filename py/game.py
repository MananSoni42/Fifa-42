from utils import *
from ball import Ball

class Game:
    """Class that controls the entire game"""
    def __init__(self, player):
        self.player = player
        self.ball = Ball(pos=(W//2, H//2))
        self.end = False
        self.bg = pygame.transform.scale(pygame.image.load(BACKGROUND_IMG), (W, H))
        self.bg.set_alpha(128)
    def draw(self, win):
        #win.blit(self.bg, (0, 0)) # grass
        win.fill((14, 156, 23)) # constant green
        pygame.draw.rect(win, (255, 255, 255), (0, 0, W, 3)) # border
        pygame.draw.rect(win, (255, 255, 255), (0, H-3, W, 3)) # border
        pygame.draw.rect(win, (255, 255, 255), (0, 0, 3, H)) # border
        pygame.draw.rect(win, (255, 255, 255), (W-3, 0, 3, H)) # border
        pygame.draw.rect(win, (255, 255, 255), (W//2 - 3, 0, 6, H)) # mid line
        pygame.draw.circle(win, (255, 255, 255), (W//2, H//2), H//5, 6) # mid circle

        self.player.draw(win)
        self.ball.draw(win)

    def next(self, a):
        if self.ball.free: # Move ball
            x,y = self.ball.pos
            x += BALL_SPEED*self.ball.vel[0]
            y += BALL_SPEED*self.ball.vel[1]
            if not (BALL_RADIUS <= x <= W - BALL_RADIUS): # Ball X overflow
                x -= BALL_SPEED*self.ball.vel[0]
                self.ball.vel = (-self.ball.vel[0],self.ball.vel[1]) # flip x veloity
            if not(BALL_RADIUS <= y <= H - BALL_RADIUS): # Ball Y overflow
                y -= BALL_SPEED*self.ball.vel[1]
                self.ball.vel = (self.ball.vel[0],-self.ball.vel[1]) # flip y velocity
            self.ball.pos = (x,y)

        if a in ['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']: # Move player
            x,y = self.player.pos
            x += PLAYER_SPEED*act[a][0]
            y += PLAYER_SPEED*act[a][1]
            if PLAYER_RADIUS <= x <= W - PLAYER_RADIUS and PLAYER_RADIUS <= y <= H - PLAYER_RADIUS:
                self.player.pos = (x,y)

        if not self.ball.free and a in ['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C']: # Player shoots
            self.ball.vel = act[a]
            self.ball.free = True

            if self.player.walk_dir == 'R' and act[a][0] in [0,1]:
                xincr = PLAYER_RADIUS - BALL_RADIUS + 1
            elif self.player.walk_dir == 'R' and act[a][0] == -1:
                xincr = -(PLAYER_RADIUS + 3*BALL_RADIUS + 1)
            elif self.player.walk_dir == 'L' and act[a][0] == 1:
                xincr = PLAYER_RADIUS + 3*BALL_RADIUS + 1
            elif self.player.walk_dir == 'L' and act[a][0] in [0,-1]:
                xincr = -(PLAYER_RADIUS - BALL_RADIUS + 1)

            self.ball.pos = (self.ball.pos[0]+xincr, self.ball.pos[1])

        if not self.ball.free:
            if self.player.walk_dir == 'L':
                self.ball.pos = (self.player.pos[0] - 2*BALL_RADIUS, self.player.pos[1] + 3*BALL_RADIUS//2)
            elif self.player.walk_dir == 'R':
                self.ball.pos = (self.player.pos[0] + 2*BALL_RADIUS, self.player.pos[1] + 3*BALL_RADIUS//2)

        elif dist(self.ball.pos, self.player.pos) < PLAYER_RADIUS + BALL_RADIUS:
            self.ball.vel = (0,0)
            self.ball.free = False
            self.ball.player_id = self.player.id
            self.player.hasBall = True

        return 0,0
