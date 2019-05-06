# lambda функции
# Как анонимная функция в JavaScript!

f = lambda: print('lambda')
f()

# Принимает параметры 
# Позиционные: f(1, 2, 3, 'abc') -> *args => tuple()
# Именованные: **kwargs f(name='Nama', age=100) => dict()
# По умолчанию: x = 10, y = 10

f = lambda x, y: print(x ** y)
f(2, 2) # 4

# По умолчанию в ней работает return

f = lambda: 10
print(f()) # 10

# Это пригодится здесь! 
# reduce, map и filetr должны получить от 1-го аргумента
# и должны что-то возвращать


# 1. map(func, collection)
# Вернет некий map object, который нужно будет приводить к списку через list()
# Функция func будет применена для каждого элемента коллекции

tag_names = ['img', 'br', 'hr']

def get_tag(value):
    return '</{}>'.format(value)

tag_list = map(get_tag, tag_names)
print(tag_list) # <map object at 0x10a1d8278>
# Но есть функция list()
print(list(tag_list)) # ['</img>', '</br>', '</hr>']

# А теперь вместе с lambda

some_list = map(lambda el: '<{}></{}>'.format(el, el), ['p', 'a', 'h1'])
print(list(some_list)) # ['<p></p>', '<a></a>', '<h1></h1>']



# filter(func, collection)
# Вернет некий filter object, который нужно будет приводить к списку через list()

numbers = [3, 12, 7, 33, 22, 11, 8]
odd_numbers = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_numbers)) # [3, 7, 33, 11]

# Можно что-то более серьезное 

str_only = filter(lambda val: type(val) is str, ['Hello', 1.2, 'Python'])
print(list(str_only)) # ['Hello', 'Python']



# reduce
# reduce(func, collection, [optional initial value])
#        func (accaccumulator, nex value)

# Гвидо Ван Россум не любит reduce!
# Поэтому удалил его из стандартной библиотеки Python
# reduce() - не возвращает reduce object, он вернет результат каких-либо вычислений.
# Это значит что он неплохой в связке с map(), в последовательности map() -> then -> reduce()

from functools import reduce

nums = [1, 3, 99, 8]

def foo(x, y):
    print(x, y)
    return x + y

# Поэтапно функция foo()
# 1. x = 1 а y = 3
# 2. 4 (4 - это возвращенная сумма предыдущих 1 и 3) а 99 - следующее
# и так далее: 103 и 8
# В конце, результат равный 111!

nums_sum = reduce(foo, nums)

print(nums_sum) # 111

people = [
    {'name': 'Bob'},
    {'name': 'Roy'},
    {'name': 'Anna'},
    {'name': 'Brian'},
]

def checked_human(count, human):
    # 1 ит count = 0
    print(human['name'])
    return count + 1


people_counter = reduce(checked_human, people, 0)
print('All people: {}'.format(people_counter)) # All people: 4