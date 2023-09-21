from oop.bank import Bank
from centeral_bank_of_alpha import CentralBank

central_bank = CentralBank('Nero Central Bank')
alpha_plc_nigeria = Bank('Alpha Plc Nigeria')
central_bank.register_bank(alpha_plc_nigeria)


def bank_welcome_menu():
    try:
        user_input = input("Welcome to Alpha Plc Nigeria\n1-> Open Account\n2-> Check balance"
                           "\n3-> Withdraw\n4-> Deposit\n5-> Exit application\n")
        if user_input == "1":
            first = input('Thanks for wanting to open an a'
                          'ccount with us, We hope to serve you better\nEnter first name:\n')
            last = input('Enter last name:\n')
            pin = input('Enter pin:\n')
            global alpha_plc_nigeria
            acct = alpha_plc_nigeria.register_acct_bank(first, last, pin)
            acct_num = acct.get_account_number()
            print('Your Account Number is ' + acct_num)
        elif user_input == '2':
            withdraw()
    except KeyboardInterrupt:
        print('You ForceFul Exit Application')


def withdraw():
    try:
        acct_number = input('Enter Account Number: \n')
        withdraw_bank = input('Enter Your bank:\n')
        pin = input('Enter your pin:\n')
        amount = input('enter Amount:\n')
        for banks in central_bank.bank_list:
            bank = central_bank.search_for_banks(withdraw_bank)
            bank.withdraw(amount, acct_number, pin)
    except KeyboardInterrupt:
        print('You ForceFul Exit Application')


bank_welcome_menu()
