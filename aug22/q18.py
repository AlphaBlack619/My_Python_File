def gcd(number1, number2):
    if number1 % 2 == 0 and number2 % 2 == 0:
        return 2
    if number1 % 3 == 0 and number2 % 3 == 0:
        return 3
    if number1 % 5 == 0 and number2 % 5 == 0:
        return 5
    if number1 % 7 == 0 and number2 % 7 == 0:
        return 7
    if number1 % 2 != 0 and number2 % 2 != 0 and number1 % 3 != 0 and number2 % 3 != 0:
        print("No lowest common divisor")


print(gcd(10, 20))
