import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base='Win32GUI'


setup(name="Dankest_Dungeon",version='0.1', executables = [Executable('dankest_dungeon.py')])

