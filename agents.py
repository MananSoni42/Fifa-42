from utils import *
from abc import ABC, abstractmethod
from copy import copy

class Agent(ABC):
    """
    Abstract class that controls agents in the football game
    Implement the move method to instantiate
    """
    def __init__(self, id, team_id, pos, dir='L'):
        self.id = id # Unique ID starts from 0 (also denotes it's position in team array)
        self.team_id = team_id # ID of player's team
        self.pos = P(pos) # Starting position
        self.walk_dir = dir # options are R (right), L (left)
        self.walk_count = 0 # For running animation

    def __str__(self):
        return f'\nAgent {self.id} - {self.pos}'

    def draw(self, win, team_id, debug=False):
        if debug:
            pygame.draw.rect(win, (255,255,255), (self.pos.x-PLAYER_RADIUS, self.pos.y-PLAYER_RADIUS,PLAYER_RADIUS*2,PLAYER_RADIUS*2))
        win.blit(RUN[team_id][self.walk_dir][self.walk_count//WALK_DELAY], (self.pos - PLAYER_CENTER).val)

    def update(self, action, players, dir):
        """ Update player's state (in-game) based on action """
        if action in ['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']:
            if action == 'MOVE_L':
                if self.walk_dir == 'R':
                    self.walk_count = 1
                    self.walk_dir = 'L'
                else:
                    self.walk_count += 1
                    if self.walk_count >= WALK_DELAY*ANIM_NUM:
                        self.walk_count = WALK_DELAY

            elif action == 'MOVE_R':
                if self.walk_dir == 'L':
                    self.walk_count = 1
                    self.walk_dir = 'R'
                else:
                    self.walk_count += 1
                    if self.walk_count >= WALK_DELAY*ANIM_NUM:
                        self.walk_count = WALK_DELAY
            else:
                self.walk_count += 1
                if self.walk_count >= WALK_DELAY*ANIM_NUM:
                    self.walk_count = WALK_DELAY

            self.pos += P(PLAYER_SPEED, PLAYER_SPEED)*P(ACT[action])
            self.pos = P(min(max(PLAYER_RADIUS,self.pos.x),W - PLAYER_RADIUS), min(max(PLAYER_RADIUS,self.pos.y), H - PLAYER_RADIUS)) # account for overflow

    @abstractmethod
    def move(self, state, reward):
        """ Implement this method for a valid agent """
        pass

class HumanAgent(Agent):
    """ Agents controlled by humans """
    def draw(self, win, team_id, selected=False, debug=False):
        if debug:
            pygame.draw.rect(win, (255,255,255), (self.pos.x-PLAYER_RADIUS, self.pos.y-PLAYER_RADIUS,PLAYER_RADIUS*2,PLAYER_RADIUS*2))
        if selected:
            pygame.draw.circle(win, (255, 0, 0), (self.pos - P(0,1.5)*P(0,PLAYER_RADIUS)).val, 5) # mid circle
        win.blit(RUN[team_id][self.walk_dir][self.walk_count//WALK_DELAY], (self.pos - PLAYER_CENTER).val)

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
                    return 'MOVE_L'
                elif event.key == pygame.K_RIGHT:
                    return 'MOVE_R'
                elif event.key == pygame.K_UP:
                    return 'MOVE_U'
                elif event.key == pygame.K_DOWN:
                    return 'MOVE_D'
                else:
                    return 'NOTHING'

class RandomAgent(Agent):
    """ Agents that move randomly """
    def move(self, state, reward):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if np.random.rand() < 0.6:
            return np.random.choice(['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R'])
        else:
            return np.random.choice(['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C'])
