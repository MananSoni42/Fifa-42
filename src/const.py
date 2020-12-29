"""
Game specific functions and constants

Includes:

- the actions that a player can take
- possible formations
- recolor a player sprite

Do not change these constants directly as other parts of the game rely on their correct format
"""

from pygame import Color
from point import P
from settings import *

############## Custom types ##############

# actions that can be performed by a plyer at any given time
ACT = {'NOTHING': P(0, 0), None: P(0, 0),
       'MOVE_U': P(0, -1), 'MOVE_D': P(0, 1), 'MOVE_L': P(-1, 0), 'MOVE_R': P(1, 0),
       'SHOOT_Q': P(-0.707, -0.707), 'SHOOT_W': P(0, -1), 'SHOOT_E': P(0.707, -0.707), 'SHOOT_A': P(-1, 0),
       'SHOOT_D': P(1, 0), 'SHOOT_Z': P(-0.707, 0.707), 'SHOOT_X': P(0, 1), 'SHOOT_C': P(0.707, 0.707)}
# 0.717 = 1/sqrt(2)

"""
Team formations
    - Must start with the keeper
    - Must contain positions for both left and right sides
    - Recommended to specify completley in terms of W and H (and PLAYER_RADIUS / BALL_RADIUS if reqd)

"""
FORM = {
    'default': {
        'name': 'Default (4-4-2)',  # name
        'img-num': 0,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(W//4, H//2 - H//10), 'pos': 'DEF'}, {
                    'coord': P(W//4, H//2 + H//10), 'pos': 'DEF'},
            {'coord': P(
                5*W//16, H//7), 'pos': 'DEF'}, {'coord': P(5*W//16, 6*H//7), 'pos': 'DEF'},

            {'coord': P(W//2, H//2 - H//10), 'pos': 'MID'}, {
                    'coord': P(W//2, H//2 + H//10), 'pos': 'MID'},
            {'coord': P(
                9*W//16, H//7), 'pos': 'MID'}, {'coord': P(9*W//16, 6*H//7), 'pos': 'MID'},

            {'coord': P(13*W//16, H//2 - H//5), 'pos': 'ATK'}, {
                    'coord': P(13*W//16, H//2 + H//5), 'pos': 'ATK'},
        ],
    },

    'balanced-1': {
        'name': 'Balanced (4-4-2 diamond)',  # name
        'img-num': 1,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(W//4, H//2 - H//10), 'pos': 'DEF'}, {
                    'coord': P(W//4, H//2 + H//10), 'pos': 'DEF'},
            {'coord': P(5*W//16, H//7), 'pos': 'DEF'},
            {'coord': P(5*W//16, 6*H//7), 'pos': 'DEF'},

            {'coord': P(W//2 + W//50, H//4), 'pos': 'MID'}, {
                    'coord': P(W//2 + W//50, 3*H//4), 'pos': 'MID'},
            {'coord': P(W//2 - 4*W//50, H//2), 'pos': 'MID'}, {
                    'coord': P(W//2 + 6*W//50, H//2), 'pos': 'MID'},

            {'coord': P(13*W//16, H//2 - H//5), 'pos': 'ATK'}, {
                    'coord': P(13*W//16, H//2 + H//5), 'pos': 'ATK'},
        ],
    },
    'balanced-2': {
        'name': 'Balanced (4-3-3)',  # name
        'img-num': 2,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(W//4, H//2 - H//10), 'pos': 'DEF'}, {
                    'coord': P(W//4, H//2 + H//10), 'pos': 'DEF'},
            {'coord': P(
                5*W//16, H//7), 'pos': 'DEF'}, {'coord': P(5*W//16, 6*H//7), 'pos': 'DEF'},

            {'coord': P(W//2 + W//50, H//4), 'pos': 'MID'}, {
                    'coord': P(W//2 + W//50, 3*H//4), 'pos': 'MID'},
            {'coord': P(W//2 - 2*W//50, H//2), 'pos': 'MID'},

            {'coord': P(13*W//16, H//2 - H//5), 'pos': 'ATK'}, {
                    'coord': P(13*W//16, H//2 + H//5), 'pos': 'ATK'},
            {'coord': P(14*W//16, H//2), 'pos': 'ATK'}
        ],
    },
    'attacking-1': {  # TODO
        'name': 'Attacking (3-4-3)',  # name
        'img-num': 3,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(
                    W//4, H//2 - H//4), 'pos': 'DEF'}, {'coord': P(W//4 - W//50, H//2), 'pos': 'DEF'},
            {'coord': P(W//4, H//2 + H//4), 'pos': 'DEF'},

            {'coord': P(W//2, H//2 - H//10),
                        'pos': 'MID'}, {'coord': P(W//2, H//2 + H//10), 'pos': 'MID'},
            {'coord': P(
                9*W//16, H//5), 'pos': 'MID'}, {'coord': P(9*W//16, 4*H//5), 'pos': 'MID'},

            {'coord': P(
                24*W//32, H//7), 'pos': 'ATK'}, {'coord': P(24*W//32, 6*H//7), 'pos': 'ATK'},
            {'coord': P(26*W//32, H//2), 'pos': 'ATK'},
        ],
    },
    'attacking-2': {
        'name': 'Attacking (3-3-4)',  # name
        'img-num': 4,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(
                    W//4, H//2 - H//4), 'pos': 'DEF'}, {'coord': P(W//4 - W//50, H//2), 'pos': 'DEF'},
            {'coord': P(W//4, H//2 + H//4), 'pos': 'DEF'},

            {'coord': P(W//2 + W//50, H//4), 'pos': 'MID'}, {
                    'coord': P(W//2 + W//50, 3*H//4), 'pos': 'MID'},
            {'coord': P(W//2 - 2*W//50, H//2), 'pos': 'MID'},

            {'coord': P(13*W//16, H//2 - H//10), 'pos': 'ATK'}, {
                    'coord': P(13*W//16, H//2 + H//10), 'pos': 'ATK'},
            {'coord': P(
                24*W//32, H//7), 'pos': 'ATK'}, {'coord': P(24*W//32, 6*H//7), 'pos': 'ATK'},
        ],
    },
    'attacking-3': {
        'name': 'Attacking (4-2-4)',  # name
        'img-num': 5,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(W//4, H//2 - H//10), 'pos': 'DEF'}, {
                    'coord': P(W//4, H//2 + H//10), 'pos': 'DEF'},
            {'coord': P(
                5*W//16, H//7), 'pos': 'DEF'}, {'coord': P(5*W//16, 6*H//7), 'pos': 'DEF'},

            {'coord': P(
                W//2, H//2 - H//5), 'pos': 'MID'}, {'coord': P(W//2, H//2 + H//5), 'pos': 'MID'},

            {'coord': P(28*W//32, H//2 - H//10), 'pos': 'ATK'}, {
                    'coord': P(28*W//32, H//2 + H//10), 'pos': 'ATK'},
            {'coord': P(
                26*W//32, H//7), 'pos': 'ATK'}, {'coord': P(26*W//32, 6*H//7), 'pos': 'ATK'},
        ],
    },
    'defensive-1': {
        'name': 'Defensive (5-3-2)',  # name
        'img-num': 6,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(
                    W//4 - W//50, H//2), 'pos': 'DEF'}, {'coord': P(W//4, 9*H//28), 'pos': 'DEF'},
            {'coord': P(
                W//4, 19*H//28), 'pos': 'DEF'}, {'coord': P(W//4 + W//12, H//7), 'pos': 'DEF'},
            {'coord': P(W//4 + W//12, 6*H//7), 'pos': 'DEF'},

            {'coord': P(W//2 + W//50, H//4), 'pos': 'MID'}, {
                    'coord': P(W//2 + W//50, 3*H//4), 'pos': 'MID'},
            {'coord': P(W//2 - 2*W//50, H//2), 'pos': 'MID'},

            {'coord': P(13*W//16, H//2 - H//5), 'pos': 'ATK'}, {
                    'coord': P(13*W//16, H//2 + H//5), 'pos': 'ATK'},
        ],
    },
    'defensive-2': {
        'name': 'Defensive (5-4-1)',  # name
        'img-num': 7,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(
                    W//4 - W//50, H//2), 'pos': 'DEF'}, {'coord': P(W//4, 9*H//28), 'pos': 'DEF'},
            {'coord': P(
                W//4, 19*H//28), 'pos': 'DEF'}, {'coord': P(W//4 + W//12, H//7), 'pos': 'DEF'},
            {'coord': P(W//4 + W//12, 6*H//7), 'pos': 'DEF'},

            {'coord': P(W//2, H//2 - H//10),
                        'pos': 'MID'}, {'coord': P(W//2, H//2 + H//10), 'pos': 'MID'},
            {'coord': P(
                19*W//32, H//5), 'pos': 'MID'}, {'coord': P(19*W//32, 4*H//5), 'pos': 'MID'},

            {'coord': P(27*W//32, H//2), 'pos': 'ATK'},
        ],
    },
    'defensive-3': {
        'name': 'Defensive (4-5-1)',  # name
        'img-num': 8,  # number corresponding to image in assets/formations directory
        'L': [
                {'coord': P(2*PLAYER_RADIUS + BALL_RADIUS, H//2), 'pos': 'GK'},

                {'coord': P(W//4, H//2 - H//10), 'pos': 'DEF'}, {
                    'coord': P(W//4, H//2 + H//10), 'pos': 'DEF'},
            {'coord': P(
                5*W//16, H//7), 'pos': 'DEF'}, {'coord': P(5*W//16, 6*H//7), 'pos': 'DEF'},

            {'coord': P(W//2 - W//12, H//2 - H//50), 'pos': 'MID'}, {
                    'coord': P(W//2 + W//50, 9*H//28), 'pos': 'MID'},
            {'coord': P(W//2 + W//50, 19*H//28), 'pos': 'MID'}, {
                    'coord': P(W//2 + W//6, H//7), 'pos': 'MID'},
            {'coord': P(W//2 + W//6, 6*H//7), 'pos': 'MID'},

            {'coord': P(27*W//32, H//2), 'pos': 'ATK'},
        ],
    },
}

for key in FORM.keys():  # Fill in right side counterparts of all formations
    FORM[key]['R'] = [
        {'coord': P(W, H) - form['coord'], 'pos': form['pos']} for form in FORM[key]['L']]

############## Functions ##############


def recolor(surface, color=(255, 108, 0)):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            val = surface.get_at((x, y))
            surface.set_at((x, y), Color(r, g, b, val[3]))


def draw_form(win, curr_form):
    win.fill((14, 156, 23))  # constant green
    pygame.draw.rect(win, (255, 255, 255), (0, 0, W -
                                            LINE_WIDTH, H - LINE_WIDTH), LINE_WIDTH)  # border
    pygame.draw.rect(win, (255, 255, 255),
                     (W//2 - LINE_WIDTH//2, 0, LINE_WIDTH, H))  # mid line
    pygame.draw.circle(win, (255, 255, 255), (W//2, H//2),
                       H//5, LINE_WIDTH)  # mid circle
    pygame.draw.rect(win, (255, 255, 255), (4*W//5-LINE_WIDTH //
                                            2, 0.1*H, W//5, 0.8*H), LINE_WIDTH)  # right D
    pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2,
                                            0.1*H, W//5, 0.8*H), LINE_WIDTH)  # left D
    pygame.draw.rect(win, (255, 255, 255), (19*W//20-LINE_WIDTH//2,
                                            GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH)  # right goal
    pygame.draw.rect(win, (255, 255, 255), (LINE_WIDTH//2,
                                            GOAL_POS[0]*H, W//20, (GOAL_POS[1]-GOAL_POS[0])*H), LINE_WIDTH)  # right goal
    for pos in FORM[curr_form]['L']:
        win.blit(RUN[1]['L'][0]['full'], (pos - PLAYER_CENTER).val)

######################################
