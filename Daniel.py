for x in range(5):
    for y in range(5 - x):
        print(' ', end='')
    for k in range(x + 1):
        print('*', end='')
    for k in range(k):
        print('*', end='')
    print()
for y in range(5):
    for x in range(y + 1):
        print(' ', end='')
    for x in range(5 - y):
        print('*', end='')
    for z in range(x):
        print('*', end='')
    print()