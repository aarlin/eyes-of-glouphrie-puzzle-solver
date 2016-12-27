# EYES OF GLOUPHRIE CALCULATOR

# LIGHT GREEN OUTLINE TO BOX OF IMAGE WHERE IT IS MORE THAN 0
# TURN .PY TO .EXE
# HELP BUTTON ?
# CLARIFY ON LOCK 
# HOW TO DISPLAY SOLUTION
# HOW TO GRAB ALL VALUES AND ASSIGN THEM THE CORRECT SHAPE+COLOR VALUE?
# validatecommand for SpinBox

# THIS IS FOR CHECKING IF CURRENT INVENTORY HAS SOLUTION
# WHAT IF PERSON HAS ITEMS THAT CAN BE CHANGED TO A SOLUTION?
# USE OF TUPLES, LISTS, DICTIONARY

# IM SURE THIS CAN BE DONE FOR SIMPLY

try:
    # Python 2.x
    from Tkinter import * 
except ImportError:
	# Python 3.x
    from tkinter import *
from PIL import Image, ImageTk

colors = ['Red','Orange','Yellow','Green','Blue', 'Indigo', 'Violet']
shapes = ['circle', 'triangle', 'square', 'pentagon']
values = [('Red_circle',1), 	('Orange_circle',2),	('Yellow_circle',3), 	('Green_circle',4),
		('Blue_circle',5), 		('Indigo_circle',6), 	('Violet_circle',7),
		('Red_triangle',3), 	('Orange_triangle',6), 	('Yellow_triangle',9), 	('Green_triangle',12), 
		('Blue_triangle',15), 	('Indigo_triangle',18), ('Violet_triangle',21),
		('Red_square',4), 		('Orange_square',8), 	('Yellow_square',12), 	('Green_square',16), 
		('Blue_square',20), 	('Indigo_square',24), 	('Violet_square',28), 
		('Red_pentagon',5), 	('Orange_pentagon',10), ('Yellow_pentagon',15), ('Green_pentagon',20), 
		('Blue_pentagon',25), 	('Indigo_pentagon',30), ('Violet_pentagon',35)]
dictvalues = dict(values)

print dictvalues['Red_circle']

def reset():
	# ITERATE THROUGH THE DATA STUCTURE HOLDING ALL SPINBOXES AND ENTRY
	# RESET ALL VALUES THEY HOLD
	for widgets in spin_widgets:
		widgets.delete(0, END)		# CLEARS WIDGET VALUE
		widgets.insert(0, 0)		# RESET TO 0
	for widgets in entry_widgets:
		widgets.delete(0, END)

def check():
	for index, widgets in enumerate(spin_widgets):
		spin_counts[index] = widgets.get()			# GET SPIN BOX VALUES AND STORE INTO INDEX OF LIST OF COUNTERS
	for index, widgets in enumerate(entry_widgets):
		entry_counts[index] = widgets.get()


	i = 0		# ITERATE THROUGH SPIN COUNTS
	j = 0		# ITERATE THROUGH ENTRY COUNTS
	for s in shapes:
		for c in colors:
			key = c + '_' + s
			shape_counts[key] = spin_counts[i]	# STORE SHAPE COUNT FROM SPIN BOX ENTRY INTO DICTIONARY
			i += 1

	for entry in entry_counts:	# GO THROUGH THE LOCKS AND TRY TO FIND SOLUTION FROM SHAPE COUNTS
		for s in shapes:
			for c in colors:
				key = c + '_' + s
				if shape_counts[key] > 0:
					if entry != "":
						if int(entry) == int(dictvalues[key]):
							print("ENTRY: ")
							print entry
							print key
							shape_counts[key] = int(shape_counts[key]) - 1



	# SO I HAVE THE COUNT OF EVERY SPIN BOX STORED INTO COUNT LISTS
	# NOW I NEED TO CHECK IF THEY HAVE SOLUTION...
	# I NEED TO MULTIPLY 
	# WHAT IF I HAVE TWO LISTS OF TUPLES...
	# ITERATE THROUGH SHAPES AND COLORS NESTED FOR LOOP
	# CALL LIST OF TUPLES THROUGH THAT FOR LOOP...


	# CHECK ALL SPINBOXES AND SEES IF WE HAVE SHAPES THAT SOLVE EACH LOCK

	# OKAY, RATHER THAN THAT. WE USE A LIST OF TUPLES FOR SHAPE VALUES
	# AND A DICTIONARY FOR THE SHAPE COUNTS
	# NOW WE NEED TO GO THROUGH THE LOCKS 
	# FIRST LOCK = 1 SHAPE NEEDED
	# SECOND LOCK = 1 SHAPE NEEDED
	# THIRD LOCK = 2 SHAPES NEEDED
	# FOURTH LOCK = 3 SHAPES NEEDED


root = Tk()
root.title("Eyes of Glouphrie Calculator")

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg = "grey23", width = 1500, height = 2000)
canvas.pack()

rows_count = 0
columns_count = 0
spin_widgets = []		# STRUCTURE TO HOLD ALL SPIN BOX WIDGETS
entry_widgets = []		# STRUCTURE TO HOLD ALL ENTRY WIDGETS
spin_counts = [0] * 28	# LIST OF COUNTS BASED ON SPIN BOXES
entry_counts = [0] * 4	# VALUES OF THE LOCKS (FIRST TO FOURTH)
shape_counts = {'Red_circle':0, 'Orange_circle':0, 		'Yellow_circle':0,		'Green_circle':0,
			'Blue_circle':0, 	'Indigo_circle':0,  	'Violet_circle':0,
			'Red_triangle':0, 	'Orange_triangle':0, 	'Yellow_triangle':0,	'Green_triangle':0, 
			'Blue_triangle':0, 	'Indigo_triangle':0, 	'Violet_triangle':0,
			'Red_square':0, 	'Orange_square':0, 		'Yellow_square':0,		'Green_square':0, 
			'Blue_square':0, 	'Indigo_square':0, 		'Violet_square':0, 
			'Red_pentagon':0, 	'Orange_pentagon':0,	'Yellow_pentagon':0,	'Green_pentagon':0, 
			'Blue_pentagon':0, 	'Indigo_pentagon':0, 	'Violet_pentagon':0}

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