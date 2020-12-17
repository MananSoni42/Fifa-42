from teams.team import HumanTeam, RandomTeam
from game import Game
from settings import *

# from const import * # Enable for possession stats and goals

"""
Driver program to test the game
"""
pygame.init()
display = (W, H)
#camera_angle = 0

win = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("FIFA-42")
clock = pygame.time.Clock()

glLineWidth(LINE_WIDTH);
glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0]/display[1]), 0.1, 3*GZ)
glTranslatef(*CAM_POS)
glRotatef(CAM_ANG,1,0,0)
glTranslatef(*CAM_POST)

"""
Define teams
    - One needs to be AI, other can be human or AI
    - ids need to be 1 and 2 only
    - Team 1 faces right by default
"""
team1 = HumanTeam(id = 1, formation='default-left', color=(0,0.1,1))
team2 = RandomTeam(id = 2, formation='default-right', color=(1,0.5,0))
game = Game(team1,team2)

pygame.key.set_repeat(1,1) # Generate multiple keydown events if a key is pressed continuously

while not game.end:
    clock.tick(FPS) # FPS

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    game.draw(win, debug=False)
    pygame.display.flip() # refresh screen

    a1 = team1.move()
    a2 = team2.move()
    s,r = game.next(a1,a2)
