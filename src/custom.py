import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math

pygame.init()
display = (400, 300)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)

sphere = gluNewQuadric() #Create new sphere

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False

    keypress = pygame.key.get_pressed()

    # init model view matrix
    glLoadIdentity()

    # init the view matrix
    glPushMatrix()
    glLoadIdentity()

    # apply the movment
    if keypress[pygame.K_w]:
        glTranslatef(0,0,0.1)
    if keypress[pygame.K_s]:
        glTranslatef(0,0,-0.1)
    if keypress[pygame.K_d]:
        glTranslatef(-0.1,0,0)
    if keypress[pygame.K_a]:
        glTranslatef(0.1,0,0)

    # multiply the current matrix by the get the new view matrix and store the final vie matrix
    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    # apply view matrix
    glPopMatrix()
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Clear the screen

    glPushMatrix()

    glTranslatef(-1.5, 0, 0) #Move to the place
    glColor4f(0.5, 0.2, 0.2, 1) #Put color
    gluSphere(sphere, 1.0, 32, 16) #Draw sphere

    glPopMatrix()

    pygame.display.flip() #Update the screen
    pygame.time.wait(10)

pygame.quit()
