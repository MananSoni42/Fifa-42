from settings import *
from const import ACT
from abc import ABC, abstractmethod

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
        self.rnd = 0.01*np.random.rand()

    def __str__(self):
        return f'\nAgent {self.id} - {self.pos}'

    def draw(self, win, team_id, debug=False):
        if debug:
            pygame.draw.rect(win, (255,255,255), (self.pos.x-PLAYER_RADIUS, self.pos.y-PLAYER_RADIUS,PLAYER_RADIUS*2,PLAYER_RADIUS*2))
            pygame.draw.circle(win, (255,128,0), (self.pos-PLAYER_CENTER).val, AI_NEAR_RADIUS, LINE_WIDTH)
            pygame.draw.circle(win, (255,0,0), (self.pos-PLAYER_CENTER).val, AI_FAR_RADIUS, LINE_WIDTH)
        win.blit(RUN[team_id][self.walk_dir][self.walk_count//WALK_DELAY], (self.pos - PLAYER_CENTER).val)

    def update(self, action, players):
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

class RandomAgent(Agent):
    """ Agents that move randomly """
    def move(self, state, reward):
        if np.random.rand() < 0.6:
            return np.random.choice(['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R'])
        else:
            return np.random.choice(['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C'])

class OriginalAIAgent(Agent):
    """ Agents that play like the orginal AI """

    def dist_to_line(self, line, pt):
        """
        distance of line x*line[0] + y*line[1] + line[2] = 0 from pt p
        """
        return np.abs(line[0]*pt.x + line[1]*pt.y + line[2])/np.sqrt(line[0]**2 + line[1]**2)

    def ai_pass(self, pos):
        pass

    def ai_move_ball(self, pos, goal_y):
        """
        If this player does not have the ball
        Calculate vectors towards the goal and away from nearby players of the opposite team
        Add up all these vectors and move in that direction (probabilistically)
        """
        player_vec = P(0,0) # Direction vector to move due to opposite team
        for i,pt in enumerate(pos):
            if self.pos.dist(pt) < AI_NEAR_RADIUS:
                dir = pt - self.pos
                mag = (AI_NEAR_RADIUS*PLAYER_RADIUS/dir.mag)**2 # magnitude of vector is proportional to inverse of distance
                player_vec -= P(mag/dir.mag,mag/dir.mag)*dir

        goal_vec = P(goal_y, H//2) - self.pos # Direction vector to move due to goal
        goal_vec *= P(1/goal_vec.mag, 1/goal_vec.mag) # O

        final_vec = goal_vec + player_vec # Final vector is sum

        dir_final = final_vec * P(1/final_vec.mag, 1/final_vec.mag)

        possible_dir = ['NOTHING', 'MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']
        dist_to_dir = [dir_final.dist(ACT[dir]) for dir in possible_dir]
        prob_dist = np.clip(np.exp([1/(d+pow(10,-6)) for d in dist_to_dir]), 0, 1000)
        chosen_dir = np.random.choice(possible_dir, p=np.array(prob_dist)/np.sum(prob_dist))

        return chosen_dir

    def ai_shoot(self, pos):
        pass

    def random_move(self, state, reward):
        if np.random.rand() < 0.6:
            return np.random.choice(['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R'])
        else:
            return np.random.choice(['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C'])

    def move(self, state, reward):
        if state :
            return self.ai_move_ball(state['team1'], state['misc']['goal_y'][1])
        else:
            return 'NOTHING'
