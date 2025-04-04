from tkinter import *

root = Tk()

Scrollbar = Scrollbar(root)
Scrollbar.pack(side = RIGHT, fill = Y) #fill y axis with scrollbar
mylist =Listbox(root,yscrollcommand =Scrollbar.set)
for line in range(100):
    mylist.insert(END,"Line" + str(line))
mylist.pack(side=LEFT)
Scrollbar.config(command=mylist.yview)#For Scrolling Function

mainloop()
