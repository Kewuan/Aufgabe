# -*- coding: utf-8 -*-
from tkinter import *
import random


def giveGray():
    v = random.randint(1, 99)
    return 'gray' + str(v)


def getValue(x):
    x = int(x)
    rightFrame.config(bg='gray' + str(x))


master = Tk()
master.title("Wahrnehmungstest.py")

# ***** zwei Fläche *****

leftFrame = Frame(master, height=200, width=100, bg=giveGray())
label = Label(leftFrame, text="leftlabel")
label.config()
rightFrame = Frame(master, height=300, width=100, bg='gray50')
leftFrame.pack(side=LEFT)
rightFrame.pack(side=RIGHT)

sca = Scale(rightFrame, from_=1, to=99, orient=HORIZONTAL,
            width=20, command=getValue)
# value = 'gray' + str(sca.get())
sca.pack(side=BOTTOM)

# righttopFram = Frame(rightFrame, height=150, width=100, bg=getValue)
# righttopFram.pack(side=TOP)

# ***** vergleichen *****



master.mainloop()
