from tkinter import *

f = Tk()

ctr = IntVar()
f.r1 = Radiobutton(f, text='5', value='5', variable=ctr)
f.r2 = Radiobutton(f, text='19', value='19', variable=ctr)
f.r3 = Radiobutton(f, text='36', value='36', variable=ctr)

for r in [f.r1, f.r2, f.r3]:
    r.pack()

f.mainloop()
