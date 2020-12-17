from settings import *
from const import ACT, GOALS
from ball import Ball
from math import sin,cos,pi

class Game:
    """ Class that controls the entire game """
    def __init__(self, team_human, team_ai):
        self.team_human = team_human
        self.team_ai = team_ai
        self.ball = Ball(pos=(W/2, H/2))
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
                    xincr = 1 + 2*PLAYER_RADIUS - abs(player1.pos.x-player2.pos.x)/2
                    xdir = (1,-1)
                    yincr = 1 + 2*PLAYER_RADIUS - abs(player1.pos.y-player2.pos.y)/2
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
        # Special case when ball is not free
        self.same_team_collision(team1, act1, self.ball.free)
        self.same_team_collision(team2, act2, self.ball.free)
        self.diff_team_collision(team1, team2, self.ball.free)

    def text_draw(self, win, text, rect):
        center_x = rect[0] + rect[2]/2
        center_y = rect[1] + rect[3]/2
        width = text.get_width()
        height = text.get_height()
        win.blit(text, (center_x - width/2, center_y - height/2))

    def goal_draw(self,win):
        """ Show game score """
        goal1_rect = (W/2 - GOAL_DISP_SIZE - 2*LINE_WIDTH, 0, GOAL_DISP_SIZE, GOAL_DISP_SIZE)
        goal2_rect = (W/2 + 2*LINE_WIDTH, 0, GOAL_DISP_SIZE, GOAL_DISP_SIZE)
        goal_font = pygame.font.Font(FONT_PATH, FONT_SIZE)

        pygame.draw.rect(win, (255, 255, 255), goal1_rect)
        pygame.draw.rect(win, (255, 255, 255), goal2_rect)
        text = goal_font.render(str(GOALS[1]), True, (0,0,0))
        self.text_draw(win, text, goal1_rect)
        text = goal_font.render(str(GOALS[2]), True, (0,0,0))
        self.text_draw(win, text, goal2_rect)

    def line_draw(self, p1, p2):
        glBegin(GL_LINES)
        glVertex3f(p1.x/SCALE, GY + .1, p1.y/SCALE)
        glVertex3f(p2.x/SCALE, GY + .1, p2.y/SCALE)
        glEnd();

    def rect_draw(self, p, len, h, fill=False):
        x,y,z = p.x/SCALE, GY + h/SCALE/2 + 2 ,p.y/SCALE
        tx,ty,tz = (len.x/SCALE/2, h/SCALE, len.y/SCALE/2)
        cubeVertices = ((x+tx,y+ty,z+tz),(x+tx,y+ty,z-tz),(x+tx,y-ty,z-tz),(x+tx,y-ty,z+tz),(x-tx,y+ty,z+tz),(x-tx,y-ty,z-tz),(x-tx,y-ty,z+tz),(x-tx,y+ty,z-tz))
        cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
        cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))
        if fill:
            glBegin(GL_QUADS)
        else:
            glBegin(GL_LINES)
        for cubeEdge in cubeEdges:
            for cubeVertex in cubeEdge:
                glVertex3fv(cubeVertices[cubeVertex])
        glEnd()

    def circle_draw(self, p, radius):
        sides = 100
        radius = radius/SCALE
        glBegin(GL_LINE_LOOP)
        for i in range(sides):
            cosine = radius * cos(i*2*pi/sides) + p.x/SCALE
            sine   = radius * sin(i*2*pi/sides) + p.y/SCALE
            glVertex3f(cosine, GY+.1, sine)
        glEnd()

    def field_draw(self,win):
        # Draw the football pitch
        #win.blit(BACKGROUND_IMG, (0, 0)) # grass
        #win.fill((14, 156, 23)) # constant green
        self.ground_draw(win)

        glColor3fv((1,1,1))
        self.line_draw(P(W/2,H), P(W/2,0)) # mid-line
        self.circle_draw(P(W/2,H/2), W/8) # mid-circle
        #self.circle_draw(P(W/2,H/2), BALL_RADIUS) # mid-line

        self.rect_draw(P(W/20, (GOAL_POS[0]+GOAL_POS[1])*H/2), P(W/10, (GOAL_POS[1]-GOAL_POS[0])*H), h=10) # goal-1
        self.rect_draw(P(19*W/20, (GOAL_POS[0]+GOAL_POS[1])*H/2), P(W/10, (GOAL_POS[1]-GOAL_POS[0])*H), h=10) # goal-2

        self.rect_draw(P(3*W/20, H/2), P(3*W/10, 3*H/4), h=0) # D-1
        self.rect_draw(P(17*W/20, H/2), P(3*W/10, 3*H/4), h=0) # D-2

        # Borders
        glColor3fv((0.5,0.5,0.5))
        self.rect_draw(P(W/2, -0.05), P(W, .1), h=50, fill=True)
        self.rect_draw(P(-0.05, H/2), P(.1, H), h=50, fill=True)
        self.rect_draw(P(W+0.05, H/2), P(.1, H), h=50, fill=True)

    def ground_draw(self,win):
        ground_surfaces = (0,1,2,3)
        ground_vertices = ((0,GY,GZ), (GX,GY,GZ), (GX,GY,0), (0,GY,0))

        glBegin(GL_QUADS)
        glColor3fv((0,1,0))
        for vertex in ground_vertices:
            glVertex3fv(vertex)
        glEnd()

    def draw(self, win, debug=False):
        """ Draw everything """
        #self.ground_draw(win)
        self.field_draw(win)
        #self.goal_draw(win)
        self.team_human.draw(win, debug=debug)
        self.team_ai.draw(win, debug=debug)
        self.ball.draw(win, debug=debug)

    def next(self, a_h,a_ai):
        """
        Next loop that is the heart of the game
         - a (list): Actions of each player in the team
        """
        self.team_human.update(a_h) # Update team's state
        self.team_ai.update(a_ai) # Update team's state
        self.collision(self.team_human, a_h, self.team_ai, a_ai, self.ball)
        self.ball.update(self.team_human, self.team_ai, a_h, a_ai) # Update ball's state
        self.ball.goal_check() # Check if a goal is scoread
        self.team_human.set_nearest(self.ball) # select nearest human player
        return 0,0
