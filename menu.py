import pygame_menu
from settings import *

MAX_CHAR = 100

# Custom theme
menu_bg = pygame_menu.baseimage.BaseImage( # load background image
    image_path=MENU_BG,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

custom_theme = pygame_menu.themes.Theme(
    background_color = menu_bg, # Add background image
    focus_background_color = (255,255,255,128),
    menubar_close_button = False,
    #selection_color = (255,255,255),
    #widget_selection_effect = pygame_menu.widgets.LeftArrowSelection,
    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
    title_background_color = (52, 168, 235),
    title_shadow = True,
    title_shadow_offset = 5,
    title_font = pygame_menu.font.FONT_8BIT,
    title_font_size = 3*FONT_SIZE//2,
    widget_font_color = (52, 168, 235),
    widget_font = pygame_menu.font.FONT_FRANCHISE,
    widget_font_size = FONT_SIZE,
)

#custom_theme = pygame_menu.themes.THEME_BLUE.copy() # define custom theme

########### About ##############

about_menu = pygame_menu.Menu(H, W, ' About',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

about_menu.add_label('This is the first game that we created. It was originally written in ANSI C++ and worked on console only.', max_char=70)
about_menu.add_label('It is a 9v9 Football game where you compete against the computer.', max_char=MAX_CHAR)
about_menu.add_label('This game is written by:', max_char=MAX_CHAR)
about_menu.add_label('Manan Soni', max_char=MAX_CHAR)
about_menu.add_label('Ashutosh Jani', max_char=MAX_CHAR)
about_menu.add_label('To know more visit github.com/MananSoni42/Fifa-42 ', max_char=MAX_CHAR)

about_menu.add_button('Back', pygame_menu.events.BACK)
#################################

########## Instructions #########

instr_menu = pygame_menu.Menu(H, W, ' Instructions',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)
instr_menu.add_label('* Use arrow keys to move your player. ', max_char=MAX_CHAR)
instr_menu.add_label('* Use the QWE, ASD, ZXC keys for passing the ball in an appropriate direction. ', max_char=MAX_CHAR)
instr_menu.add_label('* In game, use the space key to toggle Position holding. ', max_char=MAX_CHAR)
instr_menu.add_label('* (whether your players return to their original positions). ', max_char=MAX_CHAR)
instr_menu.add_label('* Pause the game by pressing the esc key. ', max_char=MAX_CHAR)
instr_menu.add_label('* Once in the pause menu, formations can be changed using. ', max_char=MAX_CHAR)
instr_menu.add_label('* the space key followed by the left/right arrow keys. ', max_char=MAX_CHAR)
instr_menu.add_label('* Use backspace to exit the pause menu. ', max_char=MAX_CHAR)

instr_menu.add_button('Back', pygame_menu.events.BACK)
#################################

########### Settings  ###########
sett_menu = pygame_menu.Menu(H, W, ' Settings',
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

s1 = sett_menu.add_selector('Team 1 color:', colors, font_color=(255,255,255))

s2 = sett_menu.add_selector('Team 2 color:', colors, font_color=(255,255,255))

sett_menu.add_selector('Sound', [('ON', 1), ['OFF', 0]])

sett_menu.add_button('Back', pygame_menu.events.BACK)
#################################

########### Settings  ###########
form_menu = pygame_menu.Menu(H, W, ' Settings',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

form_opts = [
    ('DEFAULT', 'DEFAULT'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
]

f1 = form_menu.add_selector('Formation:  ', form_opts)

form_menu.add_button('Back', pygame_menu.events.BACK)
#################################


########### Main menu ###########

main_menu = pygame_menu.Menu(H, W, ' FIFA 42',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

#################################
