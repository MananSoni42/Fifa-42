"""
Team formations
    - Must start with the keeper
    - Must contain positions for both left and right sides
    - Recommended to specify completley in terms of W and H (and PLAYER_RADIUS / BALL_RADIUS if reqd)

"""
from point import P
from settings import *

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
