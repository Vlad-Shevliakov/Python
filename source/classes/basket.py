# 1 Создать класс корзина, для разных объектов, у которого можно выставить разную вместительность
# 2 Класс пакет, который тоже можно поместить предметы, у пакета тоже есть вместимость
# 3 Любой класс, который можно поместить в корзину и пакет
# 4 Если места нет — сообщить!

import copy

class Basket:
    name = 'basket'
    def __init__(self, size = 10):
        self.size = size
        self._items = []
    def add_item(self, *items):
        if len(self._items) < self.size:
            newItems = copy.deepcopy(self._items)
            for item in items:
                if len(newItems) >= self.size:
                    break
                newItems.append(item)
            self._items = newItems
            print(self._items)
        else:
            print('The {} is full'.format(self.name))
    def clear_items(self):
        self._items = []
        print('The {} is empty'.format(self.name))
    def get_info(self):
        print('{} size: {}/{}'.format(self.name, len(self._items), self.size))


class Package(Basket):
    name = 'package'
    def __init__(self, size = 5):
        self._items = []
        self.size = size

class Box(Basket):
    name = 'box'
    def __init__(self):
        self._items = []
        self.size = 3
    def packaging(self):
        pack = tuple(copy.deepcopy(self._items))
        self.clear_items()
        return pack




basket = Basket(10)
basket.add_item('Book', 'Phone', 'Pen', 'Lamp', 'Apples', 'Mouse')
basket.get_info()

print('=' * 10)

package = Package()
package.add_item('Watches', 'Laptop')
package.get_info()
package.clear_items()
package.get_info()

print('=' * 10)

box = Box()
box.get_info()
box.add_item('Sandwich', 'Cup')
box.get_info()

pack = box.packaging()

print('=' * 10)

basket.add_item(pack)