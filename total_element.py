array = [1, 2, 3, 5, 6]


def total(list):
    total = 0
    for index in range(len(list)):
        total += list[index]
    print('The total sum is', total)


total(array)
