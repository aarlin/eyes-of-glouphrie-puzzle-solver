# EYES OF GLOUPHRIE CALCULATOR

# TURN .PY TO .EXE
# validatecommand for SpinBox

# THIS IS FOR CHECKING IF CURRENT INVENTORY HAS SOLUTION
# WHAT IF PERSON HAS ITEMS THAT CAN BE CHANGED TO A SOLUTION?
# USE OF TUPLES, LISTS, DICTIONARY

# TIE THE WIDGET WITH THE COLOR + SHAPE IN A DICTIONARY???

# HOW SHOULD I IMPLEMENT SOLUTION?
# SHOULD I GO IN ORDER... LETS SAY FIRST LOCK USES A RED CIRCLE
# THAT MEANS ITS TAKEN AWAY FROM THE SOLUTIONS OF SECOND, THIRD, FOURTH LOCKS

# COULD OF JUST ITERATED THROUGH DICTIONARY AND ADDED COUNTS, INSTEAD OF DOING SPIN_COUNT ARRAY

# THE PROGRAM DOESNT GIVE ALL COMBINATIONS OF SOLUTIONS
# RATHER IT TRIES TO SOLVE THE LOCKS IN ORDER AND DELETES THE SHAPE NEEDED FOR THAT LOCK
# THE SUBSEQUENT LOCKS DONT HAVE ACCESS TO THAT SHAPE ANYMORE
# WHAT IF THERE ARE MULTIPLE SOLUTIONS? THAT IS SOMETHING I HAVENT DECIDED UPON YET

# IF I ORDERED THE DICT, THEN I COULDVE USED BINARY SEARCH TO LOOK FOR 1 SHAPE FOR FIRST AND SECOND LOCK

# LETS SAY YOU DO RETURN ALL POSSIBLE SOLUTIONS TO THE USER WITHOUT TAKING AWAY SHAPES USED FROM OTHER LOCKS
# EHH, THAT MEANS THEY WILL HAVE TO FIND A SOLUTION OUT OF THE SOLUTIONS YOU GIVE THEM...
# NOT REALLY WANTED. THEY JUST WANT YOU TO TELL THEM THE ANSWER
# SO, WE DO TAKE AWAY A SHAPE AFTER ITS BEEN USED. THAT ALSO MEANS WE SHOULD STOP AFTER FINDING ONE SOLUTION
# OR ELSE THE SUBSEQUENT LOCKS WONT HAVE ANY SOLUTIONS BECAUSE A PREVIOUS LOCK MIGHT BE TAKING A BUNCH OF SHAPES

# HAVE MOUSEOVER OF COLOR AND SHAPE
# HAVE LOCK SHAPE #

#bad format of gui -- nothing instead of 0
#making rows to solution more visible
#mousing over shape and their names
#no solution = more visible that there are no solutions??
#py to exe
#didnt do OOP

try:
    # Python 2.x
    from Tkinter import * 
except ImportError:
	# Python 3.x
    from tkinter import *
from PIL import Image, ImageTk
from collections import Counter, OrderedDict

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

def help():
	top = Toplevel()
	top.title("Help")
	helpmsg = Message(top, width = 300, text = "1. Fill the number of shapes you currently have in your inventory to the corresponding entries. \n \
		\n 2. Fill the the lock values that are given when you click the machine. \n \
		\n 3. First lock corresponds to the initial lock that opens the other three locks. This has only one shape requirement \n \
		\n Second lock needs one shape, third lock needs two shapes, and fourth lock needs three shapes. \n \
		\n 4. Press the button named 'Check inventory' so the calculator can check for solutions. ")
	helpmsg.pack()

	dismiss = Button(top, text = "Dismiss", command = top.destroy)
	dismiss.pack()

def reset():
	# ITERATE THROUGH THE DATA STUCTURE HOLDING ALL SPINBOXES AND ENTRY
	# RESET ALL VALUES THEY HOLD
	for widgets in spin_widgets:
		widgets.delete(0, END)		# CLEARS WIDGET VALUE
		widgets.insert(0, 0)		# RESET TO 0
	for widgets in entry_widgets:
		widgets.delete(0, 0)

def check():
	for index, widgets in enumerate(spin_widgets):
		spin_counts[index] = widgets.get()			# GET SPIN BOX VALUES AND STORE INTO INDEX OF LIST OF COUNTERS
	for index, widgets in enumerate(entry_widgets):
		if widgets.get() == '':
			entry_counts[index] = 0
		else:
			entry_counts[index] = widgets.get()


	i = 0		# ITERATE THROUGH SPIN COUNTS
	for s in shapes:		
		for c in colors:
			key = c + '_' + s
			shape_counts[key] = spin_counts[i]	# STORE SHAPE COUNT FROM SPIN BOX ENTRY INTO DICTIONARY
			i += 1

	knapsack = []

	for key, value in shape_counts.items():		# THIS ISN'T ITERATING IN ORDER
		for i in range(int(value)):
			knapsack.append((key,dictvalues[key]))	# ADD SHAPE VALUE INTO KNAPSACK FOR THE NUMBER RETURNED BY SPIN BOX

	# FIRST LOCK = 1 SHAPE NEEDED
	# SECOND LOCK = 1 SHAPE NEEDED
	# THIRD LOCK = 2 SHAPES NEEDED
	# FOURTH LOCK = 3 SHAPES NEEDED

	final_solution = []
	try:
		first_solution = find_solution(knapsack, int(entry_counts[0]), 1)	# CHECK SOLUTION FOR FIRST LOCK
		second_solution = find_solution(knapsack, int(entry_counts[1]), 1)	# CHECK SOLUTION FOR SECOND LOCK
		third_solution = find_solution(knapsack, int(entry_counts[2]), 2)	# CHECK SOLUTION FOR THIRD LOCK
		fourth_solution = find_solution(knapsack, int(entry_counts[3]), 3)	# CHECK SOLUTION FOR FOURTH LOCK
	except ValueError:
		pass



	try:
		final_solution.append(first_solution)
		final_solution.append(second_solution)
		final_solution.append(third_solution)
		final_solution.append(fourth_solution)
	except UnboundLocalError:
		final_solution.append([])
	except TypeError:
		final_solution.append([])

	solution_popup_message(final_solution)		# DISPLAY A POPUP MESSAGE FOR SOLUTION TO LOCKS


def find_solution(knapsack, lock, shapes):
	# knapsack 	THE LIST OF TUPLES FOR SHAPE AND SHAPE VALUES TAKEN FROM THE SPIN BOXES
	# lock:		THE LOCK VALUE WE'RE LOOKING TO SOLVE
	# shapes: 	THE NUMBER OF SHAPES NEEDED TO UNLOCK THE LOCK

	solution = []

	if lock == "" or lock < 1:		# IF LOCK HAS NO VALUE OR IS LESS THAN 1, WE SHOULD RETURN AN EMPTY LIST
		return solution
	if len(knapsack) == 0:			# IF LENGTH OF KNAPSACK IS EMPTY, WE SHOULD ALSO RETURN AN EMPTY LIST
		return solution
	else:
		if shapes == 1:			
			# USING LINEAR SEARCHING O(n), RATHER THAN SORTING AND THEN BINARY SEARCH  O(nlogn + logn) = O(nlogn)
			for (shape, value) in knapsack:
				if value == lock:
					solution.append((shape, value))
					knapsack.remove((shape, value))
					return solution
		elif shapes == 2:
			knaplen = len(knapsack)
			for i in range(knaplen):
				for j in range(i + 1, knaplen):
					if knapsack[i][1] + knapsack[j][1] == lock:
						solution.append(knapsack[i])
						solution.append(knapsack[j])
						knapsack.remove(knapsack[j])	# REMOVE IN REVERSE ORDER BECAUSE LIST INDEX WILL BE PRESERVED
						knapsack.remove(knapsack[i])
						return solution

		elif shapes == 3:
			knaplen = len(knapsack)
			for i in range(knaplen):
				for j in range(i + 1, knaplen):
					for k in range(j + 1, knaplen):
						if knapsack[i][1] + knapsack[j][1] + knapsack[k][1] == lock:
							solution.append(knapsack[i])
							solution.append(knapsack[j])
							solution.append(knapsack[k])
							knapsack.remove(knapsack[k])	# REMOVE IN REVERSE ORDER BECAUSE LIST INDEX WILL BE PRESERVED
							knapsack.remove(knapsack[j])
							knapsack.remove(knapsack[i])
							return solution

def solution_popup_message(solution):
	rows_count = 1
	columns_count = 1

	top = Toplevel()
	top.title("Solution")

	first_lock = Label(top, text = "  First lock:		")
	first_lock.grid(row = 1, column = 0)

	second_lock = Label(top, text = "  Second lock:		")
	second_lock.grid(row = 3, column = 0)

	third_lock = Label(top, text = "  Third lock:		")
	third_lock.grid(row = 5, column = 0)

	fourth_lock = Label(top, text = "  Fourth lock:		")
	fourth_lock.grid(row = 7, column = 0)

	button = Button(top, text = "Dismiss", command = top.destroy)
	button.grid(row = 9, column = 1)

	for lock_solution in solution:			# GO THROUGH THE LIST OF SOLUTIONS AND ADD TO TOPLEVEL WINDOW
		for (key, value) in lock_solution:
			filepath = './images/'
			filepath += key		# ITERATE THROUGH THE SHAPES OF THE SAME COLOR
			filepath += '.png'

			im = Image.open(filepath)
			resized_image = im.resize((40, 40), Image.ANTIALIAS)
			shape_image = ImageTk.PhotoImage(resized_image)
			shape_label = Label(top, image = shape_image)
			shape_label.image = shape_image							# KEEP REFERENCE SO NO GARAGE COLLECTOR
			shape_label.grid(row = rows_count, column = columns_count, padx = 10, pady = 5, sticky = N+W+S+E)
			columns_count += 1
		rows_count += 2
		columns_count = 1

# START OF PROGRAM
# CREATING WINDOW
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
for s in shapes:				# GO THROUGH EACH SHAPE AND COLOR IN PREDETERMINED ORDER
	for c in colors:			
		filepath = './images/'	# GET THE IMAGE OF THIS SHAPE + COLOR
		filepath += c 				
		filepath += '_'
		filepath += s 			# ITERATE THROUGH THE SHAPES OF THE SAME COLOR
		filepath += '.png'

		im = Image.open(filepath)			# OPEN AND INSERT IMAGE TO LABEL
		resized_image = im.resize((40, 40), Image.ANTIALIAS)
		shape_image = ImageTk.PhotoImage(resized_image)
		shape_label = Label(canvas, image = shape_image)
		shape_label.image = shape_image							# KEEP REFERENCE SO NO GARAGE COLLECTOR
		shape_label.grid(row = rows_count, column = columns_count, pady = 5)

		columns_count += 1	# GO TO NEXT COLUMN FOR NEXT SHAPE

	rows_count += 1		# GO TO NEW ROW AFTER DOING ALL COLORS OF ONE SHAPE
	columns_count = 0	# RESET COLUMN TO 0 AFTER EACH SHAPE

	for c in colors:		# CREATE SPINBOXES UNDER EACH SHAPE
		shapecount = Spinbox(canvas, from_= 0, to = 50, width = 15)
		# shapecount = Spinbox(canvas, from_= 0, to = 10, width = 15, background = "white")
		shapecount.grid(row = rows_count, column = columns_count, padx = 5, pady = 5)
		spin_widgets.append(shapecount)

		columns_count += 1	# GO TO NEXT COLUMN AFTER EACH SHAPE

	rows_count += 1		# GO TO NEW ROW AFTER DOING ONE SHAPE
	columns_count = 0	# RESET COLUMN TO 0 AFTER EACH SHAPE

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

help_button = Button(canvas, text = "Help", command = help)	# HELP BUTTON
help_button.grid(row = rows_count, column = 4, pady = 5, sticky = N+W+S+E)

reset_button = Button(canvas, text = "Reset values", command = reset) 	# RESET BUTTON 
reset_button.grid(row = rows_count + 1, column = 4, pady = 5, sticky = N+W+S+E)

check_button = Button(canvas, text = "Check inventory", command = check)	# CHECK BUTTON
check_button.grid(row = rows_count + 2, column = 4, pady = 5, sticky = N+W+S+E)

root.mainloop()