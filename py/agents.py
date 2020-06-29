from utils import *

class HumanAgent(object):
    """Agents controlled by humans"""
    def __init__(self, id, type, pos, color=(255,0,0)):
        self.id = id
        self.type = type
        self.pos = pos
        self.color = color
        self.hasBall = False
        self.walk_dir = 'L' # options are R,L
        self.walk_count = 0
        self.run = {
            'L': {k:pygame.transform.scale(pygame.image.load(v), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for k,v in RUN_LEFT.items()},
            'R': {k:pygame.transform.scale(pygame.image.load(v), (2*PLAYER_RADIUS, 2*PLAYER_RADIUS)) for k,v in RUN_RIGHT.items()},
        }
    def draw(self, win):
        # Player boundary
        #pygame.draw.rect(win, (255,255,255), (self.pos[0]- PLAYER_RADIUS, self.pos[1] - PLAYER_RADIUS,PLAYER_RADIUS*2,PLAYER_RADIUS*2))
        win.blit(self.run[self.walk_dir][(self.walk_count%33)//3], (self.pos[0]-PLAYER_RADIUS, self.pos[1]-PLAYER_RADIUS))

    def move(self, state, reward):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if self.hasBall:
                    if event.key == pygame.K_q:
                        return 'SHOOT_Q'
                    elif event.key == pygame.K_w:
                        return 'SHOOT_W'
                    elif event.key == pygame.K_e:
                        return 'SHOOT_E'
                    elif event.key == pygame.K_a:
                        return 'SHOOT_A'
                    elif event.key == pygame.K_d:
                        return 'SHOOT_D'
                    elif event.key == pygame.K_z:
                        return 'SHOOT_Z'
                    elif event.key == pygame.K_x:
                        return 'SHOOT_X'
                    elif event.key == pygame.K_c:
                        return 'SHOOT_C'
                    elif event.key == pygame.K_LEFT:
                        if self.walk_dir == 'R':
                            self.walk_count = 0
                            self.walk_dir = 'L'
                        else:
                            self.walk_count+=1
                        return 'MOVE_L'
                    elif event.key == pygame.K_RIGHT:
                        if self.walk_dir == 'L':
                            self.walk_count = 0
                            self.walk_dir = 'R'
                        else:
                            self.walk_count+=1
                        return 'MOVE_R'
                    elif event.key == pygame.K_UP:
                        return 'MOVE_U'
                    elif event.key == pygame.K_DOWN:
                        return 'MOVE_D'
                    else:
                        return 'NOTHING'
                else:
                    if event.key == pygame.K_LEFT:
                        if self.walk_dir == 'R':
                            self.walk_count = 0
                            self.walk_dir = 'L'
                        else:
                            self.walk_count+=1
                        return 'MOVE_L'
                    elif event.key == pygame.K_RIGHT:
                        if self.walk_dir == 'L':
                            self.walk_count = 0
                            self.walk_dir = 'R'
                        else:
                            self.walk_count+=1
                        return 'MOVE_R'
                    elif event.key == pygame.K_UP:
                        return 'MOVE_U'
                    elif event.key == pygame.K_DOWN:
                        return 'MOVE_D'
                    else:
                        return 'NOTHING'
