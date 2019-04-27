# При сложении объекта!
class No(str):
    def __add__(self, other):
        return str(self) + str(other)

n = No()
# через метод __add__ -> self (экземпляр) + str(10)
res = n + 10
print(res)
print(type(res)) # <class 'str'>