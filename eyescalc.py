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

canvas = Canvas(frame, bg="grey23", width=1500, height=1500)
canvas.pack()

rows_count = 0
columns_count = 0
images = []

for s in shapes:
	for c in colors:
		filepath = './images/'
		filepath += c 				
		filepath += '_'
		filepath += s 			# ITERATE THROUGH THE SHAPES OF THE SAME COLOR
		filepath += '.png'

		im = Image.open(filepath)
		resized_image = im.resize((40, 40), Image.ANTIALIAS)
		shape_image = ImageTk.PhotoImage(resized_image)
		shape_label = Label(canvas, image = shape_image)
		shape_label.image = shape_image							# KEEP REFERENCE SO NO GARAGE COLLECTOR
		shape_label.grid(row = rows_count, column = columns_count, pady = 5)
		print ("ROWS1: " + str(rows_count))
		print ("COLUMNS1: " + str(columns_count)) 

		columns_count += 1

	rows_count += 1
	columns_count = 0

	for c in colors:
		shapecount = Spinbox(canvas, from_= 0, to = 10, width = 15)
		# shapecount = Spinbox(canvas, from_= 0, to = 10, width = 15, background = "white")
		shapecount.grid(row = rows_count, column = columns_count, padx = 5, pady = 5)

		print ("ROWS2: " + str(rows_count))
		print ("COLUMNS2: " + str(columns_count)) 
		columns_count += 1

	rows_count += 1
	columns_count = 0

root.mainloop()