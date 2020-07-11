from team import HumanTeam, RandomTeam
from game import Game
from settings import *
import time
import pygame_menu

"""
Driver program to test the game
"""
pygame.init()
win = pygame.display.set_mode((W,H)) # Reference to window needed for drawing anything
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

def set_difficulty(value, difficulty):
    print(value,difficulty)
    pass

# Define teams (Team 1 faces right by default)
team1 = HumanTeam(formation='default', color=(0,32,255))
team2 = RandomTeam(color=(255,128,0))

def play_game():
    game = Game(team1,team2) # initialize the game
    """ Game loop """
    while not game.end: # Game loop
        clock.tick(FPS) # FPS

        game.check_interruptions() # Check for pause or quit keys

        if game.pause:
            game.draw(win)
            game.pause_draw(win) # Draws on-top of the (frozen) game
        else:
            game.draw(win, debug=False)
            game.next() # Move the game forward

        pygame.display.update() # refresh screen
    pygame.quit()

### The menu
from menu import main_menu,instr_menu,about_menu,sett_menu,s1,s2

def color_change(widget, col, team): # Change color of widget and corresponding team
    if col:
        widget.set_background_color(col)
        team.color = col

s1.change = lambda col: color_change(s1, col, team1) # set team 1's color
s2.change = lambda col: color_change(s2, col, team2) # Set team 2's color

main_menu.add_button('Play', play_game)
main_menu.add_button('Instructions', instr_menu)
main_menu.add_button('Settings', sett_menu)
main_menu.add_button('About', about_menu)
main_menu.add_button('Quit', pygame_menu.events.EXIT) # Add exit button

###########################################

main_menu.mainloop(win) # Show the menu
