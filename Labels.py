from tkinter import*

root = Tk()

Label(root,text="Hello I am red color text",fg="red",font="Times").pack()
Label(root,text="Hello I am green color text",fg="Light Green",bg="Dark Green",
      font="Helvetica 16 bold italic").pack()

root.mainloop()
