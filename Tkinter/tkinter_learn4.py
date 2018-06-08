from tkinter import *

root = Tk()


def printNmae(event):
    print("Chello my name is Bucky!")


button_1 = Button(root, text="Print my name", fg='red')
button_1.bind('<Button-1>', printNmae)
button_1.pack()

root.mainloop()
