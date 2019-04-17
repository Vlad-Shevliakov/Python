class Bank(object):
    name = 'PB Bank inc.' # -> статика
    def __init__(self):
        self.id = 'awy1xvgh12356hwd'
        self._employees = 9763 # _ для людей 
        self.__money_transport = '11:30 AM' # __ для Python
        self.__pin = 9999
    def change_transport_time(self, pin, new_time):
        if self.__pin == pin:
            self.__money_transport = new_time
        else:
            print('Invalid password!')
    def get_transport_time(self, pin):
        if self.__pin == pin:
            # внутри есть доступ
            print('Time: {}'.format(self.__money_transport))
            return self.__money_transport
        else:
            print('Invalid password!')

bank = Bank()
print(bank.name, bank.id)
print(bank._employees)

try:
    print(bank.__money_transport)

except AttributeError as err:
    print(err) # 'Bank' object has no attribute '__money_transport'

bank.change_transport_time(9999, '4:00 PM')
bank.get_transport_time(9999)