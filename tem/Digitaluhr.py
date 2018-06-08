import tkinter
import time


def run():
    t = time.strftime('%H:%M:%S')
    lb0.config(text=t)
    lb0.after(2000, run)


root = tkinter.Tk()
lb0 = tkinter.Label()
lb0.grid(row=0, column=0)
run()
root.mainloop()
