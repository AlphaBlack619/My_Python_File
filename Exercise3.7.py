print(f'Number\t\t\tSquare\t\t\tCube')
for x in range(6):
    print(f'{x:>4}\t\t\t{x * x:>6}\t\t{x * x * x:>8}', end="\n")
from multiplication_function import multiplication_table
multiplication_table(10)