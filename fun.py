# i = 1
# for i in range(i, 10):
#     for x in range(i):
#         print(x,end='')
#     print('')


def function_name(num1, num2, num3, num4):
    print(max(num1, num2, num3, num4))


function_name(12, 13, 14, 15)


# def greater(num1, num2, num3, num4):
#     if num1 >= num2 & num1 >= num3 & num1 >= num4:
#         print(num1)
#     elif num2 >= num1 & num2 >= num3 & num2 > num4:
#         print(num2)
#     elif num3 >= num4 & num3 >= num2 & num3 >= num1:
#         print(num3)
#     elif num4 >= num3 & num4 >= num2 & num4 >= num1:
#         print(num4)


def loop(num1, num2, num3, num4):
    a = [num1, num2, num3, num4]

    for i in a:
        for b in i:
            number = b
            small = number
            if b > number:
                number = b
            elif b < number:
                small = b
    print('highest number is =', number)
    print('smallest number is =', small)


loop(3, 4, 5, 8)
