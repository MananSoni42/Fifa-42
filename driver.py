import time
from settings import *
import pygame_menu
from game import Game
from teams.human import HumanTeam
from teams.original_ai import OriginalAITeam

"""
Driver program to test the game
"""
pygame.init()
win = pygame.display.set_mode((W,H), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption("FIFA-42")

# Init music
pygame.mixer.init(44100, -16,2,2048)
menu_music = mixer.Sound(MENU_MUSIC)
single_short_whistle = mixer.Sound(SINGLE_SHORT_WHISTLE)
applause = mixer.Sound(APPLAUSE)
menu_music.play(-1)

# Define teams (Team 1 faces right by default)
team1 = HumanTeam(formation='default', color=(0,32,255))
team2 = OriginalAITeam(formation='balanced-1', color=(255,128,0))

def play_game():
    mixer.pause()
    single_short_whistle.play()
    applause.play(-1)
    game = Game(team1,team2) # initialize the game
    """ Game loop """
    while not game.end: # Game loop
        clock.tick(FPS) # FPS

        game.check_interruptions() # Check for pause or quit keys

        if game.pause:
            game.draw(win, debug=False)
            game.pause_draw(win) # Draws on-top of the (frozen) game
        else:
            game.draw(win, debug=False)
            game.next() # Move the game forward

        pygame.display.update() # refresh screen

    main_menu.mainloop(win, bgfun=draw_bg) # Game never ends - Show the menu

### The menu
from menu import main_menu, instr_menu, about_menu, sett_menu, form_menu, s1, s2, f1, f2, selected_team, selected_formation

def color_change(widget, col, team): # Change color of widget and corresponding team
    widget.set_background_color(col)
    team.color = col

def set_form(form, team_id): # Change team 1's formation and widget's background
    global selected_team, selected_formation

    selected_team = team_id
    selected_formation[selected_team] = form

    team1.formation = selected_formation[1][0]
    team2.formation = selected_formation[2][0]

def draw_bg():
    if main_menu.get_current().get_title() == 'Formation':
        dummy_game = Game(team1,team2)
        dummy_game.draw(win, hints=False)

s1.change = lambda col: color_change(s1, col, team1) # set team 1's color
s2.change = lambda col: color_change(s2, col, team2) # Set team 2's color
f1.change = lambda id: set_form(id,team_id=1) # set team 1's formation
f2.change = lambda id: set_form(id,team_id=2) # set team 2's formation

main_menu.add_button('Play', play_game)
main_menu.add_button('Instructions', instr_menu)
main_menu.add_button('Choose formation', form_menu)
main_menu.add_button('Settings', sett_menu)
main_menu.add_button('About', about_menu)
main_menu.add_button('Quit', pygame_menu.events.EXIT) # Add exit button

###########################################

main_menu.mainloop(win, bgfun=draw_bg) # Show the menu
