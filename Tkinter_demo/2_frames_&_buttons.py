
from tkinter import *

window = Tk()

window.title("Welcome to tkinter.")
window.geometry('400x700')
window.config(bg='pink')

# Frames are like containers where you can group buttons, labels etc.
frame1 = Frame(window, width=300, height=300, cursor='dot')  # Frame 1
frame2 = Frame(window, width=300, height=300, cursor='dotbox')  # Frame 2

# button1 = Button(frame1, text='Click me', background='blue')
# button2 = Button(frame2, text='Button', background='green')

# Using highlightbackground because on macOS 'bg' sometimes doesn't work properly on buttons
# Button inside frame1
button1 = Button(frame1, text='Click me', highlightbackground='blue')


# Button inside frame2
button2 = Button(frame2, text='Button', highlightbackground='green')

# Always first pack frames, then pack widgets (like button) inside frames
frame1.pack(side=BOTTOM)  # Frame 1 at bottom
frame2.pack(side=TOP)   # Frame 2 at top


button1.pack(padx=10, pady=10)  # Add some padding around button1
button2.pack(padx=10, pady=10)  # Add some padding around button2

# window.mainloop() keeps the window open and waits for user action
mainloop()
