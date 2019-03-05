import random

grid = {
    'tl': ' ', 'tm': ' ', 'tr': ' ',
    'ml': ' ', 'mm': ' ', 'mr': ' ',
    'll': ' ', 'lm': ' ', 'lr': ' '
}

presentation_grid = {
    'tl': 'tl', 'tm': 'tm', 'tr': 'tr',
    'ml': 'ml', 'mm': 'mm', 'mr': 'mr',
    'll': 'll', 'lm': 'lm', 'lr': 'lr'
}

# picked_arr_items = list(range(len(grid)))

def get_grid(grid):
    print(grid['tl'] + '|' + grid['tm'] + '|' + grid['tr'])
    print('-+-+-')
    print(grid['ml'] + '|' + grid['mm'] + '|' + grid['mr'])
    print('-+-+-')
    print(grid['ll'] + '|' + grid['lm'] + '|' + grid['lr'])
    print('#' * 7)

get_grid(presentation_grid)


def random_add(grid):
    points = ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'll', 'lm', 'lr']
    while True:
        rand_index = random.randint(0, len(points) - 1)
        if grid[points[rand_index]] == 'X':
            continue
        else:
            grid[points[random.randint(0, len(points))]] = '0'
            break
    get_grid(grid)


for trial in range(5):
    user_coord = input('Add to: ')
    if user_coord == 'e':
        break
    user_item = input('Add to: ')
    if user_item != 'X':
        print('X only!')
        exit()
    try:
        if grid[user_coord] == ' ':
            grid[user_coord] = user_item[0]
        else:
            print('I need \'X\'value')
            continue
    except KeyError:
        print('I need something like: tm, tr, mr...')
        continue
    get_grid(grid)
    random_add(grid)
