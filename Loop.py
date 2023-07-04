import random
Number = int(input("enter grade: "))
if Number < 0:
	print('its a negative number')
elif Number % 2 == 0:
	print('Its An Even')
elif Number % 2 != 0:
	print('Its an odd number')
random.seed(5)
print(random.random())
print(random.randint(35, 53))
print(random.randint(7, 9))
print(random.uniform(3, 100))
print(random.choice('Voldemort'))
# Specifying the step argument
print(random.randrange(3, 100, 5))
print(random.randrange(3, 100, 5))
print(random.randrange(3, 100, 5))
print(random.randrange(1, 5))
print(random.randrange(100))
