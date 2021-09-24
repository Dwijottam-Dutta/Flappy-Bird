import sys
from cx_Freeze import setup, Executable
setup( name = "Flappy Bird+", version = "2.4",
       description = "Flappy Bird+ Game",
       executables = [Executable("main.py",
                                 base = "Win32GUI",
                                 icon="icon.ico")])
