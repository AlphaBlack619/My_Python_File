from account import CustomException
import random
from account import Account


class Bank:
    def __init__(self, name):
        self.name = name
        self.__list_of_account = []

    def get_bank_name(self):
        return self.name

    def generate_account_number(self):
        size = ''
        for number in range(10):
            size1 = random.randint(0, 9)
            size += str(size1)
        return self.get_bank_name() + ':' + str(size)

    def register_acct_bank(self, first_name, last_name,  pin):
        new_account = Account(first_name, last_name, self.generate_account_number(), pin)
        self.register_acct_app(new_account)
        return new_account

    def register_acct_app(self, account):
        self.__list_of_account.append(account)

    def find_account_with_account_number(self, acct_num):
        try:
            acct = None
            for account in self.__list_of_account:
                if str(account.account_number) == acct_num:
                    acct = account
                    return acct
            if acct is None:
                raise ValueError('Account Not Found')
        except ValueError:
            print('Account Not Found')

    def deposit(self, amount, acct_num):
        self.find_account_with_account_number(acct_num).deposit(amount)

    def withdraw(self, amount, acct_num, pin):
        self.find_account_with_account_number(acct_num).withdraw(amount, pin)

    def update_pin(self, old_pin, new_pin, acct_number):
        self.find_account_with_account_number(acct_number).update_pin(old_pin, new_pin)

    def account_name_update(self, first_name, last_name, pin, acct_number):
        self.find_account_with_account_number(acct_number).account_name_update(first_name, last_name, pin)

    def transfer(self, amount, sender_acct_num, receiver_acct, receiver_bank, pin):
        if type(sender_acct_num) is not str or type(receiver_acct) is not str or type(pin) is not str or \
                type(receiver_bank) is not Bank:
            raise CustomException('Please Check Transaction Details')
        try:
            self.find_account_with_account_number(sender_acct_num).withdraw(amount, pin)
            if receiver_bank.find_account_with_account_number(receiver_acct) is not None:
                receiver_bank.find_account_with_account_number(receiver_acct).deposit(amount)
            else:
                raise CustomException('Account Not Found')
                self.find_account_with_account_number(sender_acct_num).deposit(amount)
        except CustomException:
            print("Error:", str(error))

    def find_account(self, acct):
        try:
            acct1 = None
            for account in self.__list_of_account:
                if account == acct:
                    acct1 = account
                    return acct1
            if acct1 is None:
                raise CustomException('Account Not Found')
        except CustomException:
            print('Account Not Found')
