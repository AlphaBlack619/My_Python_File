import unittest
from decimal import Decimal
from oop.bank import Bank
from oop.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('Alpha', 'Black', '*1', 'pin')
        self.bank = Bank('UBA')

    def test_deposit(self):
        self.account.deposit(Decimal('5000'))
        self.assertEqual(5000, self.account.check_account_balance('pin'))

    def test_withdraw(self):
        self.account.deposit(Decimal('5000'))
        self.assertEqual(5000, self.account.check_account_balance("pin"))
        self.account.withdraw(Decimal('3000'), 'pin')
        self.assertEqual(2000, self.account.check_account_balance("pin"))

    def test_canUpdatePin(self):
        self.account.update_pin("pin", 'NewPin')
        self.assertEqual('NewPin', 'NewPin')

    def test_canUpdateName(self):
        self.account.account_name_update("Nero", "White", 'pin')
        self.assertEqual("Nero White", self.account.get_account_name())

    def test_check_account_balance(self):
        self.assertEqual(0, self.account.check_account_balance('pin'))

    def test_get_account_number(self):
        self.assertEqual('*1', self.account.account_number)

    def test_transfer_between_inter_bank(self):
        my_bank = Bank('Alpha Limited')
        bank1 = Bank('Nero PlC')
        acct = Account('Alpha', 'Black',
                       my_bank.generate_account_number(), 'pin')
        acct1 = Account('Alpha', 'Black',
                        bank1.generate_account_number(), 'pin')
        my_bank.register_acct_app(acct)
        bank1.register_acct_app(acct1)
        acct.deposit(6000)
        self.assertEqual(6000, acct.check_account_balance('pin'))
        self.assertEqual(0, acct1.check_account_balance('pin'))
        print(acct.account_number)
        print(acct1.account_number)
        acct.transfer(3000, acct1.get_account_number(), bank1, 'pin')
        self.assertEqual(acct.check_account_balance('pin'), 3000)
        self.assertEqual(acct1.check_account_balance('pin'), 3000)
        new_acct = bank1.register_acct_bank('Lucia', 'White',  'pin')
        acct1.transfer(2000, new_acct.account_number, bank1, 'pin')
        self.assertEqual(1000, acct1.check_account_balance('pin'))
        self.assertEqual(2000, new_acct.check_account_balance('pin'))
