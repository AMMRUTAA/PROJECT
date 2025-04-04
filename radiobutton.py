from tkinter import *

root = Tk()

Label(root,text="select the programming language",justify=LEFT,padx = 20).pack()
      

Radiobutton(root,text="Python",padx=20,value=1).pack(anchor=w) #anchor w means place widget to west
      
Radiobutton(root,text="Pearl",padx=20,value=1).pack(anchor=w)
      

mainloop()
