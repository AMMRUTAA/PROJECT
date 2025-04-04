from tkinter import *
from tkinter import messagebox

top = Tk()

# Creating a canvas
c = Canvas(top, height=250, width=300)

# Drawing a line
line = c.create_line(0, 20, 70, 20, fill='black')

# Drawing an arc
arc = c.create_arc(10, 50, 140, 110, start=0, extent=150, fill="pink")

# Drawing a rectangle
rectangle = c.create_rectangle(110, 150, 150, 100, fill="blue")

# Drawing an oval
oval = c.create_oval(120, 160, 280, 210, fill="red")

# Drawing a polygon
polygon = c.create_polygon(250, 30, 200, 50, 230, 90)

c.pack()
top.mainloop()
