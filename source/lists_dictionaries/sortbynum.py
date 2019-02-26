numbers = (1.3, 0.9, 1.7, 2.4, 7.3, 1.9, 6.3, 5.2, 3.3, 10.3, 9.0, 2.2)

def getMinAndMaxValue(arr):
    max = 0
    min = 0
    for num in arr:
        if min == 0:
            min = num
        if num > max:
            max = num
        if num < min:
            min = num

    print(min)
    print(max)

getMinAndMaxValue(numbers)