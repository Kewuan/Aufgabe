from tkinter import *
import random
import time

# assign the module to a var
tk = Tk()

# set global vars
Height = 500
Width = 500

canvas = Canvas(tk, width=Width, height=Height)
tk.title("Graphics")
canvas.pack()

ball = canvas.create_oval(0, 0, 100, 100, fill='red')
xspeed = 5
yspeed = 0
while True:

    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)  # [left, top, right, bottom]

    if pos[2]>=Width:
        xspeed = -xspeed

    # make the ball bounce forever
    # make the ball bounce on the x and the y
    # make ball bounce around screen
    tk.update()
    time.sleep(0.01)

tk.mainloop()
