'''
Command line arguments for training the rl model

Type ```python3 rl_train.py --help``` for a descriptions of all the available options
'''
import sys
sys.path.insert(0, '../src')

import argparse
from const import FORM

def get_args():
    parser = argparse.ArgumentParser(description='Play Fifa-42')

    parser.add_argument('--ep', type=int,
                       help='Number of episodes to train for')

    parser.add_argument('--display', action='store_true', default=False,
                        help='Show the game while training')

    parser.add_argument('--nosave', action='store_true', default=False,
                        help='Don\'t save the agents after training')

    parser.add_argument('--agent_dir', type=str,
                        default='weights',
                        help='directory for saving / loading the agents\' weights')

    parser.add_argument('--camera', choices={'default', 'full', 'zoomed'},
                        default='default',
                        help='Camera angle')

    parser.add_argument('--difficulty', type=int, choices=range(0,101),
                       metavar="[0-100]", default=42,
                       help='Game difficulty (0-100)')

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

    if not (args.ep):
        parser.error('Specify the number of episodes for training')

    return args
