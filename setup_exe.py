import os
from distutils.core import setup
import py2exe
import PIL
import tkinter

Mydata_files = []
for files in os.listdir('./images/'):
    file = './images/' + files
    if os.path.isfile(file): # skip directories
        f2 = 'images', [file]
        Mydata_files.append(f2)

setup(
    windows=['eyescalc.py'],
    data_files = Mydata_files,
    options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "excludes": ["email"]
                }
        }
)
