# Unpack function arguments

def simple(*args):
    print(args)
    return sum(args)

print(simple(2, 2, 3, 5, 7)) # -> 19

# But, if i want transfer single argument to <simple func>, I will take error.

try:
    simple([1, 1, 1, 2]) # tuple с одним аргументом
except TypeError as err_mess:
    print(err_mess)
# We need to unpack list values
simple(*[12, 33, 21]) # -> 66
# simple('Don\'t do that!')


# Kwargs both

def all_kwargs(**kwargs):
    print(kwargs)

all_kwargs(name = 'Rick', id = 'C137') # {'name': 'Rick', 'id': 'C137'}

obj = {
    'color': 'limegreen',
    'online': True,
    'status': 'Guru'
}

try:
    all_kwargs(obj)
except TypeError as err_mess:
    print(err_mess)

all_kwargs(**obj) # return all keys and values