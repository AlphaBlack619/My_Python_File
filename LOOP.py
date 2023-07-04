fail = 0
passes = 0
for student in range(10):
	result = int(input('enter result student? Note:1 for pass while 2 for fail '))
	if result == 1:
		passes = passes + 1
	else:
		fail = fail + 1
if passes > 8:
	print('Bonus To Teacher')
else:
	print('No Bonus To Teacher')
