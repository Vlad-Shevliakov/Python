# угадай мое число
import random

secret_number = random.randint(1, 20)
print('Я загадал число, от 1 до 20!')

for countOfTry in range(1, 7):
    try:
        answer = int(input('Твой вариант:  '))
    except ValueError:
        print('Нужно только число!')
        continue
    if answer > secret_number:
        print('Нужно число поменьше!')
    elif answer < secret_number:
        print('Нужно число по больше!')
    else:
        break

if secret_number == answer:
    print('Ты угадал, это было число ' + str(secret_number) + ', ты угадал на ' + str(countOfTry) + ' попытке')
else:
    print('Ты был близко, но я загадал ' + str(secret_number) + '!')