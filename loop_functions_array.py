array = [1, 2, 3, 5, 6]


def total(list1):
    total1 = 0
    for index in range(len(list1)):
        total1 += list1[index]
    print('The total sum in for loop is', total1)


total(array)


def total_in_while(list1):
    total1 = 0
    index = 0
    while index in range(len(list1)):
        total1 += list1[index]
        index += 1
    print('the sum of total in while loop is', + total1)


total_in_while(array)
