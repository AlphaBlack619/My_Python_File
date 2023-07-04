for d in range(10):
    print('*' * d)
print()
for b in range(10, 0, -1):
    print('*' * b)

for d in range(10):
    print()
    for b in range(10 - d):
        print(' ', end='')
    for b in range(d + 1):
        print(' ', end=' ')
    for b in range(10 - d):
        print('*', end='')
print()

for d in range(10):
    print('')
    for b in range(10 - d):
        print(' ', end='')
    for b in range(d):
        print('*', end='')
