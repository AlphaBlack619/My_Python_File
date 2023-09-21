from _decimal import Decimal


class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Account:
    def __init__(self, first_name: str, last_name: str, account_number: str, pin: str):
        try:
            self.__account_name = first_name + ' ' + last_name
            self.account_number = account_number
            self.__account_balance = 0
            self.__account_pin = pin
        except ValueError:
            print('Invalid value')
        except TypeError:
            print('Type Error')

    def check_account_balance(self, pin):
        try:
            if type(pin) is not str:
                raise TypeError('Invalid Value')
            if validator(self.__account_pin, pin) is True:
                return self.__account_balance
            else:
                raise CustomException
        except ValueError:
            print('Invalid value')
        except CustomException:
            print('Invalid Pin')
        except KeyboardInterrupt:
            print("You Distorted the flow of the application")

    def get_account_number(self):
        return self.account_number

    def get_account_name(self):
        return self.__account_name

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError('amount must be > to 0.00.')
            if type(amount) is not int and type(amount) is not float and type(amount) is not Decimal:
                raise TypeError('Invalid Value')
            self.__account_balance += amount
        except ValueError:
            print('amount must be > to 0.00.')
        except TypeError:
            print('Invalid Value')
        except KeyboardInterrupt:
            print("You Distorted the flow of the application")

    def withdraw(self, amount, pin):
        try:
            if amount <= Decimal('0.00'):
                raise ValueError('amount must be > to 0.00.')
            if type(amount) is not int and type(amount) is not float and type(amount) is not Decimal \
                    and type(pin) is not str:
                raise TypeError('Invalid Value')
            if validator(pin, self.__account_pin) is True and self.__account_balance > amount > 0:
                self.__account_balance -= amount
            else:
                raise CustomException('Error In Transaction!! Please Cross-Check Details Again')
        except ValueError:
            print('ValueError: amount must be > to 0.00.')
        except TypeError:
            print('TypeError: Invalid Value')
        except CustomException:
            print('Error In Transaction!! Please Cross-Check Details Again')
        except KeyboardInterrupt:
            print("You Distorted the flow of the application")

    def update_pin(self, old_pin, new_pin):
        try:
            if type(old_pin) is not str or type(new_pin) is not str:
                raise TypeError('Invalid Value')
            if validator(old_pin, self.__account_pin) is True:
                self.__account_pin = new_pin
            else:
                raise CustomException('Invalid pin')
        except ValueError:
            print("Invalid values")
        except CustomException:
            print('Invalid Pin')
        except KeyboardInterrupt:
            print("You Distorted the flow of the application")

    def account_name_update(self, first_name, last_name, pin):
        try:
            if type(first_name) is not str or type(last_name) is not str:
                raise TypeError('Invalid Value')
            if validator(pin, self.__account_pin) is True:
                new_account_name = first_name + ' ' + last_name
                self.__account_name = new_account_name
            else:
                raise CustomException('Invalid pin')
        except ValueError:
            print("Invalid values")
        except CustomException:
            print('Invalid Pin')
        except KeyboardInterrupt:
            print("You Distorted the flow of the application")

    def transfer(self, amount, receiver_acct, receiver_bank, pin):
        try:
            holder = 0
            if amount < Decimal('0.00'):
                raise ValueError('Transfer amount must be >  0.00.')
            if type(amount) is not int and type(amount) is not float and type(amount) is not Decimal:
                raise TypeError('Invalid Value')
            if amount <= self.__account_balance:
                holder = amount
                self.withdraw(amount, pin)
            from oop.bank import Bank
            if type(receiver_bank) is not Bank:
                self.__account_balance += holder
                raise CustomException('Invalid Bank')
            else:
                receiver_bank.find_account_with_account_number(receiver_acct).deposit(amount)
        except ValueError:
            print('Transfer amount must be >  0.00.')
        except TypeError:
            print('Invalid Value')
        except CustomException as error:
            print("Error:", str(error))

    def request_pin(self):
        return self.__account_pin


def validator(validater, validate):
    if validater == validate:
        return True
    else:
        return False
