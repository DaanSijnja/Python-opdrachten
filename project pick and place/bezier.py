'''pcurrent = (1-t)^{2}P0 + 2t(1-t)P1 + t^{2}P2'''
import turtle
bob = turtle.Turtle()

def bezier_curve(Pstart,Peind,Psteun,t):
    Pcurrent = [0,0,0]
    #Psteun = [Pstart[0],Peind[1],(Pstart[2]+Peind[2])/2]
    for i in range(len(Pcurrent)):
        Pcurrent[i] = (1-t)**2 * Pstart[i] + 2*t*(1-t)*Psteun[i] + t**2 * Peind[i]
    return Pcurrent

def diff_bezier_curve(Pstart,Peind,Psteun,t):
    P_diff = [0,0,0]
    for i in range(len(P_diff)):
        P_diff[i] = 2*((1-t) * Pstart[i]) + 2*(1-t)*Psteun[i] + 2*(t * Peind[i])
    return P_diff



start = [0,0,0]
end = [0,100,0]
steun = [0,0,0]

for i in range(50):
    pr = bezier_curve(start,end,steun,i/50)
    diff_pr = diff_bezier_curve(start,end,steun,i/50)
    #print(pr)
    print('curve 1:',diff_pr)
    bob.goto(pr[0],pr[1])

start = [0,100,0]
end = [200,200,0]
steun = [0,200,0]

for i in range(50):
    pr = bezier_curve(start,end,steun,i/50)
    diff_pr = diff_bezier_curve(start,end,steun,i/50)
    #print(pr)
    print('curve 2:',diff_pr)
    bob.goto(pr[0],pr[1])


start = [200,200,0]
end = [400,100,0]
steun = [400,200,0]

for i in range(50):
    pr = bezier_curve(start,end,steun,i/50)
    diff_pr = diff_bezier_curve(start,end,steun,i/50)
    #print(pr)
    print('curve 3:',diff_pr)
    bob.goto(pr[0],pr[1])

start = [400,100,0]
end = [400,0,0]
steun = [400,0,0]

for i in range(50):
    pr = bezier_curve(start,end,steun,i/50)
    diff_pr = diff_bezier_curve(start,end,steun,i/50)
    #print(pr)
    print('curve 4:',diff_pr)
    bob.goto(pr[0],pr[1])



turtle.mainloop()