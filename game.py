from settings import *
from const import ACT, GOALS
from ball import Ball

class Game:
    """ Class that controls the entire game """
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team1.init(id=1, dir='L') # direction is hardcoded, don't change

        self.team2 = team2
        self.team2.init(id=2, dir='R')

        self.ball = Ball(pos=(W//2, H//2))
        self.end = False # True when the game ends (never probably)

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
        text = goal_font.render(str(GOALS[1]), True, (0,0,0))
        self.text_draw(win, text, goal1_rect)
        text = goal_font.render(str(GOALS[2]), True, (0,0,0))
        self.text_draw(win, text, goal2_rect)

    def field_draw(self,win):
        """ Draw the football pitch """
        #win.blit(BACKGROUND_IMG, (0, 0)) # grass
        win.fill((14, 156, 23)) # constant green

        pygame.draw.rect(win, (255, 255, 255), (0, 0, W, LINE_WIDTH//2)) # border
        pygame.draw.rect(win, (255, 255, 255), (0, H-LINE_WIDTH//2, W, LINE_WIDTH//2)) # border
        pygame.draw.rect(win, (255, 255, 255), (0, 0, LINE_WIDTH//2, H)) # border
        pygame.draw.rect(win, (255, 255, 255), (W-LINE_WIDTH//2, 0, LINE_WIDTH//2, H)) # border

        pygame.draw.rect(win, (255, 255, 255), (W//2 - LINE_WIDTH//2, 0, LINE_WIDTH, H)) # mid line
        pygame.draw.circle(win, (255, 255, 255), (W//2, H//2), H//5, LINE_WIDTH) # mid circle

        pygame.draw.rect(win, (255, 255, 255), (4*W//5-LINE_WIDTH//2, 0.1*H, W//5, 0.8*H), LINE_WIDTH) # right D
        pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2, 0.1*H, W//5, 0.8*H), LINE_WIDTH) # left D

        pygame.draw.rect(win, (255, 255, 255), (19*W//20-LINE_WIDTH//2, GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH) # right goal
        pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2, GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH) # right goal

    def draw(self, win, debug=False):
        """ Draw everything """
        self.field_draw(win)
        self.goal_draw(win)
        self.team1.draw(win, debug=debug)
        self.team2.draw(win, debug=debug)
        self.ball.draw(win, debug=debug)


    def next(self, a1, a2):
        """
        Next loop that is the heart of the game
         - a1,a2 (list): Actions of each player in respective teams
        """
        self.team1.update(a1, self.ball) # Update team's state
        self.team2.update(a2, self.ball)

        self.collision(self.team1, a1, self.team2, a2, self.ball) # Check for collision between players

        self.ball.update(self.team1, self.team2, a1, a2) # Update ball's state
        self.ball.goal_check() # Check if a goal is scoread
        return 0,0
