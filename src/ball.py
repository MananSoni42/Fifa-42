"""
Define the football used in the game
"""

from settings import *
from const import ACT
from pygame import mixer

# Init Sounds
mixer.init(44100, -16,2,2048)
single_short_whistle = mixer.Sound(SINGLE_SHORT_WHISTLE)
goal_sound = mixer.Sound(GOAL)
bounce = mixer.Sound(BOUNCE)
boo_sound = mixer.Sound(BOOING)

class Ball:
    """
    Implement the football used in the game
    """

    def __init__(self, pos, sound=True):
        """
        Initialize the Football

        Attributes:
            pos (Point): the initial position of the ball
        """
        self.pos = P(pos)
        self.vel = P(0,0)
        self.sound = sound
        self.free = True
        self.color = (50,50,50)
        self.ball_stats = {
            'last_player': -1,
            'last_team': -1,
            'player': -1,
            'team': -1,
        }

    def draw(self, win, cam, debug=False):
        """
        Draw the football

        Attributes:
            win (pygame.display): Window on which to draw
            debug (bool): If enabled, show the square used to approximate the ball
            as well as a red border whenever the ball is not free
        """
        if debug:
            cam.rect(win, (100,100,100), (self.pos.x-BALL_RADIUS, self.pos.y-BALL_RADIUS,BALL_RADIUS*2,BALL_RADIUS*2))
            if not self.free:
                cam.circle(win, (255,0,0), self.pos.val, BALL_RADIUS+LINE_WIDTH, LINE_WIDTH)
        cam.blit(win, FOOTBALL_IMG, self.pos.val, size=P(2*BALL_RADIUS, 2*BALL_RADIUS))

    def reset(self, pos):
        """
        Reset the ball

        Attributes:
            pos (Point): the initial position of the ball
        """
        self.pos = P(pos)
        self.vel = P(0,0)
        self.free = True
        self.ball_stats['last_player'] = -1
        self.ball_stats['last_team'] = -1
        self.ball_stats['player'] = -1
        self.ball_stats['team'] = -1

    def goal_check(self, stats):
        """
        Check if a goal is scored

        Attributes:
            stats (Stats):  Keep track of game statistics for the pause menu
        """
        goal = False
        reset = False
        side = 0 # Which team's goalpost the ball entered
        if not (BALL_RADIUS < self.pos.x < W - BALL_RADIUS):
            reset = True
            if self.pos.x <= BALL_RADIUS:
                pos = P(PLAYER_RADIUS + BALL_RADIUS, H//2)
                side = 1
            else:
                pos = P(W - PLAYER_RADIUS - BALL_RADIUS, H//2)
                side = 2

            if GOAL_POS[0]*H < self.pos.y < GOAL_POS[1]*H:

                # Play celebration sound
                if self.sound:
                    single_short_whistle.play()
                    goal_sound.play()

                goal = True
                stats.goals[3-side] += 1 # maps 1 -> 2, 2 -> 1 bcoz the goal goes to the other side!
                pos = P(W//2, H//2)

        if reset:
            self.update_stats(stats, goal=goal, side=side)
            self.reset(pos)
        return goal

    def update_stats(self, stats, player=None, goal=None, side=None):
        """
        Sync ball statistics with the global variables

        Attributes:
            player (Agent): Player that received the ball
            goal (bool): True if a goal is scored
            side (int): id of the team which conceded the goal

        Activates when a player receives the ball or during a goal attempt

            - Possession: +1 if same team pass is recorded
            - Pass: +1 to 'succ' if same team pass is recorded
                    +1 to 'fail' if diff team pass is recorded
            - Shot: +1 to 'succ' if a goal is scored
                    +1 to 'fail' if goal is not scored (out of bounds) / keeper stops the ball
                    Does not apply if player shoots towards his own goal
        """
        if player is not None: # Player receives the ball
            self.ball_stats['last_player'] = self.ball_stats['player']
            self.ball_stats['last_team'] = self.ball_stats['team']
            self.ball_stats['player'] = player.id
            self.ball_stats['team'] = player.team_id

            if self.ball_stats['last_team'] == self.ball_stats['team']: # Same team pass
                if self.ball_stats['last_player'] != self.ball_stats['player'] :
                    stats.pos[self.ball_stats['team']] += 1
                    stats.pass_acc[self.ball_stats['team']]['succ'] += 1
            else: # Different team pass
                if self.ball_stats['last_team'] != -1:
                    if self.ball_stats['player'] == 0: # GK of different team receives the ball
                        stats.shot_acc[self.ball_stats['last_team']]['fail'] += 1
                    else:
                        stats.pass_acc[self.ball_stats['last_team']]['fail'] += 1

        elif goal is not None and side != self.ball_stats['team']: # Called when a goal is scored, don't change if player shoots towards his own goalpost
            if goal:
                stats.shot_acc[self.ball_stats['team']]['succ'] += 1
            else:
                stats.shot_acc[self.ball_stats['team']]['fail'] += 1
                if self.sound:
                    boo_sound.play() # Play when missed shot

    def ball_player_collision(self, team, stats):
        """
        Check if the ball has been captured by a player

        Attributes:
            team (Team): The team for which to check
            stats (Stats):  Keep track of game statistics for the pause menu
        """
        for player in team.players:
            if self.pos.dist(player.pos) < PLAYER_RADIUS + BALL_RADIUS:
                self.vel = P(0,0)
                self.free = False
                self.dir = player.walk_dir
                self.update_stats(stats, player=player)

    def check_capture(self, team1, team2, stats):
        """
        If the ball is not free, move the ball along with the player rather than on it's own

        Attributes:
            team1 (Team): Team facing right
            team2 (Team): Team facing left
            stats (Stats):  Keep track of game statistics for the pause menu
        """

        if self.ball_stats['team'] == 1:
            player = team1.players[self.ball_stats['player']]
        elif self.ball_stats['team'] == 2:
            player = team2.players[self.ball_stats['player']]

        if not self.free:
            self.dir = player.walk_dir
            if self.dir == 'L':
                self.pos = player.pos + P(-1,1)*BALL_OFFSET*BALL_CENTER
            elif self.dir == 'R':
                self.pos = player.pos + BALL_OFFSET*BALL_CENTER

        else:
            self.ball_player_collision(team1, stats)
            self.ball_player_collision(team2, stats)

    def update(self, team1, team2, action1, action2, stats):
        """
        Update the ball's (in-game) state according to specified action
        Attributes:
            team1 (Team): Team facing right
            team2 (Team): Team facing left
            action1 (list): Actions of team 1
            action2 (list): Actions of team 2
            stats (Stats):  Keep track of game statistics for the pause menu

        Calls ```check_capture()``` and ```goal_check()```
        """

        if self.ball_stats['team'] == 1:
            a = action1[self.ball_stats['player']]
        elif self.ball_stats['team'] == 2:
            a = action2[self.ball_stats['player']]

        if self.free:
            self.pos += P(BALL_SPEED,BALL_SPEED)*self.vel
            if not (BALL_RADIUS <= self.pos.x <= W - BALL_RADIUS): # Ball X overflow
                self.pos.x = min(max(BALL_RADIUS, self.pos.x),W - BALL_RADIUS)
                self.vel.x *= (-1) # Flip X velocity
                if self.sound:
                    bounce.play() # Bounce sound

            if not(BALL_RADIUS <= self.pos.y <= H - BALL_RADIUS): # Ball Y overflow
                self.pos.y = min(max(BALL_RADIUS, self.pos.y),H - BALL_RADIUS)
                self.vel.y *= (-1) # Flip Y velocity
                if self.sound:
                    bounce.play() # Bounce sound


        elif a in ['SHOOT_Q', 'SHOOT_W', 'SHOOT_E', 'SHOOT_A', 'SHOOT_D', 'SHOOT_Z', 'SHOOT_X', 'SHOOT_C']: # Player shoots
            self.vel = P(ACT[a])
            self.free = True
            # Ball relearse mechanics (when player shoots)
            const = PLAYER_RADIUS + BALL_RADIUS + 1
            if self.dir == 'R' and ACT[a].x >= 0:
                self.pos.x += const - BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'R' and ACT[a].x < 0:
                self.pos.x -= const + BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'L' and ACT[a].x > 0:
                self.pos.x += const + BALL_RADIUS*BALL_OFFSET.x
            elif self.dir == 'L' and ACT[a].x <= 0:
                self.pos.x -= const - BALL_RADIUS*BALL_OFFSET.x

        self.check_capture(team1, team2, stats)
        self.goal_check(stats)
