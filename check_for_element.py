array = ['okon', 2, 'victor', 56, 'nero']


def check(element1, list):
    check = 'false'
    for element in list:
        if element == element1:
            check = 'true'
    print(check)


check(56, array)
check(8, array)
