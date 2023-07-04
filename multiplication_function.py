def multiplication_table(number=int(input('enter a number: '))):
    print(f'Multiplication Table For {number} In Range Of 20')
    for x in range(21):
        print(f'            {number} x {x} = {number * x}')


multiplication_table()
