# Декораторы
# Декоратор - функция которая принимет на вход функцию и возвращает новую фук

def decor(func):
    print('Name func:', func.__name__)
    def inner(x, y):
        res = func(x, y)
        print('Result: {}'.format(res))
        return res
    return inner

def sum_xy(x, y):
    return x + y

def mult_xy(x, y):
    return x * y

# f получит inner
f = decor(sum_xy)
f_res = f(9, 1) # Result: 10
print(f_res) # 10

# Для объявления декоратора в Python необходимо указать @[имя функции]

def to_html(func):
    def inner(tag, text_content):
        # любая логика
        res = '<{}>{}</{}>'.format(tag, text_content, tag)
        func(res, res)
        return res
    return inner

@to_html
def foo(tag, text_content):
    print('Done')

res = [
    foo('a', 'google'),
    foo('p', 'Title'),
]

print(res) # ['<a>google</a>', '<p>Title</p>']