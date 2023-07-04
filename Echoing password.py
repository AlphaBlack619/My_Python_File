import getpass
user_name = getpass.getuser()
while True:
    password = getpass.getpass('%s Enter new password: ' % user_name)
    if len(password.lower()) >= 8:
        print('Your password is secured! length', len(password), 'is valid')
        break
    else:
        print('invalid password length\n'
              'Enter valid password length: ')
password1 = getpass.getpass('\n%s Enter your new password to verify? ' % user_name)
while True:
    if password1.lower() == password:
        print('Welcome..!!!')
        break
    else:
        print('The answer entered by you is incorrect..!!!')
        password1 = getpass.getpass('Password Hint: %s Your favorite flower\nEnter password: ' % user_name)
