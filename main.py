def one(title = 'Python', x = '####'):
    print('Hello {}!'.format(title))
    print(x)


# one('Python') #Hello Python! ####

def getAruments(*args):
    print(args) # <class 'tuple'>

# getAruments('JavaScript', 'Python', 'Golang', 'Rust')



def getTypleSumm(*args):
    summ = 0
    for num in args:
        if type(num) == type(1) or type(num) == type(1.2):
            # пока хз как в питоне 
            summ += num
    print(summ)

getTypleSumm(1.2, 3, '99', 18, 'hello', 4, {'x': 12}, [1, 3], None)