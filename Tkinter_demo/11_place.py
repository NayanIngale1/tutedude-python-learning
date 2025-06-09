# .pack() → Automatic(top, bottom, left, right).
# .grid() → Rows and columns like a table.
# .place() → Exact position using x and y(pixels).

from tkinter import *

window = Tk()
window.title('Login Form Example')
window.geometry('400x300')
window.config(bg='white')

# Create username label and entry
username_label = Label(window, text='Username:', font=('Arial', 12))
username_label.place(x=50, y=50)

username_entry = Entry(window, font=('Arial', 12))
username_entry.place(x=150, y=50)

# Create password label and entry
password_label = Label(window, text='Password:', font=('Arial', 12))
password_label.place(x=50, y=100)

password_entry = Entry(window, font=('Arial', 12), show='*')
password_entry.place(x=150, y=100)

# Create a login button
login_button = Button(window, text='Login', font=(
    'Arial', 12), bg='white', fg='black')
login_button.place(x=150, y=150)

window.mainloop()
