from utils import *
from abc import ABC, abstractmethod

class Agent(ABC):
    """ Abstract class that controls agents in the football game """
    def __init__(self, id, type, pos, color=(255,0,0)):
        self.id = id # Unique ID starts from 0 (also denotes it's position in team array)
        self.type = type # To be used later
        self.pos = P(pos) # Starting position
        self.color = color # Colour (R,G,B) triple
        self.walk_dir = 'L' # options are R (right), L (left)
        self.walk_count = 0 # For running animation

    def draw(self, win):
        # Player boundary
        #pygame.draw.rect(win, (255,255,255), (self.pos[0]- PLAYER_RADIUS, self.pos[1] - PLAYER_RADIUS,PLAYER_RADIUS*2,PLAYER_RADIUS*2))
        win.blit(RUN[self.walk_dir][(self.walk_count%33)//3], (self.pos - PLAYER_CENTER).val)

    def update(self, a):
        """ Update player's state (in-game) based on action """
        if a in ['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']:
            self.pos += P(PLAYER_SPEED, PLAYER_SPEED)*P(act[a])
            self.pos = P(min(max(PLAYER_RADIUS,self.pos.x),W - PLAYER_RADIUS), min(max(PLAYER_RADIUS,self.pos.y), H - PLAYER_RADIUS)) # account for overflow

    @abstractmethod
    def move(self, state, reward):
        """ Implement this method for a valid agent """
        pass

class HumanAgent(Agent):
    """Agents controlled by humans"""
    def move(self, state, reward):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
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

class SimpleAIAgent(Agent):
    def move(self, state, reward):
        pass

class RLAgent(Agent):
    def move(self,state,reward):
        pass
