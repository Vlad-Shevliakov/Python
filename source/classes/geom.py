'''
Пользователь вводит список чисел через пробел, если ввел:
    1 число, стоим квадрат
    2 числа - прямоугольник
    3 числа - треугольник
    4 числа многоугольник (S)
Вычисляем периметр и площадь, выводим в консоль
    * можно сделать “ возможность “ построить данную фигуру с такими сторонами
'''

class Calc:
    def __init__(self, *params):
        self.queue = list(params)
        self.__start(self.queue)

    def info(self, area = 0, perimeter = 0):
        print('Area: {}m2, perimeter: {}m.'.format(area, perimeter))

    def __start(self, list):
        if len(list) == 1:
            self.__square(list)
        if len(list) == 2:
            self.__rectangle(list)
        if len(list) == 3:
            self.__triangle(list)
        if len(list) == 4:
            self.__polygon(list)



    def __square(self, list):
        # S = a2
        # P = 4a
        self.info(list[0] ** 2, list[0] * 4)

    def __rectangle(self, list):
        # S = a * b
        # P = 2 * a + b * 2 = 2(a + b)
        area = list[0] * list[1]
        perimeter = (2 * list[0]) + (list[1] * 2)
        self.info(area, perimeter)

    def __triangle(self, list):
        # S = √(p/2(p/2-a)*(p/2-b)*(p/2-c))
        # P = a + b + c
        perimeter = sum(list)

        p2 = perimeter / 2
        area = (p2 * (p2 - list[0]) * (p2 - list[1]) * (p2 - list[2])) ** 0.5
        self.info(area, perimeter)

    def __polygon(self, list):
        # S =
        # P =
        corners = []
        for _i in range(0, len(list), 2):
            corners.append((list[_i], list[_i + 1]))
        n = len(corners)  # углы
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += corners[i][0] * corners[j][1]
            area -= corners[j][0] * corners[i][1]
        area = abs(area) / 2.0
        print(area)


c = Calc(4, 8)