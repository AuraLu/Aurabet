from Tkinter import *

class blah:

def MoveWindow(self, event):
self.root.update_idletasks()
self.f.place_configure(x=event.x_root, y=event.y_root-20)

def __init__(self):
self.root = Tk()
self.root.title("...")
self.root.resizable(0,0)
self.root.geometry("%dx%d%+d%+d"%(640, 480, 0, 0))

self.f = Frame(self.root, bd=1, relief=SUNKEN)
self.f.place(x=0, y=0, width=200, height=200)

self.l = Label(self.f, bd=1, relief=RAISED, text="Test")
self.l.pack(fill=X, padx=1, pady=1)

self.l.bind('<B1-Motion>', self.MoveWindow)
self.f.bind('<B1-Motion>', self.MoveWindow)

self.root.mainloop()

x = blah()
