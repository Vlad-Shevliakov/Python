
ol = [12, 22, 45, 7646, 31, 22]

def sortIntList(list):
    for ind, num in enumerate(list):
        if isinstance(num, int):
            continue
        raise ValueError('not item: {}'.format(ind + 1))
    sortList = sorted(list, key = int)
    return sortList

sortIntList(ol)

# print(sortIntList(ol))


def getStringDict(obj):
    newObj = {}
    for key, value in obj.items():
        if isinstance(value, str):
            continue
        newObj[key] = str(value)
    return newObj # -> {'name': 'Rick', 'age': '70', 'id': 'C-137', 'isPortalReady': 'True'}

# getStringDict({
#     'name': 'Rick',
#     'age': 70,
#     'id': 'C-137',
#     'isPortalReady': True
# })


def composition(*numbers):
    res = numbers[0]
    if 0 in numbers:
        return
    for num in numbers:
        res *= num
    print(res)

composition(1, 2, 3, 4, 5)