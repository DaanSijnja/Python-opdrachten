def line(a):
    print("+" + '-+'*a)

def line_sec(a):
    print("| " + '| '*a)
    print("+" + '-+'*a)
  
def grid(a,b):
    line(a)
    i = 0
    for i in range(b):
        line_sec(a)
        

grid(2,2)

