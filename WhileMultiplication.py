a = 1
while a < 13:
    print()
    a = a + 1
    for b in range(1, 13):
        print(f'{a:<2} X {b:<2} = {a * b:>3}', end='\t\t')
