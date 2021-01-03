import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import sys
from cx_Freeze import setup,Executable
from pathlib import Path
import pygame
import pygame_menu

osname = 'linux'

includefiles = [("teams","teams"),
    ("assets/fonts","assets/fonts"),
    ("assets/img","assets/img"),
    ("assets/img/running","assets/img/running"),
    ("assets/sounds","assets/sounds")]

includes = ['args', 'ball', 'camera', 'const',
            'game', 'menu', 'point', 'settings', 'stats']
excludes = ['PyInstaller']
packages = ['pygame', 'pygame_menu', 'screeninfo']

build_path = os.path.join(Path(__file__).resolve().parent, 'exec', osname)

setup(
    name = 'Fifa-42',
    version = '1.1',
    description = 'An 8-bit football game',
    author = 'Manan Soni',
    author_email = 'manansoni1399@gmail.com',
    options = {'build_exe': {'includes': includes,
                             'excludes': excludes,
                             'path': sys.path,
                             'packages': packages,
                             'include_files':includefiles,
                             'build_exe': build_path},
    },
    executables = [Executable('play.py', targetName='Fifa-42')]
)
