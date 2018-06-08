from tkinter import *

root = Tk()

def leftClick(event):
    print('Left')

def middleClick(event):
    print('Middle')

def rightClick(event):
    print('Right')

frame = Frame(root, width=300, height=250)
frame.bind('<Button-1>', leftClick)   # What does '<Button-1>' actually do?
frame.bind('<Button-2>', middleClick) # The same, what does '<Button-2>'s
frame.bind('<Button-3>', rightClick)
frame.pack()


root.mainloop()