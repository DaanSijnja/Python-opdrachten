#print window
def horizontal():
    print('+' + '-'*4 + '+' + '-'*4 + '+')

def vertical():
    print('|' + ' '*4 + '|' + ' '*4 + '|')

def do_four(func):
    func()
    func()
    func()
    func()
    
#main
horizontal()
do_four(vertical)
horizontal()
do_four(vertical)
horizontal()





