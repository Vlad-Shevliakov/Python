NAME = "VLAD"

class Card(object):
    def __init__(self):
        self.card_num = '1234 5678 9101 1121'
        __pin = 4321
    
    def get_pin(self, pin):
        if self.__pin == pin:
            print('Your pin: {}'.format(self.__pin))

def rec_factorial(n):
    if n == 1: return 1
    return n * rec_factorial(n - 1)

def get_fact_result(n):
    print(rec_factorial(n))


# get_fact_result(5) # будет выполнена при import куда-либо

print(__name__)

if __name__ == '__main__':
    get_fact_result(5)