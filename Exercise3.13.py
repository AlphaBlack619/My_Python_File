def factorial(number=int(input('enter a number: '))):
    factor = 1
    if number >= 0:
        for factorials in range(number, 1, -1):
            factor *= factorials
        print(f'The factorial of {number} is {factor}')


factorial()
