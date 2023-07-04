import getpass
while True:
    password = getpass.getpass('Enter password: ')
    if len(password.lower()) >= 8:
        print('Your password length', len(password), 'is secured')
        break
    else:
        print('invalid password length\n'
              'Enter password: ')
