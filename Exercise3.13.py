def factorial(number=int(input('enter a number: '))):
    factor = 1
    if number >= 0:
        for factorials in range(number, 1, -1):
            factor *= factorials
        print(f'The factorial of {number} is {factor}')


factorial()

ee = 1
for t in range(1, 8):
    ee += 1/t
print(ee)
