# super() - ссылка на родительский класс
# Позволяет не переопределять а ссылаться вызывать!


author = 'super()'

class Top(object):
    def __init__(self, color = 'limegreen'):
        print('Top __init__')
        self.color = color

    def ml(self):
        return self.color * 2


class Middle(Top):
    def ml(self):
        return 'Middle'


class Sub(Middle):
    def __init__(self, color, num):
        super().__init__(color)  # без self, будет смотреть сквозь Middle
        self.num = num
        print(self.color)

    def ml(self):
        res = super().ml()
        print(res)
        return len(res) > self.num


x = Top('Red')
y = Sub('White', 10)
# Порядок разрешения методов - method resolution order
print(Sub.__mro__)
# (<class '__main__.Sub'>, <class '__main__.Middle'>, <class '__main__.Top'>, <class 'object'>)
# Первый найденный в цепочке метод будет выполнен!

print(y.ml())
