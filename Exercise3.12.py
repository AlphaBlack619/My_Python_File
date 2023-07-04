numbers = int(input('Enter Five Integer Number: '))
number1 = numbers // 10000 % 10
number2 = numbers // 1000 % 10
number3 = numbers // 100 % 10
number4 = numbers // 10 % 10
number5 = numbers % 10
if number1 == number5 and number2 == number4:
    print("Number is a palindrome")
else:print("Number is not a palindrome")
