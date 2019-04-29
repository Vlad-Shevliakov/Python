# Класс - объект

# Доступ к объекту с экземпляра

class Object_class(object):
    meta_data = None


ex = Object_class()
ex_v2 = Object_class()

print(ex.__class__)  #  <class '__main__.Object_class'>
print(ex.meta_data)
ex_v2.meta_data = '0x0000100'

# Недо "static" метод

Object_class.meta_data = 'x237623tebz3g'

print('New data - top to bottom {}'.format(ex.meta_data))  # x237623tebz3g
# Если метод не был перезаписан экземпляром, то этот экземпляр получит новые данные сверху вниз!

# Статические методы класса
# Ключевое слово @staticmethod перед функией*
# Функция* не принимает self

class Some_class(object):
    id = 'sd723d2sg2702s3d'
    call_counter = 0

    @staticmethod  # перед статик. функции
    def zeroing():
        print('ZERO ZERO ZERO!')        

    def __init__(self, name):
        self.name = name


bob = Some_class('Bob')
print(bob.__dict__)
  
# К статическому методу класса можно обратится через экземпляр - но в JavaScript нельзя!
# и через сам класс
Some_class.zeroing()
bob.zeroing()