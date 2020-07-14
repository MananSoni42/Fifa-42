from settings import *
from const import ACT
from ball import Ball
from stats import Stats

class Game:
    """ Class that controls the entire game """
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team1.init(id=1, dir='L') # direction is hardcoded, don't change

        self.team2 = team2
        self.team2.init(id=2, dir='R')

        self.ball = Ball(pos=(W//2, H//2))
        self.stats = Stats()

        self.end = False # True when the game ends (never probably)
        self.pause = False
        self.state = None # game state to be passed to agents (see get_state() function)
        self.rewards = None

    def check_interruptions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Quit
                self.end = True

        keys = pygame.key.get_pressed() # Pause
        if keys[pygame.K_ESCAPE]:
            self.pause = True
        elif keys[pygame.K_BACKSPACE]:
            self.pause = False
        if keys[pygame.K_SPACE]:
            self.team1.maintain_formation = not self.team1.maintain_formation
            self.team2.maintain_formation = not self.team2.maintain_formation

    def same_team_collision(self, team, actions, free):
        """ Check if current player collides with any other players (same team) """
        min_dist  = P(2*PLAYER_RADIUS, 2*PLAYER_RADIUS)
        if not free:
            min_dist.x += BALL_RADIUS

        for player1 in team.players:
            for player2 in team.players:
                if player1.id != player2.id and abs(player1.pos.x - player2.pos.x) <= min_dist.x and abs(player1.pos.y - player2.pos.y) <= min_dist.y:
                    player1.pos -= P(PLAYER_SPEED, PLAYER_SPEED)*P(ACT[actions[player1.id]])
                    player2.pos -= P(PLAYER_SPEED, PLAYER_SPEED)*P(ACT[actions[player2.id]])

    def diff_team_collision(self, team1, team2, free):
        """ Check if current player collides with any other players (different teams) """
        min_dist  = P(2*PLAYER_RADIUS, 2*PLAYER_RADIUS)
        if not free:
            min_dist.x += BALL_RADIUS

        for player1 in team1.players:
            for player2 in team2.players:
                if abs(player1.pos.x - player2.pos.x) <= min_dist.x and abs(player1.pos.y - player2.pos.y) <= min_dist.y:
                    if not free:
                        self.ball.reset(self.ball.pos)
                    xincr = 1 + 2*PLAYER_RADIUS - abs(player1.pos.x-player2.pos.x)//2
                    xdir = (1,-1)
                    yincr = 1 + 2*PLAYER_RADIUS - abs(player1.pos.y-player2.pos.y)//2
                    ydir = (1,-1)

                    if player1.pos.x < player2.pos.x:
                        xdir = (-1,1)
                    if player1.pos.y < player2.pos.y:
                        ydir = (-1,1)

                    player1.pos.x += xdir[0]*xincr
                    player2.pos.x += xdir[1]*xincr
                    player1.pos.y += ydir[0]*yincr
                    player2.pos.y += ydir[1]*yincr

    def collision(self, team1, act1, team2, act2, ball):
        self.same_team_collision(team1, act1, self.ball.free)
        self.same_team_collision(team2, act2, self.ball.free)
        self.diff_team_collision(team1, team2, self.ball.free)

    def text_draw(self, win, text, rect):
        center_x = rect[0] + rect[2]//2
        center_y = rect[1] + rect[3]//2
        width = text.get_width()
        height = text.get_height()
        win.blit(text, (center_x - width//2, center_y - height//2))

    def goal_draw(self,win):
        """ Show game score """
        goal1_rect = (W//2 - GOAL_DISP_SIZE - 2*LINE_WIDTH, 0, GOAL_DISP_SIZE, GOAL_DISP_SIZE)
        goal2_rect = (W//2 + 2*LINE_WIDTH, 0, GOAL_DISP_SIZE, GOAL_DISP_SIZE)
        goal_font = pygame.font.Font(FONT_PATH, FONT_SIZE)

        pygame.draw.rect(win, (255, 255, 255), goal1_rect)
        pygame.draw.rect(win, (255, 255, 255), goal2_rect)
        text = goal_font.render(str(self.stats.goals[1]), True, (0,0,0))
        self.text_draw(win, text, goal1_rect)
        text = goal_font.render(str(self.stats.goals[2]), True, (0,0,0))
        self.text_draw(win, text, goal2_rect)

    def field_draw(self,win):
        """ Draw the football pitch """
        win.fill((14, 156, 23)) # constant green

        pygame.draw.rect(win, (255, 255, 255), (0, 0, W - LINE_WIDTH, H - LINE_WIDTH), LINE_WIDTH) # border

        pygame.draw.rect(win, (255, 255, 255), (W//2 - LINE_WIDTH//2, 0, LINE_WIDTH, H)) # mid line
        pygame.draw.circle(win, (255, 255, 255), (W//2, H//2), H//5, LINE_WIDTH) # mid circle

        pygame.draw.rect(win, (255, 255, 255), (4*W//5-LINE_WIDTH//2, 0.1*H, W//5, 0.8*H), LINE_WIDTH) # right D
        pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2, 0.1*H, W//5, 0.8*H), LINE_WIDTH) # left D

        pygame.draw.rect(win, (255, 255, 255), (19*W//20-LINE_WIDTH//2, GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH) # right goal
        pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2, GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH) # right goal

    def draw(self, win, debug=False):
        """ Draw the game """
        self.field_draw(win)
        if debug:
            pygame.draw.circle(win, (64, 128, 255), (0, H//2), AI_SHOOT_RADIUS, LINE_WIDTH) # mid circle
            pygame.draw.circle(win, (64, 128, 255), (W, H//2), AI_SHOOT_RADIUS, LINE_WIDTH) # mid circle
        self.goal_draw(win)
        self.team1.draw(win, debug=debug)
        self.team2.draw(win, debug=debug)
        self.ball.draw(win, debug=debug)

    def pause_draw(self,win):
        """ Draw the pause menu """
        W_,H_ = int(0.8*W), int(0.8*H)
        W0,H0 = int(0.1*W), int(0.1*H)
        # background and border
        #win.fill((42, 42, 42)) # Gray
        pygame.draw.rect(win, (42, 42, 42), (W0, H0, W_ - LINE_WIDTH, H_ - LINE_WIDTH)) # border
        pad = LINE_WIDTH*2
        min_len = 10

        # Exit
        text1 = pygame.font.Font(FONT_PATH, FONT_SIZE).render("x", True, (255,0,0))
        text2 = pygame.font.Font(FONT_PATH, FONT_SIZE//5).render("(Backspace)", True, (255,0,0))
        self.text_draw(win, text1, (W0 + pad, H0 + (3*H_)//100, W_//10, (5*H_)//100))
        self.text_draw(win, text2, (W0 + pad, H0 + (8*H_)//100, W_//10, (5*H_)//100))

        # Possession
        text_pos = pygame.font.Font(FONT_PATH, FONT_SIZE//2).render("POSSESSION", True, (255,255,255))
        self.text_draw(win, text_pos, (W0, H0 + (15*H_)//100, W_, (10*H_)//100))

        pos = self.stats.get_possession()
        text1 = pygame.font.Font(FONT_PATH, FONT_SIZE//5).render(str(round(100*pos[0],2))+"%", True, (255,255,255))
        text2 = pygame.font.Font(FONT_PATH, FONT_SIZE//5).render(str(round(100*pos[1],2))+"%", True, (255,255,255))

        if int(pos[0]*W_) - 2*pad > min_len: # Team 1
            pygame.draw.rect(win, self.team1.color, (W0 + pad, H0 + (25*H_)//100, int(pos[0]*W_) - 3*pad, (5*H_)//100))
            self.text_draw(win, text1, (W0 + pad, H0 + (25*H_)//100, int(pos[0]*W_) - 3*pad, (5*H_)//100))

        if int(pos[1]*W_) - pad > min_len: # Team 2
            pygame.draw.rect(win, self.team2.color, (W0 + int(pos[0]*W_) - 2*pad, H0 + (25*H_)//100, int(pos[1]*W_), (5*H_)//100))
            self.text_draw(win, text2, (W0 + int(pos[0]*W_) - 2*pad, H0 + (25*H_)//100, int(pos[1]*W_), (5*H_)//100))

        pygame.draw.rect(win, (0,0,0), (W0 + pad, H0 + (25*H_)//100, W_ - 3*pad, (5*H_)//100), LINE_WIDTH) # border

        # Pass accuracy
        text_pos = pygame.font.Font(FONT_PATH, FONT_SIZE//2).render("Pass Accuracy", True, (255,255,255))
        self.text_draw(win, text_pos, (W0, H0 + (35*H_)//100, W_, (10*H_)//100))

        pa = self.stats.get_pass_acc()
        text1 = pygame.font.Font(FONT_PATH, FONT_SIZE//5).render(str(round(100*pa[0],2))+"%", True, (255,255,255))
        text2 = pygame.font.Font(FONT_PATH, FONT_SIZE//5).render(str(round(100*pa[1],2))+"%", True, (255,255,255))

        if int(pa[0]*W_//2) > min_len: # team 1
            pygame.draw.rect(win, self.team1.color, (W0 + pad, H0 + (45*H_)//100, int(pa[0]*W_//2) - pad, (5*H_)//100))
            self.text_draw(win, text1, (W0 + pad, H0 + (45*H_)//100, int(pa[0]*W_//2) - pad, (5*H_)//100))

        if int(pa[1]*W_//2) - pad > min_len: # team 2
            pygame.draw.rect(win, self.team2.color, (W0 + W_ - pad - int(pa[1]*W_//2), H0 + (45*H_)//100, int(pa[1]*W_//2) - pad, (5*H_)//100))
            self.text_draw(win, text2, (W0 + W_ - pad - int(pa[1]*W_//2), H0 + (45*H_)//100, int(pa[1]*W_//2) - pad, (5*H_)//100))

        pygame.draw.rect(win, (0,0,0), (W0 + pad, H0 + (45*H_)//100, W_ - 3*pad, (5*H_)//100), LINE_WIDTH) # border
        pygame.draw.rect(win, (0,0,0), (W0 + W_//2 - LINE_WIDTH//2, H0 + (45*H_)//100, LINE_WIDTH, (5*H_)//100)) # center line

        # Shot accuracy
        text_pos = pygame.font.Font(FONT_PATH, FONT_SIZE//2).render("Shot Accuracy", True, (255,255,255))
        self.text_draw(win, text_pos, (W0, H0 + (55*H_)//100, W_, (10*H_)//100))

        sa = self.stats.get_shot_acc()
        text1 = pygame.font.Font(FONT_PATH, FONT_SIZE//5).render(str(round(100*sa[0],2))+"%", True, (255,255,255))
        text2 = pygame.font.Font(FONT_PATH, FONT_SIZE//5).render(str(round(100*sa[1],2))+"%", True, (255,255,255))

        if int(sa[0]*W_//2) > min_len: # team 1
            pygame.draw.rect(win, self.team1.color, (W0 + pad, H0 + (65*H_)//100, int(sa[0]*W_//2) - pad, (5*H_)//100))
            self.text_draw(win, text1, (W0 + pad, H0 + (65*H_)//100, int(sa[0]*W_//2) - pad, (5*H_)//100))

        if int(sa[1]*W_//2) - 2*pad > min_len: # team 2
            pygame.draw.rect(win, self.team2.color, (W0 + W_ - int(sa[1]*W_//2), H0 + (65*H_)//100, int(sa[1]*W_//2) - 2*pad, (5*H_)//100))
            self.text_draw(win, text2, (W0 + W_ - int(sa[1]*W_//2), H0 + (65*H_)//100, int(sa[1]*W_//2) - 2*pad, (5*H_)//100))

        pygame.draw.rect(win, (0,0,0), (W0 + pad, H0 + (65*H_)//100, W_ - 3*pad, (5*H_)//100), LINE_WIDTH) # border
        pygame.draw.rect(win, (0,0,0), (W0 + W_//2 - LINE_WIDTH//2, H0 + (65*H_)//100, LINE_WIDTH, (5*H_)//100)) # center line

    def get_state(self):
        """
        The state object: a summary of the entire game as seen by the agent
        """
        pos1 = [player.pos for player in self.team1.players]
        pos2 = [player.pos for player in self.team2.players]
        return {
            'team1': {
                'players': self.team1.players,
                'goal_x': self.team1.goal_x,
            },
            'team2': {
                'players': self.team2.players,
                'goal_x': self.team1.goal_x,
            },
            'ball': self.ball,
        }

    def next(self):
        a1 = self.team1.move(self.state, self.rewards)
        a2 = self.team2.move(self.state, self.rewards)
        self.state, self.rewards = self.move_next(a1,a2)

    def move_next(self, a1, a2):
        """
        Next loop that is the heart of the game
         - a1,a2 (list): Actions of each player in respective teams
        """
        self.team1.update(a1, self.ball) # Update team's state
        self.team2.update(a2, self.ball)

        self.collision(self.team1, a1, self.team2, a2, self.ball) # Check for collision between players

        self.ball.update(self.team1, self.team2, a1, a2, self.stats) # Update ball's state

        return self.get_state(), 0
