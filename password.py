password = len(input())
if password < 6:
	print("password is too short")
if password < 20 & password >= 6:
	print(password * "*")
if password >= 20:
	print("password is too long")
