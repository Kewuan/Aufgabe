from tkinter import *

root = Tk()

one = Label(root, text='One', bg="#000000000", fg='#FF00FF')
two = Label(root, text='Two', bg="#0000ff", fg='#20B2AA')
three = Label(root, text='Three', bg="black", fg='red')
one.pack(fill=X)
two.pack(fill=X)
three.pack(fill=X)

root.mainloop()