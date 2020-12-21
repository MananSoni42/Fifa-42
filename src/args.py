""" Command line arguments for the game """

import argparse
from const import FORM

def get_args():
    parser = argparse.ArgumentParser(description='Play Fifa-42')

    parser.add_argument('--sound_off', action='store_true', default=False,
                        help='Play the game without any sound')

    parser.add_argument('--menu_off', action='store_true', default=False,
                        help='Play the game without displaying the menu')

    parser.add_argument('--camera', choices={'default', 'full', 'zoomed'},
                        default='default',
                        help='Camera angle')

    parser.add_argument('--difficulty', type=int, choices=range(0,101),
                       metavar="[0-100]", default=42,
                       help='Game difficulty (0-100): Easy (0-10) | Medium (11-50) | Hard (51-80)')

    parser.add_argument('--opponent', choices={'random', 'AI'},
                        default='AI',
                        help='Choose your opponent')

    parser.add_argument('--fps', type=int, default=42,
                        help='Play the game without displaying the menu')

    forms = set(FORM.keys())
    parser.add_argument('--team1_form', choices=forms,
                        metavar="{'default', 'balanced-1/2' , 'attacking-1/2/3', 'defensive-1/2/3'}",
                        default='default',
                        help='Team 1\'s formation')

    parser.add_argument('--team2_form', choices=forms,
                        metavar="{'default', 'balanced-1/2' , 'attacking-1/2/3', 'defensive-1/2/3'}",
                        default='default',
                        help='Team 2\'s formation')

    args = parser.parse_args()
    return args
