from tkinter import*

root = Tk()

frame=Frame(root)

frame.pack()

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text ="Red", fg="red")#fg=foreground
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text="Green", fg="green")
greenbutton.pack(side=LEFT)

root.mainloop()
