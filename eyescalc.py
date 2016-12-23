# EYES OF GLOUPHRIE CALCULATOR

# WHAT I WANT TO DO IS ARRANGE THE GUI IN A NEAT WAY
# TITLE, ALL SHAPES OF ONE IN A ROW
# THIS MEANS THAT IT STARTS FROM RED, ORANGE, YELLOW, GREEN, BLUE, INIDIGO, VIOLET
# WANT A INCREMENT DECREMENT BOX ABOVE THE IMAGE
# LIGHT GREEN OUTLINE TO BOX OF IMAGE WHERE IT IS MORE THAN 0
# CHECK BUTTON FOR SOLUTION CHECKING
# USE SPINBOX
# TURN .PY TO .EXE

# from tkinter import *
# Python 3.5 import line above

from Tkinter import *	
from PIL import Image, ImageTk


root = Tk()
root.title("Eyes of Glouphrie Calculator")
colours = ['red','green','orange','white','yellow','blue']

# r = 0
# for c in colours:
#     Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
#     Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
#     r = r + 1

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="./images/Blue_circle.png")
canvas.create_image(150, 150, image=photoimage)


root.mainloop()