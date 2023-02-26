from tkinter import *
from random import *

padding = 10
canvas_width = 300
canvas_height = 300

def randColor() :
    colors = {0: 'yellow', 1: 'red', 2: 'blue'}
    return colors[randrange(0, 3)]

def drawSquare() :
    left = randrange(1, min(canvas_width - padding, canvas_height - padding))
    canvas.create_rectangle(padding, padding, left, left, fill = randColor())

def drawCircle() :
    left = randrange(1, min(canvas_width - padding, canvas_height - padding))
    canvas.create_oval(padding, padding, left, left, fill = randColor())

def drawTriangle() :
    canvas.create_polygon(padding,
                          padding,
                          randrange(1, min(canvas_width - padding, canvas_height - padding)),
                          randrange(1, min(canvas_width - padding, canvas_height - padding)),
                          randrange(1, min(canvas_width - padding, canvas_height - padding)),
                          randrange(1, min(canvas_width - padding, canvas_height - padding)),
                          fill = randColor())

root = Tk()
root.geometry(str(canvas_width)+ "x" + str(canvas_width + 50))
canvas = Canvas(root, width = canvas_width, height = canvas_height, bg = 'white')
canvas.pack()

def callback():
    canvas.delete("all")
    val = randrange(0, 3)

    if val == 0 :
        drawSquare()
    elif val == 1 :
        drawCircle()
    elif val == 2 :
         drawTriangle()

button = Button(root,text='Push me!',command=callback)
button.pack()

root.mainloop()
