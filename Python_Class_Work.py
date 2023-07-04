first = input('enter first name: ')
if "".__eq__(first):
    print('invalid name')
second = input('enter second name: ')
if len(second) == 0:
    print('invalid name')
last = input('enter last name: ')
if len(last) == 0:
    print('invalid name')
    exit()
age = int(input('enter age: '))
if age < 0:
    print("you can't input negative number")
elif age in range(18,65):
    print('You are a citizen')
elif age > 65:
    print('You are older')
