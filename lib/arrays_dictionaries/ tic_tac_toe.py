grid = {
    'tl': ' ', 'tm': ' ', 'tr': ' ',
    'ml': ' ', 'mm': ' ', 'mr': ' ',
    'll': ' ', 'lm': ' ', 'lr': ' '
}

def get_grid():
    print(grid['tl'] + '|' + grid['tm'] + '|' + grid['tr'])
    print('-+-+-')
    print(grid['ml'] + '|' + grid['mm'] + '|' + grid['mr'])
    print('-+-+-')
    print(grid['ll'] + '|' + grid['lm'] + '|' + grid['lr'])

get_grid()

for i in grid:
    where = input('Where to insert: ')
    what = input('What to insert: ')
    try:
        if grid[where] == ' ':
            grid[where] = what
        else:
            continue
    except KeyError:
        print('I need something like: tm, tr, mr...')
        continue
    get_grid()