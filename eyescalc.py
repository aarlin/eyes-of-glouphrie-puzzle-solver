# EYES OF GLOUPHRIE CALCULATOR

# LIGHT GREEN OUTLINE TO BOX OF IMAGE WHERE IT IS MORE THAN 0
# CHECK BUTTON FOR SOLUTION CHECKING
# USE SPINBOX
# TURN .PY TO .EXE


# r = 0
# for c in colours:
#     Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
#     Entry(bg=c, relief=SUNKEN,width=10).grid(row=r,column=1)
#     r = r + 1


# from tkinter import *
# Python 3.5 import line above

from Tkinter import *	
from PIL import Image, ImageTk

colors = ['Red','Orange','Yellow','Green','Blue', 'Indigo', 'Violet']
shapes = ['circle', 'triangle', 'square', 'pentagon']

root = Tk()
root.title("Eyes of Glouphrie Calculator")

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="grey23", width=1500, height=1500)
canvas.pack()

rows_count = 0
columns_count = 0
images = []

# IMAGES AND SPIN BOXES
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

		columns_count += 1

	rows_count += 1
	columns_count = 0

	for c in colors:
		shapecount = Spinbox(canvas, from_= 0, to = 10, width = 15)
		# shapecount = Spinbox(canvas, from_= 0, to = 10, width = 15, background = "white")
		shapecount.grid(row = rows_count, column = columns_count, padx = 5, pady = 5)

		columns_count += 1

	rows_count += 1
	columns_count = 0

# LOCK SCREENS (AMOUNTS TO BE FOUND)

#for i in range(4):
# Label(canvas, text = "First Lock").grid(rows = rows_count, column = 3)
# Entry(canvas).grid(rows = rows_count, column = 4)
# rows_count += 1

# BUTTONS
for i in range(7):
	if i == 3:
		check_button = Button(canvas, text = "Check inventory")	# CHECK BUTTON
		check_button.grid(row = rows_count, column = i, padx = 5, pady = 5, sticky = N+W+S+E)
		# command=callback

	if i == 4:
		reset_button = Button(canvas, text = "Reset values") 	# RESET BUTTON 
		reset_button.grid(row = rows_count, column = i, padx = 5, pady = 5, sticky = N+W+S+E)

	# if i == 4:
	# 	quit_button = Button(canvas, text = "Quit program") 	# QUIT BUTTON
	# 	quit_button.grid(row = rows_count, column = i, padx = 5, pady = 5, sticky = N+W+S+E)


root.mainloop()