from tkinter import*
import tkinter
top = Tk()
mb = Menubutton(top,text = "File",relief = RAISED)
mb.grid()
mb.menu = Menu(mb,tearoff=0)
mb["menu"] =mb .menu
mb.menu.add_checkbutton(label = "New")
mb.menu.add_checkbutton(label = "Open")

mb.pack()
top.mainloop()
