import pygame_menu
from settings import *

# Custom theme
custom_theme = pygame_menu.themes.THEME_DARK.copy() # define custom theme

menu_bg = pygame_menu.baseimage.BaseImage( # load background image
    image_path=MENU_BG,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)
custom_theme.background_color = menu_bg # Add background image
custom_theme.title_font = pygame_menu.font.FONT_8BIT
custom_theme.widget_font=pygame_menu.font.FONT_FRANCHISE

########### About ##############

about_menu = pygame_menu.Menu(H, W, 'About',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

about_menu.add_label('This is the first game that we created. It was originally written in ANSI C++ and worked on console only.', max_char=70, font_size=FONT_SIZE//2)
about_menu.add_label('It is a 9v9 Football game where you compete against the computer.', max_char=70, font_size=FONT_SIZE//2)
about_menu.add_label('This game is written by:', max_char=60, font_size=FONT_SIZE//2)
about_menu.add_label('Ashutosh Jani', max_char=60, font_size=FONT_SIZE//2)
about_menu.add_label('Manan Soni', max_char=60, font_size=FONT_SIZE//2)
about_menu.add_label('To know more visit github.com/MananSoni42/Fifa-42 ', max_char=60, font_size=FONT_SIZE//2)

about_menu.add_button('Back', pygame_menu.events.BACK)
#################################

########## Instructions #########

instr_menu = pygame_menu.Menu(H, W, 'Instructions',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)
instr_menu.add_label('* Use arrow keys to move your player. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* Use the QWE, ASD, ZXC keys for passing the ball in an appropriate direction. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* In game, use the space key to toggle Position holding. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* (whether your players return to their original positions). ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* Pause the game by pressing the esc key. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* Once in the pause menu, formations can be changed using. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* the space key followed by the left/right arrow keys. ', max_char=60, font_size=FONT_SIZE//2)
instr_menu.add_label('* Use backspace to exit the pause menu. ', max_char=60, font_size=FONT_SIZE//2)

instr_menu.add_button('Back', pygame_menu.events.BACK)
#################################

sett_menu = pygame_menu.Menu(H, W, 'Settings',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

colors = [
    ('DEFAULT', None),
    ('BLACK' , (0,0,0)),
    ('RED'   , (255,0,0)),
    ('ORANGE', (255,165,0)),
    ('YELLOW', (255,255,0)),
    ('PURPLE', (128,0,128)),
    ('NAVY'  , (0,0,128)),
    ('BLUE'  , (0,0,255)),
    ('CYAN'  , (0,255,255))
]

s1 = sett_menu.add_selector('Team 1 color:', colors)

s2 = sett_menu.add_selector('Team 2 color:', colors)

sett_menu.add_selector('Sound', [('ON', 1), ['OFF', 0]])

sett_menu.add_button('Back', pygame_menu.events.BACK)
#################################


########### Main menu ###########

main_menu = pygame_menu.Menu(H, W, 'FIFA 42',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

#################################
