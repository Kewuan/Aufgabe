from tkinter import *


def green():
    return var1.get()


def blau():
    return var2.get()


def rot():
    return var3.get()


root = Tk()
root.title("Additive Farbmischung.py")

leftFrame = Frame(root)
rightFrame = Frame(root, width=100, height=100)
leftFrame.pack(side=LEFT)
rightFrame.pack(side=RIGHT)

# ***** left frame *****

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
leftFrame.roller1 = Scale(leftFrame, from_=1, to=255, variable=var1, command=green)
leftFrame.roller2 = Scale(leftFrame, from_=1, to=255, variable=var2, command=blau)
leftFrame.roller3 = Scale(leftFrame, from_=1, to=255, variable=var3, command=rot)
leftFrame.roller1.grid(row=0, column=0)
leftFrame.roller2.grid(row=0, column=1)
leftFrame.roller3.grid(row=0, column=3)


# ***** right frame *****
def farbe():
    return '#' + format(green(), 'x') + format(blau(), 'x') + format(rot(), 'x')


root.mainloop()
