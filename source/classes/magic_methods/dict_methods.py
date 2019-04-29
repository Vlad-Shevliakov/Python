# Dict itmes
# В этих методах важно возвращать значения!


class Some(object):
    def __init__(self):
        self.value = {}

    def __contains__(self, some_item):
        return some_item in self.value

    def __setitem__(self, key, value):
        if key not in self.value:
            print(key, value)
            self.value[key] = value
        else:
            print('Уже есть!')

    def __delitem__(self, key):
        print('Del', key)

    def __getitem__(self, item):
        return 'You call {}'.format(item)

    def __str__(self):  # обновление вверх -> :(
        res = 'Object: {}'.format(self.__dict__)
        print(res)
        return res

    def __len__(self):
        return 100


instance = Some()

print(1 in instance)
instance['book'] = '5th edition'
# Уже есть!
instance['book'] = 'new*'
instance.num = '10001384013749374678312632787212365221'
str(instance)
del instance['num']
print(len(instance))  # 100
print(instance.value)
