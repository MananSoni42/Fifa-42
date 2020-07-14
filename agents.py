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
            #pygame.draw.circle(win, (255,128,0), (self.pos-PLAYER_CENTER).val, AI_NEAR_RADIUS, LINE_WIDTH)
            pygame.draw.circle(win, (255,0,0), (self.pos-PLAYER_CENTER).val, AI_FAR_RADIUS, LINE_WIDTH)
            pygame.draw.circle(win, (255,0,0), (self.pos-PLAYER_CENTER).val, AI_FAR_RADIUS, LINE_WIDTH)

            pl_font = pygame.font.Font(FONT_PATH, FONT_SIZE)
            text = pl_font.render(str(self.id), True, (0,0,0))
            win.blit(text, self.pos.val)

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
        distance of
            line: x*line[0] + y*line[1] + line[2] = 0
            from point: p
        """
        return np.abs(line[0]*pt.x + line[1]*pt.y + line[2])/np.sqrt(line[0]**2 + line[1]**2)

    def ai_move_with_ball(self, pos, goal_x):
        """
        If this player has the ball
        Calculate vectors towards the goal and away from nearby players of the opposite team
        Add up all these vectors and move in that direction (probabilistically)
        pos: positions of all of the enemy team
        goal_x: x-coordinate of enemy goal
        """
        player_vec = P(0,0) # Direction vector to move due to opposite team
        for i,pt in enumerate(pos):
            if self.pos.dist(pt) < AI_NEAR_RADIUS:
                dir = pt - self.pos
                mag = (AI_NEAR_RADIUS*PLAYER_RADIUS/dir.mag)**2 # magnitude of vector is proportional to inverse of distance
                player_vec -= P(mag/dir.mag,mag/dir.mag)*dir

        goal_vec = P(goal_x, H//2) - self.pos # Direction vector to move due to goal
        goal_vec *= P(1/goal_vec.mag, 1/goal_vec.mag) # O

        final_vec = goal_vec + player_vec # Final vector is sum

        dir_final = final_vec * P(1/final_vec.mag, 1/final_vec.mag)

        possible_dir = ['NOTHING', 'MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']
        dist_to_dir = [dir_final.dist(ACT[dir]) for dir in possible_dir]
        prob_dist = np.clip(np.exp([1/(d+pow(10,-6)) for d in dist_to_dir]), 0, 1000)
        chosen_dir = np.random.choice(possible_dir, p=np.array(prob_dist)/np.sum(prob_dist))

        return chosen_dir

    def ai_move_without_ball(self, ball_pos):
        """
        Move towards the ball if it is nearby
        Moves probabilistically
        ball_pos: Position of the ball
        """
        if self.pos.dist(ball_pos) < AI_FAR_RADIUS:
            vec = ball_pos - self.pos
            vec_dir = P(1/vec.mag,1/vec.mag)*vec

            possible_dir = ['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']
            dist_to_dir = [vec_dir.dist(ACT[dir]) for dir in possible_dir]
            prob_dist = np.clip(np.exp([1/(d+pow(10,-6)) for d in dist_to_dir]), 0, 1000)
            chosen_dir = np.random.choice(possible_dir, p=np.array(prob_dist)/np.sum(prob_dist))
            return chosen_dir
        else:
            return 'NOTHING'

    def ai_pass(self, team_pos, enemy_team_pos):
        """
        Pass the ball such that the perpendicular distance to the pass line is less than
        AI_MIN_PASS_DIST and no enemy is nearer than a team player in that direction
        pos: Postions of all teammates

        Note:   y co-ordinates need to be inverted everywhere because the origin is at top-left
                instead of the standard bottom-left
        """

        prefs  = {
            'SHOOT_Q': {'priority': 1, 'angle': np.pi*3/4, 'dir': P(-1,-1)},
            'SHOOT_A': {'priority': 1, 'angle': np.pi, 'dir': P(-1,0)},
            'SHOOT_Z': {'priority': 1, 'angle': np.pi*5/4, 'dir': P(-1,1)},
            'SHOOT_W': {'priority': 2, 'angle': np.pi/2, 'dir': P(0,1)},
            'SHOOT_X': {'priority': 2, 'angle': np.pi*3/2, 'dir': P(0,-1)},
            'SHOOT_E': {'priority': 3, 'angle': np.pi/4, 'dir': P(1,-1)},
            'SHOOT_C': {'priority': 3, 'angle': np.pi*7/4, 'dir': P(1,1)},
            'SHOOT_D': {'priority': 4, 'angle': 0, 'dir': P(1,0)},
        }

        possible_passes  = []

        for k,v in prefs.items():
            line = [ # Equation of line as A*x +B*y + C = 0
                    np.sin(v['angle']), # x coeff
                    -np.cos(v['angle']), # y coeff
                    -self.pos.y*np.cos(v['angle']) - self.pos.x*np.sin(v['angle']), # constant
            ]
            for i,player_pos in enumerate(team_pos):
                if i != self.id:
                    team_dist = self.dist_to_line(line, P(1,-1)*player_pos)
                    if  (team_dist < AI_MIN_PASS_DIST and # player is near enough to receive the ball
                         (player_pos.x - self.pos.x)*v['dir'].x >= 0 and # In correct x-direction (not behind the line)
                         -(player_pos.y - self.pos.y)*v['dir'].y >= 0): # In correct y-direction

                        enemy_dist = np.inf
                        enemy_min_pos = P(0,0)
                        for j,enemy_pos in enumerate(enemy_team_pos): # Check for all enemies
                            if self.dist_to_line(line, P(1,-1)*enemy_pos) < enemy_dist:
                                enemy_dist = self.dist_to_line(line, P(1,-1)*enemy_pos)
                                enemy_min_pos = enemy_pos

                        if  (enemy_dist < team_dist and # enemy is nearer than team player
                            (self.pos.x - enemy_min_pos.x)*v['dir'].x >= 0 and # In correct x-direction (not behind the line)
                            (self.pos.y - enemy_min_pos.y)*v['dir'].y >= 0): # In correct y-direction

                            continue # Don't add to possible passes

                        else:
                            possible_passes.append(
                                (v['priority'],
                                team_dist,
                                k,
                                i)
                            )

        # Sort by priority then distance
        if possible_passes != []:
            ai_pass = sorted(possible_passes)[0][2]
        else:
            ai_pass = 'NOTHING'
        return ai_pass

    def ai_shoot(self, pos):
        pass

    def random_move(self, state, reward):
        if np.random.rand() < 0.6:
            return np.random.choice(['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R'])
        else:
            return np.random.choice(['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C'])

    def move(self, state, reward, selected):

        if state:
            if self.team_id == 1: # Set correct teams based on team id
                self_team = state['team1']
                other_team = state['team2']
            else:
                self_team = state['team2']
                other_team = state['team1']

        if state:
            if selected == self.id and self.pos.dist(state['ball']) < PLAYER_RADIUS + BALL_RADIUS: # Selected player who has the ball
                ai_pass =  self.ai_pass(self_team, other_team)
                if ai_pass != 'NOTHING': # Pass if possible
                    return ai_pass
                else:
                    return self.ai_move_with_ball(other_team, state['misc']['goal_x'][1]) # Move towards the goal

            else: # Move towards the ball if posssbile, otherwise return to formation
                move = self.ai_move_without_ball(state['ball'])
                if move!= 'NOTHING':
                    return move
                else:
                    return 'FORM'
        else:
            return 'NOTHING'
