from settings import *
from const import ACT, FORM
from teams.agent import Agent
from teams.team import Team

class OriginalAIAgent(Agent):
    """ Agents that play like the original AI """

    def draw(self, win, team_id, debug=False):
        if debug:
            pygame.draw.circle(win, (0, 100, 0), (self.pos-PLAYER_CENTER).val, AI_NEAR_RADIUS, LINE_WIDTH)
            pygame.draw.circle(win, (0, 200, 0), (self.pos-PLAYER_CENTER).val, AI_FAR_RADIUS, LINE_WIDTH)

        super().draw(win, team_id, debug=debug)

    def dist_to_line(self, line, pt):
        """
        distance of
            line: x*line[0] + y*line[1] + line[2] = 0
            from point: p
        """
        return abs(line[0]*pt.x + line[1]*pt.y + line[2])/math.sqrt(line[0]**2 + line[1]**2)

    def ai_move_with_ball(self, enemy_players, goal_x):
        """
        If this player has the ball
        Calculate vectors towards the goal and away from nearby players of the opposite team
        Add up all these vectors and move in that direction (probabilistically)
        enemy_players: positions of all of the enemy team
        goal_x: x-coordinate of enemy goal
        """

        player_vec = P(0,0) # Direction vector to move due to opposite team
        for player in enemy_players:
            if self.pos.dist(player.pos) < AI_NEAR_RADIUS:
                dir = player.pos - self.pos
                mag = (AI_NEAR_RADIUS*PLAYER_RADIUS/dir.mag)**2 # magnitude of vector is proportional to inverse of distance
                player_vec -= P(mag/dir.mag,mag/dir.mag)*dir

        goal_vec = P(goal_x, H//2) - self.pos # Direction vector to move due to goal
        goal_vec *= P(1/goal_vec.mag, 1/goal_vec.mag) # O

        final_vec = goal_vec + player_vec # Final vector is sum

        dir_final = final_vec * P(1/final_vec.mag, 1/final_vec.mag)

        possible_dir = ['NOTHING', 'MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']
        dist_to_dir = [dir_final.dist(ACT[dir]) for dir in possible_dir]
        prob_dist = [math.exp(1/d) if d >= 0.1 else math.exp(10) for d in dist_to_dir]
        chosen_dir = random.choices(possible_dir, weights=[prob/sum(prob_dist) for prob in prob_dist])[0]

        return chosen_dir

    def ai_move_without_ball(self, ball):
        """
        Move towards the ball if it is nearby
        Moves probabilistically
        """
        if self.pos.dist(ball.pos) < AI_FAR_RADIUS:
            vec = ball.pos - self.pos
            vec_dir = P(1/vec.mag,1/vec.mag)*vec

            possible_dir = ['MOVE_U', 'MOVE_D', 'MOVE_L', 'MOVE_R']
            dist_to_dir = [vec_dir.dist(ACT[dir]) for dir in possible_dir]
            prob_dist = [math.exp(1/d) if d >= 0.1 else math.exp(10) for d in dist_to_dir]
            chosen_dir = random.choices(possible_dir, weights=[prob/sum(prob_dist) for prob in prob_dist])[0]
            return chosen_dir
        else:
            return 'NOTHING'

    def ai_pass(self, team_players, enemy_team_players):
        """
        Pass the ball such that the perpendicular distance to the pass line is less than
        AI_MIN_PASS_DIST and no enemy is nearer than a team player in that direction

        Note:   The origin is at top-left instead of the standard bottom-left
                so, map y -> H-y
        """

        # Invert coordinates
        team_pos = {player.id: P(player.pos.x, H-player.pos.y) for player in team_players}
        enemy_team_pos = {player.id: P(player.pos.x, H-player.pos.y) for player in enemy_team_players}
        self_pos  = P(self.pos.x, H-self.pos.y)

        prefs  = { # directions are wrt origin at bottom-right
            'SHOOT_A': {'priority': {1: 4, 2: 1}, 'angle': math.pi, 'dir': P(-1,0)},
            'SHOOT_Q': {'priority': {1: 3, 2: 1}, 'angle': math.pi*3/4, 'dir': P(-1,1)},
            'SHOOT_Z': {'priority': {1: 3, 2: 1}, 'angle': -math.pi*3/4, 'dir': P(-1,-1)},
            'SHOOT_W': {'priority': {1: 2, 2: 2}, 'angle': math.pi/2, 'dir': P(0,1)},
            'SHOOT_X': {'priority': {1: 2, 2: 2}, 'angle': -math.pi/2, 'dir': P(0,-1)},
            'SHOOT_E': {'priority': {1: 1, 2: 3}, 'angle': math.pi/4, 'dir': P(1,1)},
            'SHOOT_C': {'priority': {1: 1, 2: 3}, 'angle': -math.pi/4, 'dir': P(1,-1)},
            'SHOOT_D': {'priority': {1: 1, 2: 4}, 'angle': 0, 'dir': P(1,0)},
        }

        possible_passes  = []

        for k,v in prefs.items():
            line = [ # Equation of line as A*x +B*y + C = 0
                    math.sin(v['angle']), # x coeff
                    -math.cos(v['angle']), # y coeff
                    self_pos.y*math.cos(v['angle']) - self_pos.x*math.sin(v['angle']), # constant
            ]
            for player in team_players:
                if player.id != self.id:
                    team_dist = self.dist_to_line(line, team_pos[player.id])
                    if  (team_dist < AI_MIN_PASS_DIST and # player is near enough to receive the ball
                         (self_pos.x - team_pos[player.id].x)*v['dir'].x <= 0 and # In correct x-direction (not behind the line)
                         (self_pos.y - team_pos[player.id].y)*v['dir'].y <= 0): # In correct y-direction

                        # Consider enemy's distance as well
                        enemy_dist = math.inf
                        enemy_min_pos = P(0,0)
                        for enemy_player in enemy_team_players: # Check for all enemies
                            if self.dist_to_line(line, enemy_team_pos[enemy_player.id]) < enemy_dist:
                                enemy_dist = self.dist_to_line(line, enemy_team_pos[enemy_player.id])
                                enemy_min_pos = enemy_team_pos[enemy_player.id]

                        if  (enemy_dist < team_dist and # enemy is nearer than team player
                            (self.pos.x - enemy_min_pos.x)*v['dir'].x <= 0 and # In correct x-direction (not behind the line)
                            (self.pos.y - enemy_min_pos.y)*v['dir'].y <= 0): # In correct y-direction
                            continue
                        else:
                            possible_passes.append(
                                (v['priority'][self.team_id],
                                team_dist,
                                k,
                                enemy_dist
                                )
                            )

        # Sort by priority then distance
        if possible_passes != []:
            ai_pass = sorted(possible_passes)[0][2]
        else:
            ai_pass = 'NOTHING'

        return ai_pass

    def ai_shoot(self, gk, goal_x):
        """
        Shoot the ball
        Only shoots if within AI_SHOOT_RADIUS of goal
        Shoots to maximize distance between keeper and shot while keeping the shot within goal boundaries
        gk_pos: Goal keeper of the enemy team
        goal_x: X coordinate of goal post
        """
        angles  = {
            1: { # For team 1
                'SHOOT_E': math.pi/4,
                'SHOOT_D': 0,
                'SHOOT_C': -math.pi/4,
            },
            2: { # For team 2
                'SHOOT_Q': math.pi*3/4,
                'SHOOT_A': math.pi,
                'SHOOT_Z': -math.pi*5/4,
            },
        }

        self_pos  = P(self.pos.x, H-self.pos.y)
        gk_pos  = P(gk.pos.x, H-gk.pos.y)

        possible_shots = []
        for k,v in angles[self.team_id].items():
            line = [ # Equation of line as A*x +B*y + C = 0
                    math.sin(v), # x coeff
                    -math.cos(v), # y coeff
                    self_pos.y*math.cos(v) - self_pos.x*math.sin(v), # constant
            ]
            intersection_pt = -(line[2] + line[0]*goal_x)/line[1]
            if GOAL_POS[0]*H < intersection_pt < GOAL_POS[1]*H:
                possible_shots.append((-self.dist_to_line(line, gk_pos), k))

        if possible_shots:
            shot = sorted(possible_shots)[0][1]
        else:
            shot = 'NOTHING'

        return shot


    def gk_move(self, goal_x, ball):
        """
        Move towards the ball and stay within the goal's limits
        """
        if ball.pos.dist(P(goal_x,H//2)) < AI_SHOOT_RADIUS:
            if abs(self.pos.x - goal_x) > BALL_RADIUS + PLAYER_RADIUS: # Goal keeper does not go into the goal himself
                if ball.pos.y == self.pos.y: # Do nothing if ball is directly in your path
                    return 'NOTHING'
                elif PLAYER_RADIUS and GOAL_POS[0]*H < self.pos.y < GOAL_POS[1]*H:
                    if ball.pos.y - self.pos.y >= 0:
                        return 'MOVE_D'
                    else:
                        return 'MOVE_U'
                else:
                    return 'FORM' # IMM_PASS
        else:
            return 'FORM'

    def gk_pass(self, enemy_players, goal_x):
        """
        Pass such that enemy players in AI_SHOOT_RADIUS do not get the ball
        goal_x: Self team's goal position
        """

        angles  = {
            1: { # For team 1
                'SHOOT_E': math.pi/4,
                'SHOOT_D': 0,
                'SHOOT_C': -math.pi/4,
            },
            2: { # For team 2
                'SHOOT_Q': math.pi*3/4,
                'SHOOT_A': math.pi,
                'SHOOT_Z': -math.pi*5/4,
            },
        }

        self_pos  = P(self.pos.x, H-self.pos.y)
        near_enemy_players = [player for player in enemy_players if player.pos.dist(P(goal_x,H//2)) <= AI_SHOOT_RADIUS]
        near_enemy_pos  = [P(player.pos.x, H - player.pos.y) for player in near_enemy_players]

        possible_passes = []
        for k,v in angles[self.team_id].items():
            line = [ # Equation of line as A*x +B*y + C = 0
                    math.sin(v), # x coeff
                    -math.cos(v), # y coeff
                    self_pos.y*math.cos(v) - self_pos.x*math.sin(v), # constant
            ]
            if near_enemy_pos:
                dist = math.inf
                dir = 'NOTHING'
                dist = min([self.dist_to_line(line, pos) for pos in near_enemy_pos])
                possible_passes.append((-dist,k))

        if possible_passes:
            shot = sorted(possible_passes)[0][1]
        else:
            shot = 'NOTHING'

        return shot

    def move(self, state_prev, state, reward, selected):
        if state:
            if self.team_id == 1: # Set correct teams based on team id
                self_team = state['team1']
                other_team = state['team2']
            else:
                self_team = state['team2']
                other_team = state['team1']

        if state:
            if self.id == 0: # Special for the goal-keeper
                ai_gk_pass = self.gk_pass(other_team['players'], self_team['goal_x'])
                ai_gk_move = self.gk_move(self_team['goal_x'], state['ball'])
                if selected == self.id and state['ball'].ball_stats['player'] == self.id: # GK has the ball
                    if ai_gk_pass != 'NOTHING':
                        return ai_gk_pass
                    else:
                        return ai_gk_move
                else:
                    return ai_gk_move

            if selected == self.id and state['ball'].ball_stats['player'] == self.id: # Selected player has the ball
                ai_shoot = self.ai_shoot(other_team['players'][0], other_team['goal_x'])
                ai_pass =  self.ai_pass(self_team['players'], other_team['players'])
                if self.pos.dist(P(other_team['goal_x'],H//2)) <= AI_SHOOT_RADIUS and ai_shoot != 'NOTHING': # If shot is possible, take it
                    return ai_shoot
                elif ai_pass != 'NOTHING' and random.random() >= AI_PASS_PROB: # Else, pass if possible (passes towards the enemy goal are prioritized)
                    return ai_pass
                else:
                    return self.ai_move_with_ball(other_team['players'], other_team['goal_x']) # Move towards the goal

            else: # Move towards the ball if posssbile, otherwise return to formation
                move = self.ai_move_without_ball(state['ball'])
                if move != 'NOTHING':
                    return move
                else:
                    return 'FORM' # Special action, not defined in ACT
        else:
            return 'NOTHING' # Otherwise do nothing

class OriginalAITeam(Team):
    """The AI team used in the original (C++) version"""
    def set_players(self):
        self.players = []
        for i in range(NUM_TEAM):
            self.players.append(OriginalAIAgent(id=i, team_id=self.id, pos=FORM[self.formation][self.dir][i]['coord']))

    def select_player(self, ball):
        """
        Select the player that is controlled by the keyboard
            - If ball is near the D-area, keeper gets automatic control
            - Otherwise the player nearest to the ball has control (ties are broken randomly)
        """
        dists = [player.pos.dist(ball.pos) + player.rnd for player in self.players]
        self.selected = dists.index(min(dists)) # Default - Ball goes to nearest player

        if min(dists) > PLAYER_RADIUS + BALL_RADIUS and abs(ball.pos.x - self.goal_x) < W//5:
            # If the ball is within the D and is not very near to any other player, give control to the keeper
            self.selected = 0

    def formation_dir(self, id):
        """ Send player with given id to his designated place in the formation """
        player = self.players[id]
        min_dist = 2

        """
        If player is in-line (horizontally or vertically), move directly towards original point (U/L/D/R)
        Otherwise choose 2 directions that take you closer to the original point and choose one of them randomly (UL/UR/DL/DR)
        """
        if abs(player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) <= min_dist and abs(player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) <= min_dist:
            player.walk_count = 0
            return 'NOTHING'
        elif abs(player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) <= min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) > min_dist:
                return 'MOVE_U'
            else:
                return 'MOVE_D'
        elif abs(player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) <= min_dist:
            if (player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) > min_dist:
                return 'MOVE_L'
            else:
                return 'MOVE_R'
        elif (player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) > min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) > min_dist:
                return random.choices(['MOVE_L', 'MOVE_U'])[0]
            else:
                return random.choices(['MOVE_L', 'MOVE_D'])[0]
        elif (player.pos.x - FORM[self.formation][self.dir][id]['coord'].x) < - min_dist:
            if (player.pos.y - FORM[self.formation][self.dir][id]['coord'].y) > min_dist:
                return random.choices(['MOVE_R', 'MOVE_U'])[0]
            else:
                return random.choices(['MOVE_R', 'MOVE_D'])[0]
        else:
            return 'NOTHING'

    def move(self, state_prev, state, reward):
        """ Move each player """
        actions = []
        if state:
            self.select_player(state['ball'])
        else:
            self.selected = NUM_TEAM//2
        for i,player in enumerate(self.players):
            move = player.move(state_prev, state, reward,self.selected)
            if move != 'FORM':
                actions.append(move)
            else:
                actions.append(self.formation_dir(i))
        return actions
