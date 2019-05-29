# sort -> mutable
# sorted -> immutable

arr = [
    'am',
    'in',
    'I',
    '2019'
]


def num_char_sort(string):
    return len(string)


new_arr = sorted(arr, key=num_char_sort)

print(new_arr)
print(arr)  # тот же самый


arr.sort(key=num_char_sort)  # return None
# reverse=True - по убыванию, но сильно жрет CPU
# лучше default sort, а затем reverse()

print(arr)

# test


def sub_second(sub_list):
    return sub_list[1]


some = [
    [1, 2, 3],
    [2, 1, 3],
    [4, 0, 1]
]

some.sort(key=sub_second)

print(some)
