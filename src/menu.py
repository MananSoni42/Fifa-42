"""
Defines the game menu (written using pygame-menu)
"""

from pygame import mixer
import pygame_menu
from settings import *
from const import FORM
from game import Game

MAX_CHAR = 50
V_PAD = 20


# Init sound
engine = pygame_menu.sound.Sound()
engine.set_sound(pygame_menu.sound.SOUND_TYPE_CLICK_MOUSE, CLICK)
mixer.init(44100, -16, 2, 2048)
menu_music = mixer.Sound(MENU_MUSIC)

# Theme
menu_bg = pygame_menu.baseimage.BaseImage(  # load background image
    image_path=MENU_BG,
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
)

custom_theme = pygame_menu.themes.Theme(
    background_color=menu_bg,  # Add background image
    focus_background_color=(255, 255, 255, 128),
    menubar_close_button=False,
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
    title_background_color=(52, 168, 235),
    title_shadow=True,
    title_shadow_offset=5,
    title_font=FONT_8BIT,
    title_font_size=3*FONT_SIZE//2,
    widget_font_color=(52, 168, 235),
    widget_font=FONT_NEVIS,
    widget_font_size=FONT_SIZE,
    scrollbar_color=(42, 42, 42),
    scrollbar_slider_color=(52, 168, 235)
)


class Menu:
    """
    The game menu. Configure the game the way you want to
    """

    def __init__(self, win, team1, team2, sound, diff, cam):
        self.win = win
        self.team1 = team1
        self.team2 = team2
        self.sound = sound
        self.difficulty = diff
        self.cam = cam

    def create_about_menu(self):
        about_menu = pygame_menu.Menu(H, W, ' About',
                                      theme=custom_theme,
                                      mouse_motion_selection=True,
                                      mouse_visible=True)

        about_menu.add_label('Written by:', max_char=MAX_CHAR)
        about_menu.add_label('Manan Soni')
        about_menu.add_vertical_margin(V_PAD)
        about_menu.add_label('More info at:', max_char=MAX_CHAR)
        about_menu.add_label('github.com/MananSoni42/Fifa-42 ', max_char=MAX_CHAR)
        about_menu.add_vertical_margin(V_PAD)
        about_menu.add_button('Back', pygame_menu.events.BACK)
        return about_menu

    def create_instr_menu(self):
        instr_menu = pygame_menu.Menu(H, W, ' Instructions',
                                      theme=custom_theme,
                                      mouse_motion_selection=True,
                                      mouse_visible=True,
                                      # columns=2,
                                      # rows=21,
                                      )

        instr_menu.add_label('Basics')
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            'This is an 11 v 11 Football game where you play against the computer.', max_char=MAX_CHAR)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            'Your play as Team 1 and the computer is Team 2', max_char=MAX_CHAR)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            'You control the player marked by a red dot on top of him', max_char=MAX_CHAR)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            'Running into opponents causes both of you to be thrown back and lose possession of the ball', max_char=MAX_CHAR)
        instr_menu.add_vertical_margin(3*V_PAD)
        instr_menu.add_label('Settings')
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            'Team colors can be changed from the settings', max_char=MAX_CHAR)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            'You can also choose your own formation', max_char=MAX_CHAR)
        instr_menu.add_vertical_margin(3*V_PAD)
        instr_menu.add_label('Controls')
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            '< ^ v >                   Move the player', align=pygame_menu.locals.ALIGN_LEFT)
        instr_menu.add_label(
            '(arrow keys)', align=pygame_menu.locals.ALIGN_LEFT)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label('Shoot the ball')
        instr_menu.add_image(CONTROLS_IMG, align=pygame_menu.locals.ALIGN_LEFT)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            'SPACE                Toggle if your players maintain', align=pygame_menu.locals.ALIGN_LEFT)
        instr_menu.add_label(
            '                           the team\'s formation', align=pygame_menu.locals.ALIGN_LEFT)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label(
            'ESC                     Bring up / collapse Pause menu', align=pygame_menu.locals.ALIGN_LEFT)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_label('BACKSPACE        Exit to main menu',
                             align=pygame_menu.locals.ALIGN_LEFT)
        instr_menu.add_vertical_margin(V_PAD)
        instr_menu.add_button('Back', pygame_menu.events.BACK)
        return instr_menu

    def create_sett_menu(self):
        sett_menu = pygame_menu.Menu(H, W, ' Settings',
                                     theme=custom_theme,
                                     mouse_motion_selection=True,
                                     mouse_visible=True)

        colors = [
            ('BLACK', (0, 0, 0)),
            ('RED', (255, 0, 0)),
            ('ORANGE', (255, 165, 0)),
            ('YELLOW', (255, 255, 0)),
            ('PURPLE', (128, 0, 128)),
            ('NAVY', (0, 0, 128)),
            ('BLUE', (0, 0, 255)),
            ('CYAN', (0, 255, 255))
        ]

        s1 = sett_menu.add_selector(
            'Team 1 color:', colors, default=2, font_color=(255, 255, 255))
        s1.change = lambda col: self.color_change(
            s1, col, self.team1)  # set team 1's color
        s1.set_background_color((255, 165, 0))

        s2 = sett_menu.add_selector(
            'Team 2 color:', colors, default=6, font_color=(255, 255, 255))
        s2.change = lambda col: self.color_change(
            s2, col, self.team2)  # Set team 2's color
        s2.set_background_color((0, 0, 255))

        def set_difficulty(name, diff):
            self.difficulty = diff/100

        def set_camera(name,cam):
            self.cam = cam

        sett_menu.add_selector(
            'Camera angle', [('default', 'default'), ('full', 'full'), ('zoomed', 'zoomed')],
            default=0, onchange=set_camera)
        sett_menu.add_vertical_margin(V_PAD)

        sett_menu.add_selector(
            'Difficulty', [(f'{i}%', i) for i in range(10,100+10,10)], default=5, onchange=set_difficulty)

        sett_menu.add_selector(
            'Sound', [('ON', True), ('OFF', False)], default=int(self.sound), onchange=self.set_menu_sound)
        sett_menu.add_vertical_margin(V_PAD)

        sett_menu.add_button('Back', pygame_menu.events.BACK)
        return sett_menu

    def create_form_menu(self):
        bc = custom_theme.background_color
        # Temporarily set the background to be transparent
        custom_theme.background_color = (42, 42, 42, 0)

        form_menu = pygame_menu.Menu(H, W, 'Formation',
                                     theme=custom_theme,
                                     mouse_motion_selection=True,
                                     mouse_visible=True)

        form_opts = [  # Get formation options from the settings (FORM)
            (v['name'], (k, v['img-num'])) for k, v in FORM.items()
        ]

        self.selected_team = 1
        self.selected_formation = {
            1: ('default', 0),
            2: ('balanced-1', 1),
        }

        form_menu.add_selector('Team 1 formation:  ', form_opts,
                               default=self.selected_formation[1][1], onchange=lambda name, id: self.set_form(id, team_id=1))
        form_menu.add_selector('Team 2 formation:  ', form_opts,
                               default=self.selected_formation[2][1], onchange=lambda name, id: self.set_form(id, team_id=2))

        form_menu.add_vertical_margin(V_PAD)
        form_menu.add_button('Back', pygame_menu.events.BACK)

        custom_theme.background_color = bc  # Change backgroung back to image
        return form_menu

    def create_pract_menu(self):
        practice_menu = pygame_menu.Menu(H, W, 'Formation',
                                         theme=custom_theme,
                                         mouse_motion_selection=True,
                                         mouse_visible=True)
        return practice_menu

    def create_main_menu(self, play, practice):
        main_menu = pygame_menu.Menu(H, W, ' FIFA 42',
                                     theme=custom_theme,
                                     mouse_motion_selection=True,
                                     mouse_visible=True)
        # Apply on menu and all sub-menus
        main_menu.set_sound(engine, recursive=True)

        main_menu.add_button('Play', lambda: play(self.win, self.team1, self.team2, sound=self.sound, difficulty=self.difficulty, cam=self.cam))
        main_menu.add_button('Practice', practice)
        main_menu.add_button('Instructions', self.create_instr_menu())
        main_menu.add_button('Choose formation', self.create_form_menu())
        main_menu.add_button('Settings', self.create_sett_menu())
        main_menu.add_button('About', self.create_about_menu())
        main_menu.add_button(
            'Quit', pygame_menu.events.EXIT)  # Add exit button
        self.main_menu = main_menu

    # Change color of widget and corresponding team
    def color_change(self, widget, col, team):
        widget.set_background_color(col)
        team.color = col

    def set_form(self, form, team_id):  # Change team 1's formation and widget's background
        self.selected_team = team_id
        self.selected_formation[self.selected_team] = form

        self.team1.formation = self.selected_formation[1][0]
        self.team2.formation = self.selected_formation[2][0]

    def set_menu_sound(self, name, val):
        if self.sound and not val:
            mixer.pause()
        elif not self.sound and val:
            mixer.unpause()
        self.sound = val

    def draw_bg(self):
        if self.main_menu.get_current().get_title() == 'Formation':
            dummy_game = Game(self.team1, self.team2, sound=False, cam='full')
            dummy_game.draw(self.win, hints=False)

    def start(self):
        """
        Display the game menu
        """
        if self.sound:
            mixer.stop()
            menu_music.play(-1)
        self.main_menu.mainloop(self.win, bgfun=self.draw_bg)  # Show the menu

def play_with_menu(win, team1, team2, play, practice, sound, difficulty, cam):
    game_menu = Menu(win, team1, team2, sound=sound, diff=difficulty/100, cam=cam)
    game_menu.create_main_menu(play, practice)
    return game_menu
