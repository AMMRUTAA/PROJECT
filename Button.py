from tkinter import *
from tkinter import ttk  # Correcting the import for ttk

# Create the main window
root = Tk()  # 'TK()' should be 'Tk()'

# Define the function for the button command
def button_pressed():
    print("Button pressed!")

# Create a button using ttk
button = ttk.Button(root, text="Hello", command=button_pressed)  # 'TTK.button' should be 'ttk.Button'

# Place the button in the grid
button.grid()

# Start the main event loop
root.mainloop()
