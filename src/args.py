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
                       help='Game difficulty (0-100)')

    parser.add_argument('--team1', choices={'random', 'AI', 'human'},
                        default='human',
                        help='Choose your opponent')

    parser.add_argument('--team2', choices={'random', 'AI'},
                        default='AI',
                        help='Choose your opponent')

    parser.add_argument('--fps', type=int, default=42,
                        help='Define the number of frames rendered per second')

    forms = set(FORM.keys())
    parser.add_argument('--team1_formation', choices=forms,
                        metavar="{'default', 'balanced-1/2' , 'attacking-1/2/3', 'defensive-1/2/3'}",
                        default='default',
                        help='Team 1\'s formation')

    parser.add_argument('--team2_formation', choices=forms,
                        metavar="{'default', 'balanced-1/2' , 'attacking-1/2/3', 'defensive-1/2/3'}",
                        default='default',
                        help='Team 2\'s formation')

    args = parser.parse_args()
    return args
