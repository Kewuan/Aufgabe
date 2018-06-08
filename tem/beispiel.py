from tkinter import *

def counting():
    global i
    i += 1
    fenster.label.config(text='Counter: ' +str(i))

i = 0
fenster = Tk()
fenster.label = Label(master=fenster,
                      text='Counter: 0')

fenster.label.pack()

fenster.button = Button(master=fenster,
                        text='counting',
                        command=counting)

fenster.button.pack()
fenster.mainloop()