from tkinter import *

class BucksButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quiteButton = Button(frame, text="Quite", command=frame.quit)
        self.quiteButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked!")



root = Tk()
b = BucksButtons(root)
root.mainloop()