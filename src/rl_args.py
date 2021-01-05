'''
Command line arguments for training the rl model

Type ```python3 rl_train.py --help``` for a descriptions of all the available options
'''

import argparse
from const import FORM

def get_args():
    parser = argparse.ArgumentParser(description='Play Fifa-42')

    parser.add_argument('--display', action='store_true', default=False,
                        help='Show the gam while training')

    parser.add_argument('--agent_dir', type=str,
                        default='',
                        help='Camera angle')

    parser.add_argument('--camera', choices={'default', 'full', 'zoomed'},
                        default='default',
                        help='Camera angle')

    parser.add_argument('--difficulty', type=int, choices=range(0,101),
                       metavar="[0-100]", default=42,
                       help='Game difficulty (0-100)')

    parser.add_argument('--team1', choices={'rl', 'random', 'ai', 'human'},
                        default='ai',
                        help='Choose your opponent')

    parser.add_argument('--team2', choices={'rl', 'random', 'ai'},
                        default='rl',
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
                        default='balanced-1',
                        help='Team 2\'s formation')

    args = parser.parse_args()
    return args
