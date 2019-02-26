# How I can unpack values?
# with only iterable things  

names = ['Steve', 'Mark', 'Bill', 'Jeff']

def simple():
    first, second = ('Mark', 'Bill') # if names => ValueError
    print(first, second)
    return first, second



print(simple()) # -> ('Mark', 'Bill')

# Unpacking with strings!

def unpc_str(string):
    # like in JavaScript destructions operator
    # [f, ...other] = 'Hello'
    first_symbol, *other = string
    return (first_symbol, other)

print(unpc_str('Facebook')) # -> ('F', ['a', 'c', 'e', 'b', 'o', 'o', 'k'])

# This is applicable when returning more than <<TWO>> values from a function.
_1th, _ = unpc_str('IBM')
print(_1th, _) # -> I ['B', 'M']
# :) const [ state, changeState ] = useState({ count: 0 })
# 0_o


# Unpack with middle value

def unpack_with_middle(string):
    first, *middle, last = string
    return first, middle, last


print(unpack_with_middle('F##k')) # -> ('F', ['#', '#'], 'k')