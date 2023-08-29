import os
from typing import TextIO

with open('account_file.txt', mode='w') as account_file:
    account_file.write('100 jones 24.98\n')
    account_file.write('200 Doe 345.67\n')
    account_file.write('300 White 0.00\n')
    account_file.write('400 Stone -42.16\n')
    account_file.write('500 Rich 224.62\n')
    print('600 Alpha 244.88', file=account_file)
    account_file.close()
with open('account_file.txt', mode='r') as account_file:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record in account_file:
        account_file, name, balance = record.split()
        print(f'{account_file:<10}{name:<10}{balance:>10}')
account_file = open('account_file.txt', 'r')
temp_file = open('temp_file.txt', 'w')
with account_file, temp_file:
    for record in account_file:
        account_file, name, balance = record.split()
        if account_file != '300':
            temp_file.write(record)
        else:
            new_record = ' '.join([account_file, 'Williams', balance])
            temp_file.write(new_record + '\n')
print()
with open('temp_file.txt', mode='r') as temp_file:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record in temp_file:
        temp_file, name, balance = record.split()
        print(f'{temp_file:<10}{name:<10}{balance:>10}')
os.remove('account_file.txt')
os.rename('temp_file.txt', 'alpha.txt')
