from tkinter import *

def greetings(event) :
    label.config(text = "Hello " + contents.get())

root = Tk()

label = Label()
label.pack()
entrythingy = Entry()
entrythingy.pack()

contents = StringVar()
contents.set("no name")
entrythingy["textvariable"] = contents
entrythingy.bind('<Key-Return>', greetings)

root.mainloop()
