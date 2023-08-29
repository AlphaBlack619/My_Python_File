def validator(data_list, number):
    checker = ''
    for element in data_list:
        if element == number:
            checker = 'true'
            break
        else:
            checker = 'false'
    print(checker)


list1 = [1, 2, 3, 4, 5, 6]
validator(list1, -5)
