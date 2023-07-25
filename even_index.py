array = ['come', 'alpha', 12, 14, 'chibuzor']


def even(list):
    for index in range(len(list)):
        if index % 2 == 0:
            print(list[index], end=' ')


even(array)
