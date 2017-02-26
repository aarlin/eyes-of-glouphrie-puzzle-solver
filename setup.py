application_title = "Eyes of Glouphrie Calculator"
main_python_file = "eyescalc.py"

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includefiles = ["images/"]
packages = ["PIL"]

setup(
        name = application_title,
        version = "1.0",
        description = "First run",
        options = {"build_exe" : {"include_files" : includefiles, "packages" : packages }},
        executables = [Executable(main_python_file, base = base)])
