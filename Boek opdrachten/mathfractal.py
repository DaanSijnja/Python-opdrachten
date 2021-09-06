import turtle

pen = turtle.Turtle()

pen.speed(3000)
ls = []


print(ls)
def formule(n):
    
    if(n <= 1):
        return
    
    if(n % 2 == 0):
        #print('+')
        ls.insert(0,'+')
        formule(n/2)
    else:
        #print('-')
        ls.insert(0,'-')
        formule(3*n+1)

def draw_list(t,lis):
    angle_even = 2
    angle_uneven = 1
    lenght = 20

    for i in range(len(lis)):
        if(lis[i] == '+'):
            #pen.color('red')
            t.lt(angle_even)
        else:
            t.rt(angle_uneven)
            #pen.color('green')
        t.fd(lenght)

def rot(t,angle):
    ang = t.heading() - angle
    if(ang > 0):
        t.rt(ang)
    else:
        t.lt(ang*-1)

for i in range(400):

    formule(i)
    
    draw_list(pen,ls)
    ls=[]
    pen.penup()
    rot(pen,0)
    pen.setx(0)
    pen.sety(0)
    pen.pendown()


        

turtle.mainloop()
 
