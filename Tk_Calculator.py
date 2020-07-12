# Tk tutorial

# from tkinter import everything
from tkinter import *

root = Tk()

# to change title appearing at top
root.title("Simple Calculator")

# input box without default text
e = Entry(root, width = 40, borderwidth = 10)
e.grid(row = 0, column = 0, columnspan = 3)

def onClick(number):
	save_curr = e.get()
	e.delete(0, END)
	e.insert(0, str(save_curr) + str(number))
	
# clears the input box
def onClear():
	e.delete(0, END)

# to delete a single entry
def backspace():
	e.delete(0)

# add function
def onAdd():
	global first 
	global operation
	first = e.get()
	operation = "add"
	e.delete(0, END)

def onSub():
	global first 
	global operation
	first = e.get()
	operation = "sub"
	e.delete(0, END)

def onMul():
	global first 
	global operation
	first = e.get()
	operation = "mul"
	e.delete(0, END)

def onDiv():
	global first 
	global operation
	first = e.get()
	operation = "div"
	e.delete(0, END)

def onMod():
	global first 
	global operation
	first = e.get()
	operation = "mod"
	e.delete(0, END)

def onEqual():
	sn = e.get()
	e.delete(0, END)
	if operation == "add":
		e.insert(0, int(first) + int(sn))
	if operation == "sub":
		e.insert(0, int(first) - int(sn))
	if operation == "mul":
		e.insert(0, int(first) * int(sn))
	if operation == "div":
		if int(sn) == 0:
			e.insert(0, "Not Defined")
			return
		if int(first) == 0:
			e.insert(0, 0)
			return
		e.insert(0, int(first) / int(sn))
	if operation == "mod":
		if int(sn) == 0:
			e.insert(0, "Not Defined")
			return
		if int(first) == 0:
			e.insert(0, 0)
			return
		e.insert(0, int(first) % int(sn))

# define buttons
b1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda : onClick(1))
b2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda : onClick(2))
b3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda : onClick(3))
b4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda : onClick(4))
b5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda : onClick(5))
b6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda : onClick(6))
b7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda : onClick(7))
b8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda : onClick(8))
b9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda : onClick(9))
b0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda : onClick(0))
b_add = Button(root, text = "+", padx = 39, pady = 20, command = onAdd)
b_sub = Button(root, text = "-", padx = 41, pady = 20, command = onSub)
b_mul = Button(root, text = "*", padx = 40, pady = 20, command = onMul)
b_div = Button(root, text = "/", padx = 40, pady = 20, command = onDiv)
b_mod = Button(root, text = "%", padx = 40, pady = 20, command = onMod)
b_equal = Button(root, text = "=", padx = 39, pady = 20, command = onEqual)
b_clear = Button(root, text = "clear", padx = 30, pady = 20, command = onClear)
back = Button(root, text = "<=", padx = 35, pady = 20, command = backspace)


# displaying buttons on screen
b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)
b0.grid(row = 4, column = 1)

b_add.grid(row = 4, column = 0)
b_sub.grid(row = 5, column = 2)
b_mul.grid(row = 6, column = 0)
b_div.grid(row = 6, column = 1)
b_mod.grid(row = 6, column = 2)
b_equal.grid(row = 4, column = 2)
b_clear.grid(row = 5, column = 1)
back.grid(row = 5, column = 0)

root.mainloop()
