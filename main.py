import random

grid = {
    'tl': ' ', 'tm': ' ', 'tr': ' ',
    'ml': ' ', 'mm': ' ', 'mr': ' ',
    'll': ' ', 'lm': ' ', 'lr': ' '
}

picked_arr_items = list(range(len(grid)))

def get_grid():
    print(grid['tl'] + '|' + grid['tm'] + '|' + grid['tr'])
    print('-+-+-')
    print(grid['ml'] + '|' + grid['mm'] + '|' + grid['mr'])
    print('-+-+-')
    print(grid['ll'] + '|' + grid['lm'] + '|' + grid['lr'])
    print('#' * 7)

# get_grid()

def random_add(grid, arr):
    count = 0
    for key, value in grid.items():
        if value != ' ':
            arr[count] = True
        else:
            arr[count] = key
        count += 1
    


for trial in range(5):
    get_grid()
    user_coord = input('Add to: ')
    if user_coord == 'e':
        break
    user_item = input('Add to: ')
    try:
        if grid[user_coord] == ' ':
            grid[user_coord] = user_item[0]
        else:
            continue
    except KeyError:
        print('I need something like: tm, tr, mr...')
        continue
    get_grid()
    random_add(grid, picked_arr_items)