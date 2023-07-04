display = """Function Menu\n(1) Phonebook \n(2) Messages \n(3) Chat \n(4) CallRegister\n(5) Tones \n(6) Setting
(7) Call Divert \n(8) Reminder \n(9) Calculator \n(10) Clock\n(11) Sim Services \n(12) Profile
(13) Game \n"""
a = '(1) Phonebook'
b = '(2) Messages '
c = 'n(3) Chat '
print(display)


def a1():
    return a


def function(command=input('function Menu: ')):
    if command == '1':
        input(a1)
    elif command == '2':
        print(b)
    elif command == '3':
        print(c)
    else: print('invalid command')


def back(back_command = input('0 for back: ')):
    return display


function()
back()