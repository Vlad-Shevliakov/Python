# lambda
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



# filter
# Вернет некий filter object, который нужно будет приводить к списку через list()

numbers = [3, 12, 7, 33, 22, 11, 8]
odd_numbers = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_numbers)) # [3, 7, 33, 11]

# Можно что-то более серьезное 

str_only = filter(lambda val: type(val) is str, ['Hello', 1.2, 'Python'])
print(list(str_only)) # ['Hello', 'Python']