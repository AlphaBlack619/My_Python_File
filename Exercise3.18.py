for x in range(10):
    for y in range(x + 1):
        print('*', end='')
    for y in range(10 - x):
        print(' ', end='')
    print(' ', end=' ')
    for y in range(10 - x):
        print('*', end='')
    print('', end='')
    for y in range(x + 1):
        print(' ', end=' ')
    for y in range(10 - x):
        print('*', end='')
    for y in range(10 - x):
        print(' ', end='')
    print(' ', end=' ')
    for y in range(x + 1):
        print('*', end='')
    print('')
