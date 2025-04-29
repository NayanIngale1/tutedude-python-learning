from tkinter import *
import tkinter.messagebox

window = Tk()
window.title('All Message Box Types')
window.geometry('400x400')
window.config(bg='lightblue')

# showinfo
tkinter.messagebox.showinfo('Information', 'This is an info message.')

# showwarning
tkinter.messagebox.showwarning('Warning', 'This is a warning!')

# showerror
tkinter.messagebox.showerror('Error', 'Something went wrong!')

# askquestion
answer1 = tkinter.messagebox.askquestion('Question', 'Do you like Python?')
print('Answer to askquestion:', answer1)  # will print 'yes' or 'no'

# askokcancel
answer2 = tkinter.messagebox.askokcancel(
    'OK Cancel', 'Do you want to continue?')
print('Answer to askokcancel:', answer2)  # True or False

# askyesno
answer3 = tkinter.messagebox.askyesno('Yes No', 'Save your progress?')
print('Answer to askyesno:', answer3)  # True or False

# askretrycancel
answer4 = tkinter.messagebox.askretrycancel(
    'Retry Cancel', 'Try connecting again?')
print('Answer to askretrycancel:', answer4)  # True or False

window.mainloop()
