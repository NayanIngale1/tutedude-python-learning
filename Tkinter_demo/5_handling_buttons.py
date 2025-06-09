from tkinter import *


window = Tk()

window.title('Handling buttons tutorial')
window.geometry('500x500')
window.config(bg='white')


def log_entry():
    print('Logged In')


button = Button(window, text='LOGIN', command=log_entry,
                width=12, highlightbackground='green', fg='black', relief=FLAT, font=('bold', '12'), activebackground='black', activeforeground='white')
button.pack()


mainloop()
