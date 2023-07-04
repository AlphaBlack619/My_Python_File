Number = int(input("enter grade: "))
if  Number < 0:
	print('its a negative number')
elif Number % 2 == 0:
	print('Its An Even')
elif Number % 2 != 0:
	print('Its an odd number')
