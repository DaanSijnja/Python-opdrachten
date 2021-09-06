'''Waarheidstabel'''
import operator as op

def waarheid(p):
    '''waarheidstabel geprint'''
    print(str(p))
    print('False, False == ' + str(p(False,False)))
    print('True, False == ' + str(p(True,False)))
    print('False, True == ' + str(p(False,True)))
    print('True, True == ' + str(p(True,True)))

def waarheid_fruitfull(p):
    '''waarheidstabel als array'''
    result = [[False,False,0],[True,False,0],[False,True,0],[True,True,0]]
    for i in range(4):
        result[i][2] = p(result[i][0],result[i][1])
    
    return result


''''print or_ and_ en xor'''
waarheid(op.or_)
waarheid(op.and_)
waarheid(op.xor)

print(waarheid_fruitfull(op.xor))


