from tkinter import *

root = Tk()

photo = PhotoImage(file='hbPNG.png')
label = Label(root, image=photo)
label.pack()


root.mainloop()