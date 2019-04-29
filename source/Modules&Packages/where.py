from my_package.data_module import Card, rec_factorial, NAME

# для проверки отличия __name__ от data_module.py
# print(__name__) -> my_package.data_module
# что в корне отличается от __main__

# Доступ к глобальной переменной 
print(NAME)

one = Card()
print(one.__dict__)

res = rec_factorial(5)
print(res)
