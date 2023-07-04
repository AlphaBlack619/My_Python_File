counter = 1
while counter < 6:
    numbers = int(input('enter five digit integer: '))
    number1 = numbers // 10000 % 10
    counter += 1
    print(number1,)
    number2 = numbers // 1000 % 10
    counter += 1
    print(number1, number2,)
    number3 = numbers // 100 % 10
    counter += 1
    print(number1, number2, number3)
    number4 = numbers // 10 % 10
    counter += 1
    print(number1, number2, number3, number4)
    number5 = numbers % 10
    counter += 1
    print(number1, number2, number3, number4, number5)
