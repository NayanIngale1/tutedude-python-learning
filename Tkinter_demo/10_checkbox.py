# Step 1: Import Tkinter
from tkinter import *

# Step 2: Create the main window
window = Tk()
window.title('Checkbox - Fruits You Like')
window.geometry('500x500')
window.config(bg='lightblue')

# Step 3: Title Label
title = Label(window, text='Select the fruits you like:',
              font=('Arial', 14, 'bold'), bg='lightblue')
title.pack(pady=10)

# Step 4: Variables to track checkbox states
apple_var = IntVar()   # 1 if selected, 0 if not
banana_var = IntVar()
mango_var = IntVar()
grape_var = IntVar()

# Step 5: Create checkboxes
apple_cb = Checkbutton(window, text='Apple',
                       variable=apple_var, bg='lightblue', font=('Arial', 12))
banana_cb = Checkbutton(window, text='Banana',
                        variable=banana_var, bg='lightblue', font=('Arial', 12))
mango_cb = Checkbutton(window, text='Mango',
                       variable=mango_var, bg='lightblue', font=('Arial', 12))
grape_cb = Checkbutton(window, text='Grapes',
                       variable=grape_var, bg='lightblue', font=('Arial', 12))

# Display checkboxes on screen
apple_cb.pack()
banana_cb.pack()
mango_cb.pack()
grape_cb.pack()

# Step 6: Function to show selected fruits


def show_selected():
    result = "You like:\n"
    if apple_var.get() == 1:
        result += "🍎 Apple\n"
    if banana_var.get() == 1:
        result += "🍌 Banana\n"
    if mango_var.get() == 1:
        result += "🥭 Mango\n"
    if grape_var.get() == 1:
        result += "🍇 Grapes\n"

    # Update label with result
    selected_label.config(text=result)


# Step 7: Button to submit selection
btn = Button(window, text='Submit', command=show_selected,
             font=('Arial', 12), bg='white')
btn.pack(pady=10)

# Step 8: Label to display the result
selected_label = Label(window, text='', font=('Arial', 12), bg='lightblue')
selected_label.pack(pady=10)

# Step 9: Run the main loop
window.mainloop()
