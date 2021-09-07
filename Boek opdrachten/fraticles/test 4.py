
import turtle
import math
bob = turtle.Turtle()
print(bob)

def square(t,size):
    for i in range(4):
        t.fd(size)
        t.lt(90)

def polygon(t,n,length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon_square(t,n,length):
    angle = 360 / n
    for i in range(n):
        square(t,length)
        t.fd(length)
        t.lt(angle)

def circle(t,r):
    circumference = 2 * r * math.pi
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t,n,length)


def circle_square(t,r):
    circumference = 2 * r * math.pi
    n = 50
    length = circumference / n
    polygon_square(t,n,length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length / 3) + 1
    step_lenght = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_lenght)
        t.lt(step_angle)

def arc_sun(t,n,lenght,angle):
    for i in range(n):
        arc(bob,lenght,angle)
        pos(bob,0,0)
        rot(bob,(i+1)*360/n)


def eye(t,lenght,angle):
    for i in range(2):
        arc(t,lenght,angle)
        t.lt(180-angle)
    
def flower(t,n,lenght,ang):
    angle = 360/n
    for i in range(n):
        eye(t,lenght,ang)
        t.lt(angle)

def flower_arc(t,n,lenght):
    angle = 180 + 360/n
    arc_sun(t,n,lenght,angle)

def triagle(t,lenght):
    for i in range(3):
        t.fd(lenght)
        t.lt(180-60)
    
def pos(t,x,y):  
    t.pu()
    t.setx(x)
    t.sety(y)
    t.pd()

def rot(t,angle):
    ang = t.heading() - angle
    if(ang > 0):
        t.rt(ang)
    else:
        t.lt(ang*-1)

bob.speed(100)

polygon_square(bob,30,50)
  







   

turtle.mainloop()





