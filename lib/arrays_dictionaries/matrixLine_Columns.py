matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

def line():
    for l in matrix:
        print(l)
    print('############')

line()


def columns(matrix):
    # if length more than 3 in array
    for some in matrix:
        if len(some) > 3:
            print('Line length not more than 3: {}'.format(some))
            return None
    
    ind = 0
    count = 0
    iterCount = 0
    while True:
        if iterCount > 2:
            break
        for x in matrix:
            if count == len(matrix):
                ind += 1
                count = 0
            print(x[ind])
            count += 1
        iterCount += 1
        print('####')


columns(matrix)