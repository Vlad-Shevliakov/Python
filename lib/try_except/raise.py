import random
try:
    if random.randint(0, 5) < 3:
        print('Hello')
    else:
        raise ValueError("0_o")
except ValueError as err:
    print(err)
else:
    print('There was no mistake!')
finally:
    print('|_ finally')

# def test():
#     try:
#         if random.randint(0, 5) < 3:
#             print('Hello')
#         else:
#             raise ValueError("0_o")
#     except ValueError as err:
#         return(1)
#         print(err)
#     else:
#         return(2)
#         print('There was no mistake!')
#     finally:
#         return('Im a boss')
#         print('|_ finally')

# # print(test()) 


try:
    raise ZeroDivisionError("0 it's 0")
except ZeroDivisionError:
    pass

def controlRaiseError():

    def getExceptons():
        s = [ValueError('ValueError'), TypeError('TypeError'), RuntimeError('RuntimeError')]
        raise s[random.randint(0, 2)]

    try:
        getExceptons()
    except ValueError as err:
        print(err)
    except TypeError as err:
        print(err)
    except RuntimeError as err:
        print(err)

# controlRaiseError()