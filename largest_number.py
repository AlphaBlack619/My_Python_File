array = [100, 14, 101, 19, 90]


def largest(list1):
    maximum = list1[0]
    for element in list1:
            if element > maximum:
                maximum = element
    print('Largest number is', maximum)


largest(array)
