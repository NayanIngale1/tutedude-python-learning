# step 1: import tkinter

from tkinter import *

# step 2: GUI interaction
window = Tk()

# step 3: adding inputs
inp = Label(window, text='Hello world!')
inp.pack()

# step 4: main loop
window.mainloop()
