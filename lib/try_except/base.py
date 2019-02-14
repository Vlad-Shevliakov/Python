try:
    print(10 / '2')
except ValueError as err:
    print('I can\'t divide by zero')
    print(type(err))
except TypeError as err:
    print('Wrong Type')
    print(err)



def objExeptions():
    obj = {
        'name': 'Vlad'
    }
    try:
        print(obj['age'])
    except KeyError as err:
        print(err)

    # try:
    #     print(obj['num'])
    # except ZeroDivisionError as err:
    #     print(err)

    # Это несоответствующее исключение и оно не будет обработано
    
    

# objExeptions()

def listExeptions():
    ul = [1, 2, 3, 4]

    try:
        print(ul[10])
    except IndexError as err:
        print(err)

# listExeptions()