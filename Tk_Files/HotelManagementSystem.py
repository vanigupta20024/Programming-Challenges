from tkinter import *
import time
from tkinter import ttk

root = Tk()
root.geometry('1600x800+0+0')
root.title("Hotel management system")

def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator = ''
    txt_input.set('')
    display.insert(0, 'Start calculating...')

def equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''

def totalcost():
    varme1 = meal_box.get()
    varme2 = meal1.get()
    if varme1 == 'Noodles':
        varme3 = (varme2*1.8)
        cost.set(varme3)
    elif varme1 == 'Pizza':
        varme3 = (varme2*2.2)
        cost.set(varme3)
    elif varme1 == 'Springroll':
        varme3 = (varme2*1.5)
        cost.set(varme3)
    elif varme1 == 'Burger':
        varme3 = (varme2*1.3)
        cost.set(varme3)
    else:
        varme3 = varme2*0.0
        cost.set(varme3)

    vardi1 = drink_box.get()
    vardi2 = drink1.get()
    if vardi1 == 'Pepsi':
        vardi3 = (vardi2*1.8)
        drink.set(vardi3)
    elif vardi1 == 'Water':
        vardi3 = (vardi2*2.2)
        drink.set(vardi3)
    elif vardi1 == 'Lemonade':
        vardi3 = (vardi2*1.5)
        drink.set(vardi3)
    elif vardi1 == 'Frooti':
        vardi3 = (vardi2*1.3)
        drink.set(vardi3)
    else:
        vardi3 = vardi2*0.0
        drink.set(vardi3)

    num1 = float(cost.get())
    num2 = float(drink.get())
    deli = (num1 + num2)*0.5


    room1 = v.get()
    null = 0.0
    rvip = 10
    rvip1 = deli/(10*0.5)
    rnormal = 5
    rnormal1 = deli/(5*2.5)

    if room1 == 1:
        if chkbx1.get() == 1:
            service.set(rvip1)
            room.set(10.0)
            delivery.set(deli)
        else:
            service.set(null)
            delivery.set(null)
            room.set(10.0)
    if room1 == 2:
        if chkbx1.get() == 1:
            service.set(rnormal)
            room.set(5.0)
            delivery.set(deli)
        else:
            service.set(null)
            delivery.set(null)
            room.set(5.0)
    if room1 == 3:
        if chkbx1.get() == 1:
            service.set(null)
            room.set(null)
            delivery.set(null)
        else:
            service.set(null)
            delivery.set(null)
            room.set(null)

    num3 = float(delivery.get())
    num4 = float(room.get())
    num5 = float(service.get())
    mytotal = num1+num2+num3+num4+num5
    total.set(mytotal) 
    finaltotal = "Total  = " + str(mytotal) + "$"

    num6 = texttot.get()
    display.delete(0, END)
    display.insert(0, finaltotal)
    if num6 <= '0.0':
        display.delete(0, END)
        display.insert(0, 'Please make an order.')


def convert():
    var2 = indicator.get()
    var3 = var1.get()

    if var2 == 'India':
        display.delete(0, END)
        var4 = ('INR', (var3 * 72.00))
        display.insert(0, var4)
    elif var2 == 'France':
        display.delete(0, END)
        var4 = ('Euro', (var3 * 0.8))
        display.insert(0, var4)
    elif var2 == 'Nigeria':
        display.delete(0, END)
        var4 = ('Naira', (var3 * 365.00))
        display.insert(0, var4)
    else:
        display.insert(0, 'Error: Select a country!')

def clearScreen():
    display.delete(0, END)
    room.set('')
    total.set('')
    service.set('')
    drink.set('')
    cost.set('')
    delivery.set('')
    txtQty.set('')
    txtQty1.set('')

def stop():
    root.destroy()

def exit():
    display.delete(0, END)
    display.insert(0, 'Thanks for patronage...')
    display.after(2000, stop)

def hotel():
    display.delete(0, END)
    display.insert(0, "-- Hotel Tkinter --")

def powered():
    display.delete(0, END)
    display.insert(0, 'Powered by python...')

def reset():
    display.delete(0, END)
    display.insert(0, 'System resetting..')
    display.after(2000, hotel)
    display.after(4000, powered)
    display.after(6000, rst)

def rst():
    clear()
    display.delete(0, END)
    display.insert(0, 'Hotel management')
    meal_box.set(value = 'Food items')
    drink_box.set(value = 'Fresh Drinks')
    indicator.set(value = 'Select a country')
    txtQty.delete(0, END)
    txtQty.insert(0, 0)
    txtQty1.delete(0, END)
    txtQty1.insert(0, 0)
    txtamnt.delete(0, END)
    txtamnt.insert(0, 0)
    room.set(0.0)
    total.set(0.0)
    service.set(0.0)
    drink.set(0.0)
    cost.set(0.0)
    chkbx1.set(0)
    v.set(3)
    delivery.set(0.0)


#======================Windows partition===================#

topscreen = Frame(root, width = 1600, height = 100, bg = 'coral3', relief = SUNKEN)
topscreen.pack(side = TOP)

f1 = Frame(root, width = 700, height = 700, relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 300, height = 700, relief = SUNKEN)
f2.pack(side = RIGHT)

f3 = Frame(root, width = 30, height = 700, relief = SUNKEN)
f3.pack(side = LEFT)

f4 = Frame(root, width = 100, height = 700, relief = SUNKEN)
f4.pack(side = LEFT)

#==========================Main screen=====================#

txt_input = StringVar(value = 'Hotel management')

display = Entry(topscreen, font = ('arial', 90, 'bold'), fg = 'white', bd = 30,
    bg = 'coral3', justify = 'center', textvariable = txt_input)

display.grid(columnspan = 4)

#===========================Date and Time====================#

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(f2, font = ('arial', 20, 'bold'), text = localtime, bd = 10, anchor = W)
lblinfo.grid(row = 0, column = 0, columnspan = 4)

#=======================Calculator=====================#

#=======================row 1 =========================#

operator = ''

btn7 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '7', bg = 'salmon1', command = lambda: btn(7))
btn7.grid(row = 1, column = 0)
btn8 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '8', bg = 'salmon1', command = lambda: btn(8))
btn8.grid(row = 1, column = 1)
btn9 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '9', bg = 'salmon1', command = lambda: btn(9))
btn9.grid(row = 1, column = 2)
btnC = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = 'C', bg = 'salmon1', command = clear)
btnC.grid(row = 1, column = 3)

#=======================row 2 =========================#

btn4 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '4', bg = 'salmon1', command = lambda: btn(4))
btn4.grid(row = 2, column = 0)
btn5 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '5', bg = 'indian red', command = lambda: btn(5))
btn5.grid(row = 2, column = 1)
btn6 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '6', bg = 'indian red', command = lambda: btn(6))
btn6.grid(row = 2, column = 2)
btnsum = Button(f2, padx = 18, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '+', bg = 'salmon1', command = lambda: btn('+'))
btnsum.grid(row = 2, column = 3)

#=======================row 3 =========================#

btn1 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '1', bg = 'salmon1', command = lambda: btn(1))
btn1.grid(row = 3, column = 0)
btn2 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '2', bg = 'indian red', command = lambda: btn(2))
btn2.grid(row = 3, column = 1)
btn3 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '3', bg = 'indian red', command = lambda: btn(3))
btn3.grid(row = 3, column = 2)
btndif = Button(f2, padx = 23, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '-', bg = 'salmon1', command = lambda: btn('-'))
btndif.grid(row = 3, column = 3)

#=======================row 4 =========================#

btn0 = Button(f2, padx = 15, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '0', bg = 'salmon1', command = lambda: btn(0))
btn0.grid(row = 4, column = 0)
btndot = Button(f2, padx = 21, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '.', bg = 'indian red', command = lambda: btn('.'))
btndot.grid(row = 4, column = 1)
btndiv = Button(f2, padx = 21, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '/', bg = 'indian red', command = lambda: btn('/'))
btndiv.grid(row = 4, column = 2)
btnmul = Button(f2, padx = 17, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = 'x', bg = 'salmon1', command = lambda: btn('*'))
btnmul.grid(row = 4, column = 3)

#=======================row 5 =========================#

btneq = Button(f2, padx = 64, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '=', bg = 'salmon1', command = equal)
btneq.grid(row = 5, column = 0, columnspan = 2)
btnopb = Button(f2, padx = 20, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = '(', bg = 'salmon1', command = lambda: btn('('))
btnopb.grid(row = 5, column = 2)
btnclb = Button(f2, padx = 21, pady = 5, bd = 8, font = ('arial', 30, 'bold'), text = ')', bg = 'salmon1', command = lambda: btn(')'))
btnclb.grid(row = 5, column = 3)

#==============================Meals===================#
meal1 = IntVar()
meal_box = StringVar(value = 'Food items')

lblMeal = Label(f1, font = ('arial', 16, 'bold'), text = 'Choose meal:', bd = 10, anchor = W)
lblMeal.grid(row = 0, column = 0)

textmeal = ttk.Combobox(f1, font = ('arial', 16, 'bold'), textvariable = meal_box)
textmeal['values'] = ('Noodles', 'Springroll', 'Pizza', 'Burger')
textmeal.grid(row = 0, column = 1)

lblQty = Label(f1, font = ('arial', 16, 'bold'), text = "Quantity:", bd = 10, anchor = W)
lblQty.grid(row = 1, column = 0)

txtQty = Entry(f1, font = ('arial', 16, 'bold'), textvariable = meal1, bd = 10, insertwidth = 4, justify = 'right')
txtQty.grid(row = 1, column =1)

#==============================Drinks===================#

drink1 = IntVar()
drink_box = StringVar(value = 'Fresh drinks')

lblDrink = Label(f1, font = ('arial', 16, 'bold'), text = 'Choose drink:', bd = 10, anchor = W)
lblDrink.grid(row = 2, column = 0)

textdrink = ttk.Combobox(f1, font = ('arial', 16, 'bold'), textvariable = drink_box)
textdrink['values'] = ('Water', 'Pepsi', 'Lemonade', 'Frooti')
textdrink.grid(row = 2, column = 1)

lblQty1 = Label(f1, font = ('arial', 16, 'bold'), text = "Quantity:", bd = 10, anchor = W)
lblQty1.grid(row = 3, column = 0)

txtQty1 = Entry(f1, font = ('arial', 16, 'bold'), textvariable = drink1, bd = 10, insertwidth = 4, justify = 'right')
txtQty1.grid(row = 3, column =1)

#==============================Delivery===================#

chkbx1 = IntVar()

lbldev = Label(f1, font = ('arial', 16, 'bold'), text = 'Delivery?', bd = 10, anchor = W)
lbldev.grid(row = 4, column = 0)

check = Checkbutton(f1, font = ('arial', 16, 'bold'), text = "Yes", bd = 10, variable = chkbx1)
check.grid(row = 4, column = 1)

#==============================Room===================#

v = IntVar()
v.set(3)

lblRoom = Label(f1, font = ('arial', 16, 'bold'), text = 'Book a room:',  bd = 10, anchor = W)
lblRoom.grid(row = 5, column = 0)

radiobutton = Radiobutton(f1, font = ('arial', 16, 'bold'), text = 'VIP', variable = v, value = 1)
radiobutton.grid(row = 5, column = 1, sticky = E)

radiobutton = Radiobutton(f1, font = ('arial', 16, 'bold'), text = 'Normal', variable = v, value = 2)
radiobutton.grid(row = 5, column = 1)

radiobutton = Radiobutton(f1, font = ('arial', 16, 'bold'), text = 'No', variable = v, value = 3)
radiobutton.grid(row = 5, column = 1, sticky = W)

#==============================Cost===================#

cost = StringVar()
lblmeal1 = Label(f1, font = ('arial', 16, 'bold'), text = 'Cost of meal ($)', bd = 10, anchor = W)
lblmeal1.grid(row = 0, column = 2)

textmeal1 = Entry(f1, font = ('arial', 16, 'bold'), textvariable = cost, bd = 10, insertwidth = 4, justify = 'right')
textmeal1.grid(row = 0, column = 3)


drink = StringVar()
lbldrink1 = Label(f1, font = ('arial', 16, 'bold'), text = 'Cost of drink ($)', bd = 10, anchor = W)
lbldrink1.grid(row = 1, column = 2)

textdrink1 = Entry(f1, font = ('arial', 16, 'bold'), textvariable = drink, bd = 10, insertwidth = 4, justify = 'right')
textdrink1.grid(row = 1, column = 3)

delivery = StringVar()
lbldev = Label(f1, font = ('arial', 16, 'bold'), text = 'Cost of delivery ($)', bd = 10, anchor = W)
lbldev.grid(row = 2, column = 2)

textdev = Entry(f1, font = ('arial', 16, 'bold'), textvariable = delivery, bd = 10, insertwidth = 4, justify = 'right')
textdev.grid(row = 2, column = 3)

room = StringVar()
lblroom = Label(f1, font = ('arial', 16, 'bold'), text = 'Cost of Room ($)', bd = 10, anchor = W)
lblroom.grid(row = 3, column = 2)

textroom = Entry(f1, font = ('arial', 16, 'bold'), textvariable = room, bd = 10, insertwidth = 4, justify = 'right')
textroom.grid(row = 3, column = 3)

service = StringVar()
lblser = Label(f1, font = ('arial', 16, 'bold'), text = 'Service charge ($)', bd = 10, anchor = W)
lblser.grid(row = 4, column = 2)

textser = Entry(f1, font = ('arial', 16, 'bold'), textvariable = service, bd = 10, insertwidth = 4, justify = 'right')
textser.grid(row = 4, column = 3)

total = StringVar()
lbltot = Label(f1, font = ('arial', 16, 'bold'), text = 'Total ($)', bd = 10, anchor = W)
lbltot.grid(row = 5, column = 2)

texttot = Entry(f1, font = ('arial', 16, 'bold'), textvariable = total, bd = 10, insertwidth = 4, justify = 'right')
texttot.grid(row = 5, column = 3)

#==============================Currency converter===================#

var1 = IntVar()
indicator = StringVar(value = 'Choose a country: ')

lblcurrcon = Label(f1, font = ('arial', 16, 'bold'), text = '------------Currency Converter------------', bd = 20, anchor = W)
lblcurrcon.grid(row = 6, column = 0, columnspan = 4)

lblcountry = Label(f1, font = ('arial', 16, 'bold'), text = 'Nationality', bd = 20, anchor = W)
lblcountry.grid(row = 7, column = 0)

txtcountry = ttk.Combobox(f1, font = ('arial', 16, 'bold'), textvariable = indicator)
txtcountry['values'] = ('India', 'France', 'Nigeria')
txtcountry.grid(row = 7, column = 1)

lblammount = Label(f1, font = ('arial', 16, 'bold'), text = 'Amount ($)', bd = 20, anchor = W)
lblammount.grid(row = 7, column = 2)

txtamnt = Entry(f1, font = ('arial', 16, 'bold'), textvariable = var1, bd = 10, insertwidth = 4, justify = 'right')
txtamnt.grid(row = 7, column = 3)

#==============================Buttons===================#

btnconvert = Button(f1, padx = 10, pady = 4, bd = 16, width = 10, font = ('arial', 16, 'bold'), text = "Convert", command = convert, bg = 'RosyBrown1')
btnconvert.grid(row = 8, column = 2)

btntotal = Button(f4, padx = 10, pady = 8, bd = 16, width = 10, font = ('arial', 16, 'bold'), text = "Total", command = totalcost, bg = 'light pink')
btntotal.grid(row = 0, column = 0)

btnscreen = Button(f4, padx = 10, pady = 4, bd = 16, width = 10, font = ('arial', 16, 'bold'), text = "Clear", command = clearScreen, bg = 'light pink')
btnscreen.grid(row = 1, column = 0)

btnreset = Button(f4, padx = 10, pady = 8, bd = 16, width = 10, font = ('arial', 16, 'bold'), text = "Reset", command = reset, bg = 'light pink')
btnreset.grid(row = 2, column = 0)

btnexit = Button(f4, padx = 10, pady = 4, bd = 16, width = 10, font = ('arial', 16, 'bold'), text = "Exit", command = exit, bg = 'light pink')
btnexit.grid(row = 3, column = 0)

root.mainloop()
