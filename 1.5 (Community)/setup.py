import sys
from cx_Freeze import setup, Executable
setup( name = "Flappy Bird+ ", version = "1.5",
       description = "Flappy Bird+ (Reality)Community",
       executables = [Executable("main.py",
                                 base = "Win32GUI",
                                 icon="icon.ico")])
