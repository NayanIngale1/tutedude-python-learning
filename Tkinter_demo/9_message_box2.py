from tkinter import *


window = Tk()
window.title('Message box 2')
window.geometry('500x500')
window.config(bg='lightblue')


# message = Message(window,text='Python')
# message.pack()

# var = StringVar()
# message = Message(window, textvariable=var, relief=RAISED, padx=20, pady=20)
# var.set('Welcome')
# message.pack()

var = StringVar()
message = Message(window, textvariable=var, relief=RAISED, padx=30, pady=20,width=400)
inp_var = StringVar()


def insert():
    result = inp_var.get()
    var.set(result)


entry = Entry(window, textvariable=inp_var)
button1 = Button(window, text='Ok', command=insert)

message.pack()
entry.pack()
button1.pack()

mainloop()
