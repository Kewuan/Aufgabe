from tkinter import *


def func():
    pass


f = Tk()
apfel = IntVar()
birne = StringVar()

f.c1 = Checkbutton(f, text='Äpfel', offvalue=0,
                   onvalue=1, variable=apfel)

f.c2 = Checkbutton(f, text='Biernen',
                   offvalue='off', onvalue='on',
                   variable=birne, command=func)

f.c1.pack()
f.c2.pack()

f.mainloop()
