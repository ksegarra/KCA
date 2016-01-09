import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, height=400, width=800)

#C.create_line(0,0,200,400, width = 5)
# other shapes
#   C.create_oval(200, 200, 400, 400)
#   C.create_line(x1, y1, x2, y2)
#   C.create_polygon(x1, y1, x2, y2 ... xn, yn)

def create_circles(x,y):
    C.create_oval(x,y,x+100,y+100,fill='blue')
    C.create_oval(x+100,y+100,x+200,y+200,fill='red')

##create_circles(0,0)
##create_circles(150,150)
##create_circles(10,0)
##create_circles(20,60)
    
def create_lollipop(x,y,color):
    C.create_line(x+50,y+50,x+50,y+150)
    C.create_oval(x,y,x+100,y+100,fill=color)

create_lollipop(0,0,'green')
create_lollipop(200,200,'red')
create_lollipop(400,200,'blue')

C.pack()
top.mainloop()
