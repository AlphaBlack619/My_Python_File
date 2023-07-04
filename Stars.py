from operator import length_hint


def triangle(number):
    for x in range(number):
        for y in range(x + 1):
            print('#', end='')
        for y in range(10 - x):
            print(' ', end='')
        print(' ', end=' ')
        for y in range(10 - x):
            print('#', end='')
        print('', end='')
        for y in range(x + 1):
            print(' ', end=' ')
        for y in range(10 - x):
            print('#', end='')
        for y in range(10 - x):
            print(' ', end='')
        print(' ', end=' ')
        for y in range(x + 1):
            print('#', end='')
        print('')


print('The length of the triangle is ', length_hint(triangle(10)))
