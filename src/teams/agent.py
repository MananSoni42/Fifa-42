"""
Defines how an agent is created, drawn and updated

Override the ```move``` method to create a valid custom agent
"""

from settings import *
from const import ACT
from abc import ABC, abstractmethod


class Agent(ABC):
    """
    Abstract class that controls agents in the football game

    Implement the move method to instantiate a valid agent
    """

    def __init__(self, id, team_id, pos, dir='L'):
        """
        Initialize a player

        Attributes:
            id (int): Player's unique ID
            team_id (int): ID of the team the player plays for
            pos (Point): The player's initial position
            dir (string): The player's current direction (which way it faces). Either 'R' or 'L'
        """
        self.id = id  # Unique ID starts from 0 (also denotes it's position in team array)
        self.team_id = team_id  # ID of player's team
        self.pos = P(pos)  # Starting position
        self.walk_dir = dir  # options are R (right), L (left)
        self.walk_count = 0  # For running animation
        self.rnd = 0.01*random.random() # random number used to break ties

    def __str__(self):
        return f'\nAgent {self.id} - {self.pos}'

    def draw(self, win, cam, team_id, debug=False):
        """
        Draw the player as an animated sprite

        Attributes:
            win (pygame.display): Window on which to draw
            team_id (int): Required to get the correct sprite
            debug (bool): Show additional info including the player's ID and the square used to approximate the player
        """
        if debug:
            cam.rect(win, (255,255,255,100), (self.pos.x-PLAYER_CENTER.x, self.pos.y-PLAYER_CENTER.y, 2*PLAYER_RADIUS, 2*PLAYER_RADIUS))
            pl_font = pygame.font.Font(FONT_NEVIS, FONT_SIZE//3)
            text = pl_font.render(str(self.id), True, (0, 0, 0))
            text = {
                'full': text,
                'default': text,
                'zoom': text,
            }
            cam.blit(win, text, (self.pos).val, P(FONT_SIZE//3,FONT_SIZE//3))

        cam.blit(win, RUN[team_id][self.walk_dir][self.walk_count //
                                             WALK_DELAY], (self.pos).val,
                size=P(2*PLAYER_RADIUS, 2*PLAYER_RADIUS).val)

    def update(self, action, players):
        """
        Update player's (in-game) state based on his action
        """
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
            self.pos = P(min(max(PLAYER_RADIUS, self.pos.x), W - PLAYER_RADIUS), min(
                max(PLAYER_RADIUS, self.pos.y), H - PLAYER_RADIUS))  # account for overflow

    @abstractmethod
    def move(self, state_prev, state, reward):
        """
        Implement this method for a valid agent

        Attributes:
            state_prev (dict): The lsat to last game state
            state (dict): The last game state
            reward (list): Reward returned from this state (Not implemented)

        Should return a valid action
        """
        pass
