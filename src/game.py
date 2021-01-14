"""
Contains the central game class

Manages interactions with the players and the ball
"""

from settings import *
from const import ACT
from ball import Ball
from stats import Stats
from camera import Camera
from pygame import mixer
import time


mixer.init(44100, -16, 2, 2048)
applause = mixer.Sound(APPLAUSE)
kick = mixer.Sound(KICK)
single_short_whistle = mixer.Sound(SINGLE_SHORT_WHISTLE)
single_long_whistle = mixer.Sound(SINGLE_LONG_WHISLTE)
three_whistles = mixer.Sound(THREE_WHISTLES)
applause = mixer.Sound(APPLAUSE)


class Game:
    """ Class that controls the entire game """

    def __init__(self, team1, team2, sound=True, difficulty=0.6, cam='default'):
        """
        Initializes the game

        Attributes:
            team1 (Team): Right-facing team
            team2 (Team): Left-facing team
            sound (bool): Enable / Disable in-game sounds
            difficulty (float): Game difficulty (0-1)
        """
        self.sound = sound
        self.difficulty = difficulty
        self.debug = False

        self.team1 = team1
        self.team1.init(id=1, dir='L', diff=self.difficulty)  # direction is hardcoded, don't change

        self.team2 = team2
        self.team2.init(id=2, dir='R', diff=self.difficulty)

        self.ball = Ball(pos=(W//2, H//2), sound=sound)
        self.stats = Stats()

        self.cam = Camera(self.ball.pos.x, self.ball.pos.y, mode=cam)

        self.end = False  # True when the game ends (never probably)
        self.pause = False
        self.state_prev = None
        # game state to be passed to agents (see get_state() function)
        self.state = None
        self.rewards = None

        if self.sound:
            single_short_whistle.play()
            applause.play(-1)

    def check_interruptions(self):
        """
        Check for special keyboard buttons

        Sets internal flags to pause, quit the game or run it in debug mode
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit
                mixer.pause()
                if self.sound:
                    three_whistles.play()
                self.end = True
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:  # Pause menu
                    self.pause = not self.pause
                    if self.pause:
                        mixer.pause()
                        if self.sound:
                            single_long_whistle.play()
                    else:
                        if self.sound:
                            single_short_whistle.play()
                            applause.play(-1)

                if event.key == pygame.K_BACKSPACE:  # Return to main menu
                    mixer.stop()
                    self.end = True

                if event.key == pygame.K_SPACE:  # Toggle whether to maintain formation
                    self.team1.maintain_formation = not self.team1.maintain_formation

                if event.key == pygame.K_d:  # Debug mode
                    mods = pygame.key.get_mods()
                    if mods & pygame.KMOD_CTRL and mods & pygame.KMOD_SHIFT and mods & pygame.KMOD_ALT:
                        self.debug = not self.debug

    def same_team_collision(self, team, free):
        """
        Check if current player collides with any other players of the same team
        """
        min_dist = P(2*PLAYER_RADIUS, 2*PLAYER_RADIUS)
        if not free:
            min_dist.x += BALL_RADIUS

        for player1 in team.players:
            for player2 in team.players:
                if player1.id != player2.id and abs(player1.pos.x - player2.pos.x) <= min_dist.x and abs(player1.pos.y - player2.pos.y) <= min_dist.y:
                    xincr = 1 + PLAYER_RADIUS - \
                        abs(player1.pos.x-player2.pos.x)//2
                    xdir = (1, -1)
                    yincr = 1 + PLAYER_RADIUS - \
                        abs(player1.pos.y-player2.pos.y)//2
                    ydir = (1, -1)

                    if player1.pos.x < player2.pos.x:
                        xdir = (-1, 1)
                    if player1.pos.y < player2.pos.y:
                        ydir = (-1, 1)

                    player1.pos.x += xdir[0]*xincr
                    player2.pos.x += xdir[1]*xincr
                    player1.pos.y += ydir[0]*yincr
                    player2.pos.y += ydir[1]*yincr

    def diff_team_collision(self, team1, team2, free):
        """
        Check if current player collides with any other players of the opposite team
        """
        min_dist = P(2*PLAYER_RADIUS, 2*PLAYER_RADIUS)
        if not free:
            min_dist.x += BALL_RADIUS

        for player1 in team1.players:
            for player2 in team2.players:
                if abs(player1.pos.x - player2.pos.x) <= min_dist.x and abs(player1.pos.y - player2.pos.y) <= min_dist.y:
                    if not free:
                        self.ball.reset(self.ball.pos)
                    xincr = 1 + 2*PLAYER_RADIUS - \
                        abs(player1.pos.x-player2.pos.x)//2
                    xdir = (1, -1)
                    yincr = 1 + 2*PLAYER_RADIUS - \
                        abs(player1.pos.y-player2.pos.y)//2
                    ydir = (1, -1)

                    if player1.pos.x < player2.pos.x:
                        xdir = (-1, 1)
                    if player1.pos.y < player2.pos.y:
                        ydir = (-1, 1)

                    player1.pos.x += xdir[0]*xincr
                    player2.pos.x += xdir[1]*xincr
                    player1.pos.y += ydir[0]*yincr
                    player2.pos.y += ydir[1]*yincr

    def collision(self, team1, team2, ball):
        """
        Handle collisions between all in-game players.
        """
        self.same_team_collision(team1, self.ball.free)
        self.same_team_collision(team2, self.ball.free)
        self.diff_team_collision(team1, team2, self.ball.free)

    def text_draw(self, win, text, rect, align='center'):
        """
        Utility to draw text

        Attributes:
            win (pygame.display): window for rendering
            text (pygame.font (rendered)): The text object
            rect (tuple): Rectangle specified as (x, y, width, height)
            align (string): text alignment can be one of 'left', 'right', 'center' (defaults to 'center')
        """
        width = text.get_width()
        height = text.get_height()
        center_x = round(rect[0] + rect[2]/2)
        center_y = round(rect[1] + rect[3]/2)

        if align == 'left':
            final_rect = (round(rect[0]), round(center_y - height/2))
        elif align == 'right':
            final_rect = (round(rect[0] + rect[2] - width), round(center_y - height/2))
        else:  # Center
            final_rect = (round(center_x - width/2), round(center_y - height/2))
        win.blit(text, final_rect)

    def goal_draw(self, win):
        """
        Display the current score (goals for each side)
        """
        #""" Show game score """
        goal1_rect = (W//2 - GOAL_DISP_SIZE - 2*LINE_WIDTH, 0, GOAL_DISP_SIZE, GOAL_DISP_SIZE)
        goal2_rect = (W//2 + 2*LINE_WIDTH, 0, GOAL_DISP_SIZE, GOAL_DISP_SIZE)
        goal_font = pygame.font.Font(FONT_ROBOTO, FONT_SIZE)

        pygame.draw.rect(win, (255, 255, 255), goal1_rect)
        pygame.draw.rect(win, (255, 255, 255), goal2_rect)
        text = goal_font.render(str(self.stats.goals[1]), True, (0, 0, 0))
        self.text_draw(win, text, goal1_rect)
        text = goal_font.render(str(self.stats.goals[2]), True, (0, 0, 0))
        self.text_draw(win, text, goal2_rect)

    def overlay_draw(self, win):
        scale_rect = lambda x,y,w,h: (OVER_TOP_LEFT.x + x*OVER_SIZE.x//W, OVER_TOP_LEFT.y + y*OVER_SIZE.y//H, w*OVER_SIZE.x//W, h*OVER_SIZE.y//H)
        scale_pt = lambda x,y: (OVER_TOP_LEFT.x + x*OVER_SIZE.x//W, OVER_TOP_LEFT.y + y*OVER_SIZE.y//H)

        r = scale_rect(0,0,W,H)
        s = pygame.Surface((r[2],r[3]), pygame.SRCALPHA)
        s.fill((0,0,0,75))
        win.blit(s, (r[0],r[1]))
        #pygame.draw.rect(win, (0, 136, 3, 100), r)
        pygame.draw.rect(win, (255,255,255), r, LINE_WIDTH)

        pygame.draw.rect(win, (255,255,255),
            scale_rect(self.cam.c.x - self.cam.params['pt'].x//2, self.cam.c.y - self.cam.params['pt'].y//2,
            self.cam.params['pt'].x, self.cam.params['pt'].y), LINE_WIDTH)

        pygame.draw.rect(win, (255, 255, 255), scale_rect(0.95*W-LINE_WIDTH//2,
                                                GOAL_POS[0]*H, 0.05*W, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH)  # right penalty
        pygame.draw.rect(win, (255, 255, 255), scale_rect(LINE_WIDTH//2,
                                                GOAL_POS[0]*H, 0.05*W, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH)  # left penalty

        pygame.draw.rect(win, self.team2.color,scale_rect(W - 3*LINE_WIDTH,
                                                 GOAL_POS[0]*H, 3*LINE_WIDTH, (GOAL_POS[1]-GOAL_POS[0])*H))  # right goal
        pygame.draw.rect(win, self.team1.color,scale_rect(0,
                                                 GOAL_POS[0]*H, 3*LINE_WIDTH, (GOAL_POS[1]-GOAL_POS[0])*H))  # left goal

        pygame.draw.rect(win, (255, 255, 255),
                         scale_rect(W//2 - LINE_WIDTH//2, 0, LINE_WIDTH, H))  # mid line


        for player in self.team1.players:
            pygame.draw.circle(win, self.team1.color, scale_pt(*player.pos.val),
                               PLAYER_RADIUS//4)

        for player in self.team2.players:
            pygame.draw.circle(win, self.team2.color, scale_pt(*player.pos.val),
                               PLAYER_RADIUS//4)

            pygame.draw.circle(win, (42,42,42), scale_pt(*(self.ball.pos + PLAYER_CENTER).val),
                               BALL_RADIUS)

    def field_draw(self, win, hints):
        """
        Draw the football pitch

        Attributes:
            win (pygame.display): window for rendering
            hints (bool): If (movement-based) hints are to be shown
        """
        win.fill((0,0,0))  # constant black
        self.cam.rect(win, (14, 156, 23), (0,0,W,H))  # green ground

        self.cam.rect(win, (255, 255, 255), (0, 0, W -
                                                LINE_WIDTH, H - LINE_WIDTH), LINE_WIDTH)  # border

        self.cam.rect(win, (255, 255, 255),
                         (W//2 - LINE_WIDTH//2, 0, LINE_WIDTH, H))  # mid line
        self.cam.circle(win, (255, 255, 255), (W//2, H//2),
                           H//10, LINE_WIDTH)  # mid circle

        self.cam.rect(win, (255, 255, 255), (0.9*W - LINE_WIDTH //
                                                2, 0.2*H, 0.1*W, 0.6*H), LINE_WIDTH)  # right D
        self.cam.rect(win, (255, 255, 255), (LINE_WIDTH//2,
                                                0.2*H, 0.1*W, 0.6*H), LINE_WIDTH)  # left D

        self.cam.rect(win, (255, 255, 255), (0.95*W-LINE_WIDTH//2,
                                                GOAL_POS[0]*H, 0.05*W, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH)  # right penalty
        self.cam.rect(win, (255, 255, 255), (LINE_WIDTH//2,
                                                GOAL_POS[0]*H, 0.05*W, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH)  # left penalty

        self.cam.rect(win, self.team2.color, (W - 3*LINE_WIDTH,
                                                 GOAL_POS[0]*H, 3*LINE_WIDTH, (GOAL_POS[1]-GOAL_POS[0])*H))  # right goal
        self.cam.rect(win, self.team1.color, (0,
                                                 GOAL_POS[0]*H, 3*LINE_WIDTH, (GOAL_POS[1]-GOAL_POS[0])*H))  # left goal

        if self.cam.mode != 'full':
            self.overlay_draw(win)

        if hints:
            field_font = pygame.font.Font(FONT_ROBOTO, FONT_SIZE//2)
            text_esc = field_font.render('Esc: pause', True, (0, 100, 0))
            text_back = field_font.render(
                'Backspace: return to menu', True, (0, 100, 0))
            text_space = field_font.render(
                'Space: Toggle formation', True, (0, 100, 0))
            text_team1_form = field_font.render(
                f'Maintain formation: {"ON" if self.team1.maintain_formation else "OFF"}', True, (0, 100, 0))

            self.text_draw(win, text_esc, (W - 2*0.1*W - 3*LINE_WIDTH,
                                           3*LINE_WIDTH, 2*0.1*W, 0.05*H), align='right')
            self.text_draw(win, text_space, (W - 3*0.1*W - 3*LINE_WIDTH,
                                             3*LINE_WIDTH, 2*0.1*W, 0.05*H), align='left')
            self.text_draw(win, text_back, (W - 0.2*W - 3*LINE_WIDTH,
                                            3*LINE_WIDTH + 0.05*H, 0.2*W, 0.05*H), align='left')
            self.text_draw(win, text_team1_form, (3*LINE_WIDTH,
                                                  3*LINE_WIDTH, 0.2*W, 0.05*H), align='left')

            if self.debug:
                self.cam.circle(win, (0, 200, 100), (0, H//2),
                                   AI_SHOOT_RADIUS, LINE_WIDTH)  # AI Shoot radius
                self.cam.circle(win, (0, 200, 100), (W, H//2),
                                   AI_SHOOT_RADIUS, LINE_WIDTH)  # AI shoot radius
                text_debug = field_font.render(
                    f'Developer mode: ON', True, (0, 100, 0))
                self.text_draw(win, text_debug, (3*LINE_WIDTH, 3*LINE_WIDTH +
                                                 0.05*H, 0.2*W, 0.05*H), align='left')  # Developer model

    def draw(self, win, hints=True):
        """
        Draw the entire game

        Calls ```field_draw()``` along with the ```draw()``` methods for each team and the ball
        """
        self.field_draw(win, hints=hints)
        if hints:
            self.goal_draw(win)
        self.team1.draw(win, self.cam, debug=self.debug)
        self.team2.draw(win, self.cam, debug=self.debug)
        self.ball.draw(win, self.cam, debug=self.debug)

    def practice_instr_draw(self, win):
        """
        Draw the practice game instructions (shows extra hints and keyboard controls)
        """
        title_font = pygame.font.Font(FONT_ROBOTO, FONT_SIZE)
        title_text = title_font.render('PRACTICE', True, (0, 100, 0))
        self.text_draw(win, title_text, (0, 0, W, 0.01*H))

        field_font = pygame.font.Font(FONT_MONO, FONT_SIZE//2)
        text_shoot1 = field_font.render('       Q W E', True, (0, 100, 0))
        text_shoot2 = field_font.render('Shoot: A   D', True, (0, 100, 0))
        text_shoot3 = field_font.render('       Z X C', True, (0, 100, 0))
        text_move = field_font.render(f'Move: Arrow keys', True, (0, 100, 0))

        self.text_draw(win, text_move, (3*LINE_WIDTH,
                                        3*LINE_WIDTH, 0.2*W, 0.05*H))
        self.text_draw(win, text_shoot1, (3*LINE_WIDTH + 0.2*W, 3 *
                                          LINE_WIDTH, 2*0.1*W + 2*LINE_WIDTH, 0.05*H), align='left')
        self.text_draw(win, text_shoot2, (3*LINE_WIDTH + 0.2*W, 3 *
                                          LINE_WIDTH + 0.05*H, 2*0.1*W + 2*LINE_WIDTH, 0.05*H), align='left')
        self.text_draw(win, text_shoot3, (3*LINE_WIDTH + 0.2*W, 3*LINE_WIDTH +
                                          2*0.05*H, 2*0.1*W + 2*LINE_WIDTH, 0.05*H), align='left')

    def bar_draw(self, win, dim, w0, h0, w, h, col, val, debug_text, invert=False):
        """
        Draw a bar in the pause menu (for statistics)

        Attributes:
            win: Main window used for all drawing
            dim ([int]): extra dimensions for the pause menu
            w0 (int): x coordinate of the bar's top left point
            h0 (int): y coordinate of the bar's top left point
            w (int): width of the bar
            h (int): height of the bar
            col ([int]): color of the bar (RGB tuple)
            val (float): % of the bar to fill (between 0 and 1)
            debug_text (str): Text to display in debug mode
            invert (bool): Flip the bar left to right
        """

        W_, H_, W0, H0, pad, min_len = dim
        inv_col = (255-col[0], 255-col[1], 255-col[2])

        if self.debug:
            text = pygame.font.Font(FONT_ROBOTO, FONT_SIZE//3).render(
                debug_text, True, inv_col)
        else:
            text = pygame.font.Font(
                FONT_ROBOTO, FONT_SIZE//3).render(
                f'{round(100*val)}%', True, inv_col)

        if int(val*w) > min_len:
            if invert:
                pygame.draw.rect(win, col, (round(w0 + w*(1-val)), round(h0),
                                    round(val*w), round(h)))
                self.text_draw(win, text, (round(w0 + w*(1-val)), round(h0),
                                    round(val*w), round(h)))

            else:
                pygame.draw.rect(win, col, (round(w0), round(h0),
                                    round(val*w), round(h)))
                self.text_draw(win, text, (round(w0), round(h0),
                                    round(val*w), round(h)))

        pygame.draw.rect(win, (0, 0, 0), (round(w0), round(h0),
                                round(w), round(h)), LINE_WIDTH)

    def bar_label_draw(self, win, dim, w0, h0, w, h, text):
        """
        Draw the label of a bar in the pause menu (for statistics)

        Attributes:
            win: Main window used for all drawing
            dim ([int]): extra dimensions for the pause menu
            w0 (int): x coordinate of the bar's top left point
            h0 (int): y coordinate of the bar's top left point
            w (int): width of the bar
            h (int): height of the bar
            text (str): Text to display in the label
        """

        W_, H_, W0, H0, pad, min_len = dim

        text_pos = pygame.font.Font(FONT_ROBOTO, FONT_SIZE//2).render(text, True, (255, 255, 255))
        self.text_draw(win, text_pos, (w0, h0, w, h))

    def pause_box_draw(self, win, dim):
        """
        Draw the skeleton of the pause menu (bg, title, exit button)

        Attributes:
            win: Main window used for all drawing
            dim ([int]): extra dimensions for the pause menu
        """

        W_, H_, W0, H0, pad, min_len = dim

        # background and border
        pygame.draw.rect(win, (42, 42, 42), (W0, H0, W_ -
                                             LINE_WIDTH, H_ - LINE_WIDTH))  # border
        # Title
        text_title = pygame.font.Font(FONT_ROBOTO, FONT_SIZE).render(
            "Pause Menu", True, (255, 255, 255))
        self.text_draw(win, text_title, (W0 + pad, H0 +
                                         0.05*H_, W_ - pad, 0.04*H_))

        # Exit button
        text_close1 = pygame.font.Font(
            FONT_ROBOTO, FONT_SIZE).render("x", True, (255, 0, 0))
        text_close2 = pygame.font.Font(
            FONT_ROBOTO, FONT_SIZE//5).render("(ESCAPE)", True, (255, 0, 0))
        self.text_draw(win, text_close1, (W0 + 9*0.1*W_ - pad,
                                          H0 + 0.03*H_, 0.1*W_, 0.05*H))
        self.text_draw(win, text_close2, (W0 + 9*0.1*W_ - pad,
                                          H0 + 0.08*H_, 0.1*W_, 0.05*H))

    def pause_draw(self, win):
        """
        Draw the pause menu

        Displays statistics for possession, pass accuracy and shot accuracy
        """
        W_, H_ = int(0.8*W), int(0.8*H)
        W0, H0 = int(0.1*W), int(0.1*H)

        pad = W_*0.02
        min_len = W_*0.01

        dim = [W_, H_, W0, H0, pad, min_len] # extra dimensions for the pause menu

        self.pause_box_draw(win, dim)

        # Possession
        pos = self.stats.get_possession()

        self.bar_label_draw(win, dim,
            W0, H0 + 0.15*H_, W_, 0.1*H_,
            "POSSESSION")

        self.bar_draw(win, dim, # team 1
            W0 + pad, H0 + 0.25*H_, (W_ - 2*pad)/2, 0.05*H_,
            col=self.team1.color, val=pos[0],
            debug_text=f'{int(round(100*pos[0],0))} ({self.stats.pos[1]})')

        self.bar_draw(win, dim, # team 2
            W0 + W_/2, H0 + 0.25*H_, (W_ - 2*pad)/2, 0.05*H_,
            col=self.team2.color, val=pos[1], invert=True,
            debug_text=f'{int(round(100*pos[1],0))} ({self.stats.pos[2]})')

        # Pass accuracy
        pa = self.stats.get_pass_acc()

        self.bar_label_draw(win, dim,
            W0, H0 + 0.35*H_, W_, 0.1*H_,
            "PASS ACCURACY")

        self.bar_draw(win, dim, # team 1
            W0 + pad, H0 + 0.45*H_, (W_ - 2*pad)/2, 0.05*H_,
            col=self.team1.color, val=pa[0],
            debug_text=f'{int(round(100*pa[0],0))} ({self.stats.pass_acc[1]["succ"]}/{self.stats.pass_acc[1]["succ"]+self.stats.pass_acc[1]["fail"]})')

        self.bar_draw(win, dim, # team 2
            W0 + W_/2, H0 + 0.45*H_, (W_ - 2*pad)/2, 0.05*H_,
            col=self.team2.color, val=pa[1], invert=True,
            debug_text=f'{int(round(100*pa[1],0))} ({self.stats.pass_acc[2]["succ"]}/{self.stats.pass_acc[2]["succ"]+self.stats.pass_acc[2]["fail"]})')

        # Shot accuracy
        sa = self.stats.get_shot_acc()

        self.bar_label_draw(win, dim,
            W0, H0 + 0.55*H_, W_, 0.1*H_,
            "SHOT ACCURACY")

        self.bar_draw(win, dim, # team 1
            W0 + pad, H0 + 0.65*H_, (W_ - 2*pad)/2, 0.05*H_,
            col=self.team1.color, val=sa[0],
            debug_text=f'{int(round(100*sa[1],0))} ({self.stats.shot_acc[2]["succ"]}/{self.stats.shot_acc[2]["succ"]+self.stats.shot_acc[2]["fail"]})')

        self.bar_draw(win, dim, # team 2
            W0 + W_/2, H0 + 0.65*H_, (W_ - 2*pad)/2, 0.05*H_,
            col=self.team2.color, val=sa[1], invert=True,
            debug_text=f'{int(round(100*sa[1],0))} ({self.stats.shot_acc[2]["succ"]}/{self.stats.shot_acc[2]["succ"]+self.stats.shot_acc[2]["fail"]})')

    def get_state(self):
        """
        Create a state object that summarizes the entire game

        ```
        state = {
            'team1': {
                'players' # list of the team player's coordinates
                'goal_x' # The x-coordinate of their goal post
            },
            'team2': {
                'players' # list of the team player's coordinates
                'goal_x' # The x-coordinate of their goal post
            },
            'ball' # Position of the ball
        }
        ```
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
                'goal_x': self.team2.goal_x,
            },
            'ball': self.ball,
        }

    def next(self):
        """
        Move the game forward by 1 frame

        Passes state objects to the teams and pass their actions to ```move_next()```
        """
        a1 = self.team1.move(self.state_prev, self.state, self.rewards)
        a2 = self.team2.move(self.state_prev, self.state, self.rewards)
        self.state_prev, self.state, self.rewards = self.move_next(a1, a2)

    def move_next(self, a1, a2):
        """
        Update the players' and ball's internal state based on the teams' actions

        Attributes:
            a1 (list): list of actions (1 for each player) in team 1
            a2 (list): list of actions (1 for each player) in team 2

        Each action must be a key in the ```ACT``` dictionary found in ```const.py```
        """

        state_prev = self.get_state()

        self.team1.update(a1, self.ball)  # Update team's state
        self.team2.update(a2, self.ball)

        # Check for collision between players
        self.collision(self.team1, self.team2, self.ball)

        self.ball.update(self.team1, self.team2, a1, a2,
                         self.stats)  # Update ball's state

        self.cam.move(self.ball.pos.x, self.ball.pos.y)

        state = self.get_state()
        return state_prev, state, 0
