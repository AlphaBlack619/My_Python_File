def reverse():
    first_name = input('Enter first name\n')
    last_name = input("Enter last name\n")
    total = ''
    x = len(first_name)
    b = len(last_name)
    while x > 0:
        total += first_name[x - 1]
        x -= 1
    total += " "
    while b > 0:
        total += last_name[b - 1]
        b -= 1
    print(total)


reverse()
