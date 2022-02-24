print ("Hello, world")

def outer():
    def inner():
        print('This is inner.')
    print('This is outer, returning inner.')
    return inner

i = outer()
type(i)
i()

def myfunc(*args):
    for a in args:
        print(a + ' ')
    if args:
        print()

myfunc('10')
myfunc()
myfunc('10', '20', '30')

'''  First comment  '''

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

myfunc2(a=10, b=20)
