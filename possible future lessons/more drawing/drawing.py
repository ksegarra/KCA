import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, height=400, width=800)

#C.create_line(0,0,200,400, width = 5)
# other shapes
#   C.create_oval(200, 200, 400, 400)
#   C.create_line(x1, y1, x2, y2)
#   C.create_polygon(x1, y1, x2, y2 ... xn, yn)

# lets make a parametrized draw house function

# recall the old function we used to make a house

##def create_house():
##    C.create_rectangle(200,200,400,400, fill='red')
##    C.create_polygon(200,200,300,50,400,200, fill='blue')
##    C.create_rectangle(320,250,380,400,fill='maroon')

def draw_house(x: int, y: int):
    pass

def draw_tree(x: int, y: int):
    pass

def main():
    '''lets create a neighborhood with 3 houses and 8 trees by
    calling the functions we made above'''
    pass

    
main()

C.pack()
top.mainloop()


    
