from tkinter import *

def sel():
    selection = "Value = " + str(var.get())
    label.config(text=selection)

root = Tk()

var = IntVar()
scale = Scale(root, variable=var)
scale.pack(anchor=CENTER)

botton = Button(root, text="Get Scale Value", command=sel)
botton.pack()

label = Label(root)
label.pack()

root.mainloop()