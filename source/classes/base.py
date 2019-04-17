# Классы
class Lang:
    name = 'Python'
    environment = 'PVM'
# name и environment ---> Статические свойства самого КЛАССА
py = Lang()
print(py)   # <__main__.Lang object at 0x10e88ecc0>
print(type(py)) # <class '__main__.Lang'>

js = Lang()
js.name = 'JavaScript'
js.environment = 'browser'
print(js.name, js.environment)  # JavaScript browser


# Метод класса
class Lamp:
    def change_state(self): # ссылается на объект в методу, ну как и this
        self.state = 'ON'
        print('Self:', self)
        print('Lamp is {}'.format(self.state))

lamp = Lamp()
try:
    # Если обратится к свойству, которое будет определено только при вызове метода
    print(lamp.state )
except AttributeError as err:
    print(err) # AttributeError: 'Lamp' object has no attribute 'state'

lamp.change_state() # Неявная передача lamp.change_state(lamp)
# А теперь свойство есть
print(lamp.state) # ON

# разные экземпляры - разные self
lamp_2 = Lamp()
lamp_2.change_state()



# Метод + параметры
class Color:
    def new_color(self, color):
        self.color = color
        print(self.color) 
red = Color()
red.new_color('#f21515')


# Все вместе 
class Card:
    open = True
    _pin = 1234
    amount = 10000
    def subtract(self, num):
        user_pin = int(input('Enter yor pin: '))
        if user_pin == self._pin: 
            if self.amount >= num:
                self.amount -= num
            print(self.amount)
        else:
            print('Invalid password')
    def get_total(self):
        print(self.amount)
    def open_state(self):
        self.open = not self.open # this.isOpen = this.!isOpen(JS)
        return self.open

pb = Card()
pb.get_total() # 10000
pb.subtract(2500) # 7500
# Изменит поле open (очевидно)
pb.open_state()



class Test:
    def __init__(self, color = 'red'):
        print('Constructor is called')
        print('Self:', self)
        self.color = color

one = Test()
print(one.color) # red
two = Test('yellow')
print(two.color) # yellow


# 2
class Tree:
    value = 'Tree'
    def __init__(self, name = '0_o', count = 0):
        self.name = name
        self.count = count
    def change_count(self, num = 0):
        self.count -= num
        print(self.count)
    def do(self):
        print(self.value)
    
# Сначала ищет свое свойство/метод, если его там нет, то ищет его у родителя
class Fruit(Tree): # (что наследовать)
    pass

tree = Tree('Apple Tree', 12)
tree.change_count(2) # 10

fruit = Fruit()
print(fruit.name) # 0_o из Tree
fruit.do() # Tree

# Sub с своим __init__
class Main:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hi {}!'.format(self.name))

one = Main('One')
one.say_hi() # Hi One!

class Sub(Main):
    def __init__(self, age):
        self.age = age
    def say_hi(self):
        print('Hi!')


two = Sub(100) 
two.say_hi() # Hi!