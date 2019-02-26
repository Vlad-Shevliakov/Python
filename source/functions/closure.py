# closure

# 1

def func(arg):
    def get_symbol():
        print('*' * len(str(arg)))
        print('$' * len(str(arg)))
    get_symbol()
    print(arg)
    get_symbol()

func({ 'id': 'c127a2', 'is_dev': True })

# 2

def main(value):
    def sub():
        print(value)
    return sub


res = main('Hello')


print(res()) # Hello

# ____ recursion

  # |_ factorial
  # |_ count

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))

def counter(n):
    if n < 0:
        return
    print(n)
    counter(n - 1)


counter(10)