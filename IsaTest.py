
def PrintLowerCase(_text):
    print(str.lower(_text))

def PrintText(_text):
    print(_text)

def print_twice(banan):
    print(banan)
    print(banan)


def do_twice(_func, _arg):
    _func(_arg)
    _func(_arg)

def do_four(_func,_arg):
    do_twice(_func,_arg)
    do_twice(_func,_arg)


do_four(PrintText,"Banaan")



