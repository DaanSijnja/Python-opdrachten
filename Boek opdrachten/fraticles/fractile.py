import turtle
bob = turtle.Turtle()
bob.speed(1000)
bob.penup()
#bob.setx(-300)
#bob.sety(300)
bob.pendown()

def draw_tree(t,lenght,n):
    if n == 0 or n < 0:
        return
    angle = 45
    t.fd(lenght*n)
    t.lt(angle)
    draw_tree(t,lenght,n-1)
    t.rt(2*angle)
    draw_tree(t,lenght,n-1)
    t.lt(angle)
    t.bk(lenght*n)
    
def draw_triagle(t,n,lenght):
    if n == 0 or n < 0:
        return
    t.fd(lenght)
    draw_triagle(t,n-1,lenght)

    t.lt(120)
    
    t.fd(lenght)
    draw_triagle(t,n-1,lenght)
    t.lt(120)
    
    t.fd(lenght)
    draw_triagle(t,n-1,lenght)

    t.lt(120)
   
def box(t,n,lenght):
    if n == 0 or n < 0:
        return
    t.fd(lenght*2)
    box(t,n-1,lenght)
    t.rt(90)
    t.fd(lenght)
    box(t,n-1,lenght)
    t.rt(90*2)
    t.fd(lenght)
    box(t,n-1,lenght)
    t.rt(90)
    t.fd(lenght)
    box(t,n-1,lenght)

def draw_box(t,n,lenght):
    for i in range(4):
        box(t,n,lenght)   
        t.rt(90)

def cross(t,n,lenght):
    if n == 0 or n < 0:
        return
    t.fd(lenght)
    t.rt(90)
    t.fd(lenght)
    cross(t,n-1,lenght)
    t.lt(90)
    t.fd(lenght)
    cross(t,n-1,lenght)
    t.lt(90)
    t.fd(lenght)
    cross(t,n-1,lenght)
    t.rt(90)
    t.fd(lenght)
    cross(t,n-1,lenght)

def draw_cross(t,n,lenght):
        cross(t,n,lenght)
        t.lt(90)
        cross(t,n,lenght)
        t.lt(90)
        cross(t,n,lenght)
        t.lt(90)
        cross(t,n,lenght)
    

bob.lt(90)
draw_triagle(bob,10,10)
    


turtle.mainloop()