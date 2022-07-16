from curses import window
from distutils.core import setup
import py2exe

setup(windows=[{'script': 'main.py', 'icon_resources': [(1, 'assets/icon.ico')]}]),