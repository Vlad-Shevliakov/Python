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

print(res)