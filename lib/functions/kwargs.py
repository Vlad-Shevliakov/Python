def func(func, arg):
    print(func(arg)) # -> 9


# func(len, 'undefined')


def together(val, *other, **keywords):
    print(val) # -> 'firts'
    print(other) # -> ('a', 'b', 'c')
    print(keywords)


# together('firts', 'a', 'b', 'c', id = 137)


def dec(val):
    def _insideFunction():
        print('Value: {val}, new value: {new_val}'.format(new_val = new_val, val = val))
    new_val = str(val * 100)
    _insideFunction()
    return new_val

# dec(25)


def dec1(func):
    def _insideFunction(val):
        print(func(val))
    print('called')
    return _insideFunction

_dec = dec1(len)

# _dec((1, 2, 3))


def giveMeAll(*other, **kwargs):
    print(other)
    print(kwargs)

giveMeAll('foo', 'baz', id = 137)