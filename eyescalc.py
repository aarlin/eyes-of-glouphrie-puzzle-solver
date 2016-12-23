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
colors = ['Red','Orange','Yellow','Green','Blue', 'Indigo', 'Violet']
shapes = ['circle', 'triangle', 'square', 'pentagon']


# r = 0
# for c in colours:
#     Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
#     Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
#     r = r + 1

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="light blue", width=1500, height=1500)
canvas.pack()

image_count = 0
rows_count = -1
columns_count = 0

for s in shapes:
	rows_count += 1
   	columns_count = 0
	for c in colors:
		filepath = './images/'
		filepath += c
		filepath += '_'
		filepath += s
		filepath += '.png'
		print filepath

		image_count += 1
        im = Image.open(filepath)
        resized = im.resize((50, 50), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        myvar = Label(canvas, image=tkimage)
        myvar.image = tkimage
        myvar.grid(row = rows_count, column = columns_count)
        print rows_count
        print columns_count
        columns_count += 1

root.mainloop()