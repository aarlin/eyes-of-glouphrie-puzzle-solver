import sys
from cx_Freeze import setup, Executable 		# Cx   FREE ICE

buildOptions = dict(include_files = ['Images/']) #folder,relative path. Use tuple like in the single file to set a absolute path.

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"


setup(
    name = "Eyes of Glouphrie Calculator",
    version = "1.0.0",
    description = "A tool to calculate solutions to the machine's lock for Eyes of Glouphrie quest",
    options = dict(build_exe = buildOptions),
    executables = [Executable("eyescalc.py", base = base)],
    )