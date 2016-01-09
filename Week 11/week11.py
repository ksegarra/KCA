#tkinter - a module that allows us to draw stuff

import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, height=400, width=800)

#C.create_line(0,0,200,400, width = 5)
C.create_line(400,0,400,400, width = 10, fill='red')


rectangle = C.create_rectangle(100,100,300,200, width=10, fill='blue')
C.create_oval(100, 100, 400, 400, width = 10, fill='yellow')
C.create_polygon(0,0,200,100,100,300,800,800)

# other shapes
#   C.create_oval(x1, y1, x2, y2)
#   C.create_line(x1, y1, x2, y2)
#   C.create_polygon(x1, y1, x2, y2 ... xn, yn)

#lets make a house


C.pack()
top.mainloop()
