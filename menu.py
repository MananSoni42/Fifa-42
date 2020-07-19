from settings import *
import pygame_menu
from const import FORM

MAX_CHAR = 50
V_PAD = 20

# Init sound
engine = pygame_menu.sound.Sound()
engine.set_sound(pygame_menu.sound.SOUND_TYPE_CLICK_MOUSE, CLICK)

# Custom theme
menu_bg = pygame_menu.baseimage.BaseImage( # load background image
    image_path=MENU_BG,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

custom_theme = pygame_menu.themes.Theme(
    background_color = menu_bg, # Add background image
    focus_background_color = (255,255,255,128),
    menubar_close_button = False,
    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
    title_background_color = (52, 168, 235),
    title_shadow = True,
    title_shadow_offset = 5,
    title_font = FONT_8BIT,
    title_font_size = 3*FONT_SIZE//2,
    widget_font_color = (52, 168, 235),
    widget_font = FONT_NEVIS,
    widget_font_size = FONT_SIZE,
    scrollbar_color = (42,42,42),
    scrollbar_slider_color = (52, 168, 235)
)

########### About ##############

about_menu = pygame_menu.Menu(H, W, ' About',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)
#about_menu.set_sound(engine, recursive=True)  # Apply on menu and all sub-menus

about_menu.add_label('Written by:', max_char=MAX_CHAR)
about_menu.add_label('* Manan Soni')
about_menu.add_label('* Ashutosh Jani')
about_menu.add_label('To know more visit: github.com/MananSoni42/Fifa-42 ', max_char=MAX_CHAR)
about_menu.add_vertical_margin(V_PAD)
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
# instr_menu.set_sound(engine, recursive=True)  # Apply on menu and all sub-menus

instr_menu.add_label('Basics')
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('This is an 11 v 11 Football game where you play against the computer.', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('Your play as Team 1 and the computer is Team 2', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('You control the player marked by a red dot on top of him', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('Running into opponents causes both of you to be thrown back and lose possession of the ball', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(3*V_PAD)
instr_menu.add_label('Settings')
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('Team colors can be changed from the settings', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('You can also choose your own formation', max_char=MAX_CHAR)
instr_menu.add_vertical_margin(3*V_PAD)
instr_menu.add_label('Controls')
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('< ^ v >                   Move the player', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_label('(arrow keys)', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('Shoot the ball')
instr_menu.add_image(CONTROLS_IMG, align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('SPACE                Toggle if your players maintain', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_label('                           the team\'s formation', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('ESC                     Bring up / collapse Pause menu', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_label('BACKSPACE        Exit to main menu', align=pygame_menu.locals.ALIGN_LEFT)
instr_menu.add_vertical_margin(V_PAD)
instr_menu.add_button('Back', pygame_menu.events.BACK)
#################################



########### Settings  ###########
sett_menu = pygame_menu.Menu(H, W, ' Settings',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)
# sett_menu.set_sound(engine, recursive=True)  # Apply on menu and all sub-menus

colors = [
    ('BLACK' , (0,0,0)),
    ('RED'   , (255,0,0)),
    ('ORANGE', (255,165,0)),
    ('YELLOW', (255,255,0)),
    ('PURPLE', (128,0,128)),
    ('NAVY'  , (0,0,128)),
    ('BLUE'  , (0,0,255)),
    ('CYAN'  , (0,255,255))
]

s1 = sett_menu.add_selector('Team 1 color:', colors, default=2, font_color=(255,255,255))
s1.set_background_color((255,165,0))

s2 = sett_menu.add_selector('Team 2 color:', colors, default=6, font_color=(255,255,255))
s2.set_background_color((0,0,255))

sett_menu.add_vertical_margin(V_PAD)
sett_menu.add_button('Back', pygame_menu.events.BACK)
#################################



########### Settings  ###########
bc = custom_theme.background_color
custom_theme.background_color = (42, 42, 42, 0) # Temporarily set the background to be transparent

form_menu = pygame_menu.Menu(H, W, 'Formation',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)

form_opts = [ # Get formation options from the settings (FORM)
    (v['name'], (k,v['img-num'])) for k,v in FORM.items()
]

selected_team = 1
selected_formation = {
    1: ('default', 0),
    2: ('balanced-1', 1),
}

f1 = form_menu.add_selector('Team 1 formation:  ', form_opts, default=selected_formation[1][1])
f2 = form_menu.add_selector('Team 2 formation:  ', form_opts, default=selected_formation[2][1])

form_menu.add_vertical_margin(V_PAD)
form_menu.add_button('Back', pygame_menu.events.BACK)

custom_theme.background_color = bc # Change backgroung back to image
#################################



########### Main menu ###########
main_menu = pygame_menu.Menu(H, W, ' FIFA 42',
                             theme=custom_theme,
                             mouse_motion_selection=True,
                             mouse_visible=True)
main_menu.set_sound(engine, recursive=True)  # Apply on menu and all sub-menus
#################################
