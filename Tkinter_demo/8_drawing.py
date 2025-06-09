from tkinter import *

# Step 1: Create the main window
window = Tk()
window.title('Drawing Example')
window.geometry('500x500')
window.config(bg='pink')

# Step 2: Create Canvas
# Added white background inside canvas
c = Canvas(window, width=500, height=300, bg='white')
c.pack()

# Step 3: Draw shapes

# Draw a line (from (0,0) to (500,300))
c.create_line(0, 0, 500, 300, fill='blue', width=3)

# Draw a rectangle
c.create_rectangle(50, 50, 150, 150, fill='red', outline='yellow', width=4)

# Draw an oval (circle)
c.create_oval(200, 50, 300, 150, fill='yellow')

# Draw some text
c.create_text(250, 250, text="Hello Canvas!", font=('Arial', 20), fill='green')

# Draw a triangle (polygon)
c.create_polygon(400, 50, 450, 150, 350, 150, fill='purple')


# extra
def draw_circle(event):
    x = event.x    # x-coordinate where you clicked
    y = event.y    # y-coordinate where you clicked

    # Create a small circle (oval) at the click position
    r = 10  # radius of circle
    c.create_oval(x - r, y - r, x + r, y + r, fill='blue')


# Step 4: Bind mouse click event to the function
c.bind('<Button-1>', draw_circle)
# <Button-1> = Left mouse click


# Step 4: Run the window
mainloop()
