def finder(number):
    x = 0
    y = 0
    t = 0
    for num in range(len(number)):
        x = int(number[num])
        if x > y:
            t = y
            y = x
    return t


def checker(number):
    xyz = ''
    for num in range(len(number)):
        if number[num].isdigit():
            xyz += number[num]
    return xyz


def second_highest_number_finder(argument):
    z = finder(checker(argument))
    x = 0
    y = 0
    t = 0
    prin = checker(argument)
    for num in range(len(prin)):
        x = int(prin[num])
        if x >= y:
            t = y
            y = x
    if t == y:
        return '-1'
    return z


print(second_highest_number_finder('dfa12321adf'))
print(second_highest_number_finder('abc11111'))
