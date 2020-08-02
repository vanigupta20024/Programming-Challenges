from tkinter import *
import requests
import io
import random
from tkinter import ttk
from time import strftime
from tkinter import ttk
from PIL import ImageTk, Image


root = Tk()
root.geometry('1000x600+100+50')
root.title("Cryptographic Algorithms Application")

# ----------------- Partition -------------------#

left_pane = Frame(root, width = 200, height = 600, relief = SUNKEN)
left_pane.pack(side = LEFT)

main_frame = Frame(root, width = 800, height = 50, relief = SUNKEN, borderwidth = 10)
main_frame.pack()

main = Frame(root, width = 800, height = 400, relief = SUNKEN)
main.pack()

time_frame = Frame(root, width = 800, height = 30, relief = SUNKEN)
time_frame.pack(side = BOTTOM)

label = Label(main_frame, text = "A simple cryptography based application for encrypting and decrypting text.",
	 bd = 10, font = ('fixedsys', 20, 'bold'), wraplength = 500, anchor = CENTER, padx = 20, pady = 20)


def localtime():
	curr_time = strftime('%d - %m - %Y  %A  %H:%M:%S %p ') 
	t1 = Label(time_frame, text = curr_time, font = ('arial', 14, 'bold'), anchor = E)
	t1.after(1000, localtime)
	t1.grid(row = 1, column = 0, columnspan = 2)

def remove():

	label.config(text = "")
	for widget in main.winfo_children():
		widget.destroy()

def show():

	remove()
	label.config(text = "A simple cryptography based application for encrypting and decrypting text.")
	label.grid(row = 0, column = 0)
	localtime()


def caesar_cipher():

	remove()

	label.config(text = "Caesar Cipher")
	label.grid(row = 0, column = 0)

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	key_label = Label(main, text = "Enter key: ", font = ('fixedsys', 12, 'bold'))
	key_label.grid(row = 4, column = 0, padx = 20, pady = 30)

	list_key = ttk.Combobox(main)
	list_key['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
	list_key.current(0)
	list_key.grid(row = 5, column = 0)

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():
		new_text.delete('1.0', END)

		txt = text_box.get("1.0", END)
		key = int(list_key.get())
		enc_text = ""

		for index in range(len(txt)):

			if txt[index].isalpha():
				if txt[index].isupper():
					temp = (ord(txt[index]) - ord('A') + key) % 26 + ord('A')
					enc_text += chr(temp)

				elif txt[index].islower():
					temp = (ord(txt[index]) - ord('a') + key) % 26 + ord('a')
					enc_text += chr(temp)

			else:
				enc_text += txt[index]

		new_text.insert(1.0, enc_text)


	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = int(list_key.get())
		dec_text = ""

		for index in range(len(txt)):

			if txt[index].isalpha():
				if txt[index].isupper():
					temp = (ord(txt[index]) - ord('A') - key)
					if temp < 0:
						temp += 26
					temp += ord('A')
					dec_text += chr(temp)

				elif txt[index].islower():
					temp = (ord(txt[index]) - ord('a') - key)
					if temp < 0:
						temp += 26
					temp += ord('a')
					dec_text += chr(temp)

			else:
				dec_text += txt[index]

		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)

	localtime()

def homophonic_cipher():

	remove()
	label.config(text = "Homophonic Cipher")
	label.grid(row = 0, column = 0)

	key_table = {'A':'D9', 'B':'X', 'C':'S', 'D':'F', 'E':'Z721', 'F':'E', 'G':'H', 'H':'C', 'I':'V3',
	'J':'I', 'K':'T', 'L':'P', 'M':'G', 'N':'A5', 'O':'Q0', 'P':'L', 'Q':'K', 'R':'J', 'S':'R4', 'T':'6U', 
	'U':'O', 'V':'W', 'W':'M', 'X':'Y', 'Y':'B', 'Z':'N', 'a':'d(', 'b':'x', 'c': 's', 'd':'f', 'e':'z&@!', 
	'f':'e', 'g':'h', 'h':'c', 'i':'v#', 'j':'i', 'k':'t', 'l':'p', 'm':'g', 'n':'a%', 'o':'q)', 'p':'l', 
	'q':'k', 'r':'j','s':'r$', 't':'^u', 'u':'o', 'v':'w', 'w':'m', 'x':'y', 'y':'b', 'z':'n'}

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 20, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 20, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		enc_text = ""

		for item in txt:
			if item in key_table:
				enc_text += random.choice(key_table[item])
			else:
				enc_text += item

		new_text.insert(1.0, enc_text)
    	
	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		dec_text = ""		
		flag = 1
		words = txt.split(" ")

		lst = []
		for item in words:
			lst += item + " "

		for letter in lst:
			if letter == " ":
				dec_text += " "
			else:
				for item in key_table:
					flag = 1
					if letter in key_table[item]:
						dec_text += item
						flag = 0
						break
				if flag == 1:
					dec_text += letter

		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)

	localtime()

def vignere_cipher():

	remove()
	label.config(text = "Vignere Cipher")
	label.grid(row = 0, column = 0)

	text_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	text_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	scroll_text = ttk.Scrollbar(main, orient = VERTICAL)
	text_box = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text.set)
	text_box.grid(row = 1, column = 0, padx = 10, pady = 10)
	scroll_text.config(command = text_box.yview)
	scroll_text.grid(row = 1, column = 1, sticky = 'NS')

	key_label = Label(main, text = "Enter text: ", font = ('fixedsys', 12, 'bold'))
	key_label.grid(row = 2, column = 0)

	key_text = Entry(main, width = 40)
	key_text.grid(row = 3, column = 0, padx = 10, pady = 10)	

	scroll_text2 = ttk.Scrollbar(main, orient = VERTICAL)
	new_text = Text(main, height = 13, width = 40, pady = 10, yscrollcommand = scroll_text2.set)
	new_text.grid(row = 1, column = 2, columnspan = 2)
	scroll_text2.config(command = new_text.yview)
	scroll_text2.grid(row = 1, column = 4, sticky = 'NS')

	def encrypt():

		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		enc_text = ""	

		if len(key) > len(txt):
			key = key[: len(key) - len(txt) - 1]
		elif len(key) < len(txt):
			key = (key * ((len(txt) // len(key)) + 1))[:len(txt)]

		for i in range(len(txt)):
			if txt[i].isupper(): 
				v = 'A'
			elif txt[i].islower(): 
				v = 'a'
			else:
				enc_text += txt[i]
				continue

			enc_text += (chr(((ord(txt[i]) - 2 * ord(v) + ord(key[i])) % 26) + ord(v)))

		new_text.insert(1.0, enc_text)

	enc = Button(main, text = "Encrypt", bd = 10, width = 10, command = encrypt)
	enc.grid(row = 0, column = 2, padx = 20, pady = 10)

	def decrypt():
	
		new_text.delete('1.0', END)
		txt = text_box.get("1.0", END)
		key = key_text.get()
		dec_text = ""

		if len(key) > len(txt):
			key = key[: len(key) - len(txt) - 1]
		elif len(key) < len(txt):
			key = (key * ((len(txt) // len(key)) + 1))[:len(txt)]

		for i in range(len(txt)):
			if txt[i].isupper(): 
				v = 'A'
			elif txt[i].islower(): 
				v = 'a'
			else:
				dec_text += txt[i]
				continue

			s = ord(txt[i]) - ord(key[i])
			if s < 0: 
				s += 26

			dec_text += chr(s + ord(v))
		
		new_text.insert(1.0, dec_text)

	dec = Button(main, text = "Decrypt", bd = 10, width = 10, command = decrypt)
	dec.grid(row = 0, column = 3, padx = 10, pady = 10)	

	localtime()

# ----------------- Home Screen -------------------#

show()

# ----------------- Pane buttons -------------------#

home_button = Button(left_pane, padx = 20, bd = 10, text = 'Home', width = 20, height = 3, command = show)
home_button.grid(row = 0, column = 0)

caesar = Button(left_pane, padx = 20, bd = 10, text = 'Caesar Cipher', width = 20, height = 3, command = caesar_cipher)
caesar.grid(row = 1, column = 0)

homophonic = Button(left_pane, padx = 20, bd = 10, text = 'Homophonic Cipher', width = 20, height = 3, command = homophonic_cipher)
homophonic.grid(row = 2, column = 0)

vignere = Button(left_pane, padx = 20, bd = 10, text = 'Vignere Cipher', width = 20, height = 3, command = vignere_cipher)
vignere.grid(row = 3, column = 0)

C1 = Button(left_pane, padx = 20, bd = 10, text = 'Cipher 1', width = 20, height = 3)
C1.grid(row = 4, column = 0)

C2 = Button(left_pane, padx = 20, bd = 10, text = 'Cipher 2', width = 20, height = 3)
C2.grid(row = 5, column = 0)

C3 = Button(left_pane, padx = 20, bd = 10, text = 'Cipher 3', width = 20, height = 3)
C3.grid(row = 6, column = 0)

C4 = Button(left_pane, padx = 20, bd = 10, text = 'Cipher 4', width = 20, height = 3)
C4.grid(row = 7, column = 0)



root.mainloop()
