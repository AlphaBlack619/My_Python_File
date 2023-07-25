array = [12, 23, 56, 88, 'come', 'go']


def odd(list):
    for i in range(len(list)):
        if i % 2 != 0:
            print(list[i], end=' ')


odd(array)
