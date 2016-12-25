# EYES OF GLOUPHRIE CALCULATOR

# LIGHT GREEN OUTLINE TO BOX OF IMAGE WHERE IT IS MORE THAN 0
# TURN .PY TO .EXE
# HELP BUTTON ?
# CLARIFY ON LOCK 
# HOW TO DISPLAY SOLUTION
# HOW TO GRAB ALL VALUES AND ASSIGN THEM THE CORRECT SHAPE+COLOR VALUE?
# validatecommand for SpinBox
# command for button
# selection_clear

# THIS IS FOR CHECKING IF CURRENT INVENTORY HAS SOLUTION
# WHAT IF PERSON HAS ITEMS THAT CAN BE CHANGED TO A SOLUTION?

try:
    # Python 3.x
    from tkinter import * 
except ImportError:
    # Python 2.x
    from Tkinter import *
from PIL import Image, ImageTk

colors = ['Red','Orange','Yellow','Green','Blue', 'Indigo', 'Violet']
shapes = ['circle', 'triangle', 'square', 'pentagon']
values = [1, 2, 3, 4, 5, 6, 7, 			# CORRESPONDING TO RED CIRCLE, ORANGE CIRCLE, YELLOW CIRCLE, ETC. IN ORDER
			3, 6, 9, 12, 15, 18, 21, 
			4, 8, 12, 16, 20, 24, 28,
			5, 10, 15, 20, 25, 30, 35]

def reset():
	# ITERATE THROUGH THE DATA STUCTURE HOLDING ALL SPINBOXES AND ENTRY
	# RESET ALL VALUES THEY HOLD
	for widgets in spin_widgets:
		widgets.delete(0, END)
	for widgets in entry_widgets:
		widgets.delete(0, END)

def check():
	# CHECK ALL SPINBOXES AND SEES IF WE HAVE SHAPES THAT SOLVE EACH LOCK
	print "check"


root = Tk()
root.title("Eyes of Glouphrie Calculator")

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="grey23", width=1500, height=2000)
canvas.pack()

rows_count = 0
columns_count = 0
spin_widgets = []
entry_widgets = []

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
		shapecount = Spinbox(canvas, from_= 0, to = 50, width = 15)
		# shapecount = Spinbox(canvas, from_= 0, to = 10, width = 15, background = "white")
		shapecount.grid(row = rows_count, column = columns_count, padx = 5, pady = 5)
		spin_widgets.append(shapecount)

		columns_count += 1

	rows_count += 1
	columns_count = 0


# LABEL FOR LOCKS
first_lock = Label(canvas, text = "First Lock:		")
first_lock.grid(row = rows_count, column = 1, sticky = E)

first_entry = Entry(canvas, width = 10)
first_entry.grid(row = rows_count, column = 2, pady = 5, sticky = W+E)

rows_count += 1

second_lock = Label(canvas, text = "Second Lock:	")
second_lock.grid(row = rows_count, column = 1, sticky = E)

second_entry = Entry(canvas, width = 10)
second_entry.grid(row = rows_count, column = 2, pady = 5, sticky = W+E)

rows_count += 1

third_lock = Label(canvas, text = "Third Lock:	")
third_lock.grid(row = rows_count, column = 1, sticky = E)

third_entry = Entry(canvas, width = 10)
third_entry.grid(row = rows_count, column = 2, pady = 5, sticky = W+E)

rows_count += 1

fourth_lock = Label(canvas, text = "Fourth Lock:	")
fourth_lock.grid(row = rows_count, column = 1, sticky = E)

fourth_entry = Entry(canvas, width = 10)
fourth_entry.grid(row = rows_count, column = 2, pady = 5, sticky = W+E)

entry_widgets.append(first_entry)
entry_widgets.append(second_entry)
entry_widgets.append(third_entry)
entry_widgets.append(fourth_entry)

# BUTTONS

rows_count -= 2		# MOVE BACK TO ALIGN BUTTONS TO BE ADDED

reset_button = Button(canvas, text = "Reset values", command = reset) 	# RESET BUTTON 
reset_button.grid(row = rows_count, column = 4, pady = 5, sticky = N+W+S+E)

check_button = Button(canvas, text = "Check inventory", command = check)	# CHECK BUTTON
check_button.grid(row = rows_count + 1, column = 4, pady = 5, sticky = N+W+S+E)

# quit_button = Button(canvas, text = "Quit program") 	# QUIT BUTTON
# quit_button.grid(row = rows_count + 2, column = 4, pady = 5, sticky = N+W+S+E)

root.mainloop()