from tkinter import *
import tkinter.messagebox

messagebox = tkinter.messagebox

window = Tk()
window.title('Calculator using tkinter')
window.geometry('500x500')
window.config(bg='lightyellow')


# entry box
entry_var = StringVar()
entry = Entry(window, width=42, borderwidth=3, textvariable=entry_var)
entry.place(x=10, y=10)


# Step 3: Initialize global variables
operator = None
operand1 = None

result_displayed = False

# buttons and functions


def click(num):
    global result_displayed
    if result_displayed:
        entry_var.set('')  # Clear previous result
        result_displayed = False
        
    n1 = entry_var.get()
    entry_var.set(str(n1)+str(num))


def add():
    global operand1, operator
    try:
        operand1 = int(entry_var.get())
        operator = 'addition'
        entry_var.set('')
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter a number before clicking +")


def sub():
    global operand1, operator
    try:
        operand1 = int(entry_var.get())
        operator = 'subtraction'
        entry_var.set('')
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter a number before clicking -")


def mult():
    global operand1, operator
    try:
        operand1 = int(entry_var.get())
        operator = 'multiplication'
        entry_var.set('')
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter a number before clicking *")


def divide():
    global operand1, operator
    try:
        operand1 = int(entry_var.get())
        operator = 'division'
        entry_var.set('')
    except ValueError:
        messagebox.showerror(
            "Input Error", "Please enter a number before clicking /")


def clear():
    entry_var.set('')


def equal():
    global operator, operand1, result_displayed
    operand2 = entry_var.get()
    if operator is None or operand1 is None:
        entry_var.set("Error")
        return

    result_displayed = True  # Result is now displayed

    try:
        if operator == 'addition':
            result = operand1 + int(operand2)
        elif operator == 'subtraction':
            result = operand1 - int(operand2)
        elif operator == 'multiplication':
            result = operand1 * int(operand2)
        elif operator == 'division':
            result = operand1 / int(operand2)

        entry_var.set(result)

    except ZeroDivisionError:
        entry_var.set("Can't divide by 0")
    except Exception as e:
        entry_var.set("Error")


btn = Button(window, text='1', width=10, command=lambda: click('1'))
btn.place(x=10, y=60)
btn = Button(window, text='2', width=10, command=lambda: click('2'))
btn.place(x=140, y=60)
btn = Button(window, text='3', width=10, command=lambda: click('3'))
btn.place(x=270, y=60)
btn = Button(window, text='4', width=10, command=lambda: click('4'))
btn.place(x=10, y=100)
btn = Button(window, text='5', width=10, command=lambda: click('5'))
btn.place(x=140, y=100)
btn = Button(window, text='6', width=10, command=lambda: click('6'))
btn.place(x=270, y=100)
btn = Button(window, text='7', width=10, command=lambda: click('7'))
btn.place(x=10, y=140)
btn = Button(window, text='8', width=10, command=lambda: click('8'))
btn.place(x=140, y=140)
btn = Button(window, text='9', width=10, command=lambda: click('9'))
btn.place(x=270, y=140)
btn = Button(window, text='0', width=10, command=lambda: click('0'))
btn.place(x=10, y=180)
btn = Button(window, text='+', width=10, command=add)
btn.place(x=140, y=180)
btn = Button(window, text='-', width=10, command=sub)
btn.place(x=270, y=180)
btn = Button(window, text='*', width=10, command=mult)
btn.place(x=10, y=220)
btn = Button(window, text='/', width=10, command=divide)
btn.place(x=140, y=220)
btn = Button(window, text='=', width=10, command=equal)
btn.place(x=270, y=220)
btn = Button(window, text='Clear', width=10, command=clear)
btn.place(x=10, y=260)


window.mainloop()
