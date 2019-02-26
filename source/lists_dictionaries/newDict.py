a = {
    'name': 'Bob',
    'pin': 1.234
}
b = dict(foo='baz')
c = dict.fromkeys(['x', 'y', 'z'], 19)
d = {a: a ** 2 for a in range(4)}

print(a)
print(b)
print(c)
print(d)

print('######')

a.clear()
print(a)

# print(b['baz']) # throw except
print(b.get('baz')) # None

print(c.keys()) #dict_keys(['x', 'y', 'z'])
print(b.values()) # dict_values(['baz'])
# If key missing -> KeyError: '...'
print(c.pop('z')) # -> 19

# print(a.popitem())  # KeyError, because a.clear()

a.setdefault('name', 'Bob')
a.setdefault('pin', 1234) # If the key is missing, it will be added.
# and if it is, it will return its value

print(a.popitem())
# a = {'name': 'Bob'}
# popitem -> ('pin', 1234)