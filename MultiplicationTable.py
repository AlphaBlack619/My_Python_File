for b in range(1, 13):
    print(end=' ')
    print(f'{b:>7}', end='\t\t\t')
print()
print('_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________\n')
for c in range(1, 13):
    print()
    for d in range(1, 13):
        print(f'{c:>3} X {d:<3}=  {c*d:<3}', end='\t\t')
    print('\n')
    