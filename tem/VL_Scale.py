from tkinter import *


def func():
    global f
    wert2 = float(f.s2.get())


f = Tk()
wert1 = IntVar()
f.s1 = Scale(f, from_=5, to=149, variable=wert1)
f.s2 = Scale(f, from_=5, to=149, length=300,
             orient=HORIZONTAL, command=func)

f.s1.pack()
f.s2.pack()

f.mainloop()
