from team import HumanTeam, RandomTeam
from game import Game
from settings import *
from const import choose_formation
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

game = Game(team1,team2)

def play_game():
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

### Configuring the menu

# Custom theme
custom_theme = pygame_menu.themes.THEME_DARK.copy() # define custom theme

menu_bg = pygame_menu.baseimage.BaseImage( # load background image
    image_path=MENU_BG,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)
custom_theme.background_color = menu_bg # Add background image

main_menu = pygame_menu.Menu(H, 3*W//4, 'FIFA-42',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

about_menu = pygame_menu.Menu(H, 3*W//4, 'About',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

instr_menu = pygame_menu.Menu(H, 3*W//4, 'Instructions',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

about_menu.add_label('This is the first game that we created. It was originally written in ANSI C++ and worked on console only.', max_char=70, font_size=FONT_SIZE//2)
about_menu.add_label('It is a 9v9 Football game where you compete against the computer.', max_char=70, font_size=FONT_SIZE//2)
about_menu.add_label('This game is written by:', max_char=60, font_size=FONT_SIZE//2)
about_menu.add_label('Ashutosh Jani', max_char=60, font_size=FONT_SIZE//2)
about_menu.add_label('Manan Soni', max_char=60, font_size=FONT_SIZE//2)
about_menu.add_label('To know more visit github.com/MananSoni42/Fifa-42 ', max_char=60, font_size=FONT_SIZE//2)

instr_menu.add_label('* Use arrow keys to move your player. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* Use the QWE, ASD, ZXC keys for passing the ball in an appropriate direction. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* In game, use the space key to toggle Position holding. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* (whether your players return to their original positions). ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* Pause the game by pressing the esc key. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* Once in the pause menu, formations can be changed using. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* the space key followed by the left/right arrow keys. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* Use backspace to exit the pause menu. ', max_char=60, font_size=FONT_SIZE//2)

about_menu.add_button('Back', pygame_menu.events.BACK)
instr_menu.add_button('Back', pygame_menu.events.BACK)

main_menu.add_button('Play', play_game) # Add play button to menu
main_menu.add_button('Instructions', instr_menu) # Add set formation button to menu
main_menu.add_button('About', about_menu) # Add set formation button to menu
main_menu.add_button('Quit', pygame_menu.events.EXIT) #

# Display the menu
main_menu.mainloop(win)
