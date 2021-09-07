import turtle

pen = turtle.Turtle()

def cube(t,n,lenght):
    if(n ==0):
        return

    t.fd(lenght/3)
    
    t.lt(90)
    cube(t,n-1,lenght/3)
    t.fd(lenght/3)
    
    t.rt(90)
    cube(t,n-1,lenght/3)
    t.fd(lenght/3)
    
    t.rt(90)
    cube(t,n-1,lenght/3)
    t.fd(lenght/3)

    t.lt(90)
    t.fd(lenght/3)

def draw_cube(t,n,lenght):
    for i in range(4):
        cube(t,n,lenght)
        t.rt(90)


draw_cube(pen,2,120)







turtle.mainloop()