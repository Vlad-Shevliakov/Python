arr = [9, 4, 5, 67, 1.1, 2, 3.4, 54, 46]


def getMinMaxValue(args):
    res = sorted(args, key = int)
    print('Min: {}\nMax: {}'.format(res[0], res[len(args) - 1]))


# getMinMaxValue(arr)


def caseSwitcher(string, isUpCase = False):
    newString = ''
    if isUpCase:
        for substr in string:
            newString += substr.upper()
        return newString
    else:
        for substr in string:
            newString += substr.lower()
        return newString

# print(caseSwitcher('I love Python!'))



def pyConcat(*strings, glue = ' : '):
    newString = ''
    for substr in strings:
        if len(substr) >= 3:
            newString += (substr + glue)
    return newString 


# print(pyConcat('So', 'i\'m', 'sure', 'what', 'you', 'don\'t', 'know', 'what', 'is', 'GC'))