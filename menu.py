import pygame_menu
from settings import *
from const import FORM

MAX_CHAR = 50

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
    widget_font = pygame_menu.font.FONT_NEVIS,
    widget_font_size = FONT_SIZE,
    scrollbar_color = (42,42,42),
    scrollbar_slider_color = (52, 168, 235)
)

########### About ##############

about_menu = pygame_menu.Menu(H, W, ' About',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

about_menu.add_label('Written by:', max_char=MAX_CHAR)
about_menu.add_label('Manan Soni', max_char=MAX_CHAR)
about_menu.add_label('Ashutosh Jani', max_char=MAX_CHAR)
about_menu.add_label('To know more visit github.com/MananSoni42/Fifa-42 ', max_char=MAX_CHAR, selectable=True)
about_menu.add_vertical_margin(40)
about_menu.add_button('Back', pygame_menu.events.BACK)
#################################

########## Instructions #########

instr_menu = pygame_menu.Menu(H, W, ' Instructions',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True,
                             #columns=2,
                             #rows=21,
)
"""
# Col 1
instr_menu.add_label('This is an 11 v 11 Football game where you play against an AI computer.', max_char=MAX_CHAR)
instr_menu.add_label('You control a single player (marked by a red dot on top of him)', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('Controls', align=pygame_menu.locals.ALIGN_RIGHT)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('< ^ v >')
instr_menu.add_vertical_margin(40)
instr_menu.add_image(CONTROLS_IMG)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('SPACE')
instr_menu.add_vertical_margin(40)
instr_menu.add_label('ESC')
instr_menu.add_vertical_margin(40)
instr_menu.add_label('BACKSPACE')
instr_menu.add_vertical_margin(0)

# Col 2
#instr_menu.add_vertical_margin(490)
instr_menu.add_vertical_margin(490)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('Move player')
instr_menu.add_vertical_margin(300)
instr_menu.add_label('Shoot the ball')
instr_menu.add_vertical_margin(250)
instr_menu.add_label('Toggle')
instr_menu.add_vertical_margin(40)
instr_menu.add_label('Pause game (view stats)')
instr_menu.add_vertical_margin(40)
instr_menu.add_label('Resume game')
instr_menu.add_vertical_margin(60)
instr_menu.add_button('Back', pygame_menu.events.BACK,align=pygame_menu.locals.ALIGN_LEFT)
"""
instr_menu.add_label('This is an 11 v 11 Football game where you play against an AI computer.', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('You control a single player (marked by a red dot)', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('Your play as Team 1 and the computer is Team 2', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('Go back into the choose formations menu to select formations for your team as well as the computer\'s team', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('Team colors can be changed from the settings', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(80)
instr_menu.add_label('Controls')
instr_menu.add_vertical_margin(40)
instr_menu.add_label('< ^ v >                   Move the player', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_label('(arrow keys)', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(40)
#instr_menu.add_label('Q   W   E            Shoot the ball', align=pygame_menu.locals.ALIGN_LEFT)
#instr_menu.add_label('A    *    D             (in the direction relative to the', align=pygame_menu.locals.ALIGN_LEFT)
#instr_menu.add_label('Z   X    C             player denoted by the asterisk )', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_label('Shoot the ball')
instr_menu.add_image(CONTROLS_IMG, align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('SPACE                Toggle if players return to their original', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_label('                           place according to the team\'s formation', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('ESC                     Bring up pause menu', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(40)
instr_menu.add_label('BACKSPACE        Collapse pause menu', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(40)
instr_menu.add_button('Back', pygame_menu.events.BACK)
#################################

########### Settings  ###########
sett_menu = pygame_menu.Menu(H, W, ' Settings',
                             theme=custom_theme,
                             center_content=False,
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

sett_menu.add_vertical_margin(40)
s1 = sett_menu.add_selector('Team 1 color:', colors, font_color=(255,255,255))

s2 = sett_menu.add_selector('Team 2 color:', colors, font_color=(255,255,255))

sett_menu.add_selector('Sound', [('ON', 1), ['OFF', 0]])

sett_menu.add_vertical_margin(40)
sett_menu.add_button('Back', pygame_menu.events.BACK)
#################################

########### Settings  ###########
form_theme = pygame_menu.themes.Theme(
    background_color = (30, 50, 107, 0), # Add background image
    menubar_close_button = False,
    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
    title_background_color = (52, 168, 235,42),
    title_shadow = True,
    title_shadow_offset = 5,
    title_font = pygame_menu.font.FONT_8BIT,
    title_font_size = 3*FONT_SIZE//2,
    widget_font_color = (52, 168, 235,42),
    widget_font = pygame_menu.font.FONT_NEVIS,
    widget_font_size = FONT_SIZE,
    scrollbar_color = (42,42,42),
    scrollbar_slider_color = (52, 168, 235)
)

form_menu = pygame_menu.Menu(H, W, 'Formation',
                             theme=form_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

form_opts = [
    (v['name'], (k,v['img-num'])) for k,v in FORM.items()
]
form_id = 0
team_id = 1


f1 = form_menu.add_selector('Team:  ', [('Team 1', 1), ('Team 2', 2)])
f2 = form_menu.add_selector('Formation:  ', form_opts)

form_menu.add_vertical_margin(40)
form_menu.add_button('Back', pygame_menu.events.BACK)
#################################


########### Main menu ###########

main_menu = pygame_menu.Menu(H, W, ' FIFA 42',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

#################################
