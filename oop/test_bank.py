import unittest
from _decimal import Decimal
from oop.account import Account
from oop.bank import Bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank('Alpha')
        self.acct = Account('Alpha', 'Black',
                            self.bank.generate_account_number(), 'pin')
        self.bank.register_acct_app(self.acct)

    def test_get_bank_name(self):
        self.assertEqual('Alpha', self.bank.get_bank_name())

    def test_generate_account_number(self):
        acct_number = self.acct.get_account_number()
        self.assertEqual(acct_number, self.bank.find_account(self.acct).account_number)

    def test_register(self):
        bank = Bank('UBA')
        acct = Account('Alpha', 'Black',
                       bank.generate_account_number(), 'pin')
        bank.register_acct_app(acct)
        find_acct = acct.get_account_number()
        self.assertIsNotNone(bank.find_account_with_account_number(find_acct))

    def test_can_register_more_than_one_customer(self):
        my_bank = Bank('UBA')
        acct2 = Account('Alpha', 'Black',
                        my_bank.generate_account_number(), 'pin')
        acct1 = Account('Alpha', 'Nero',
                        my_bank.generate_account_number(), 'pin')
        my_bank.register_acct_app(acct1)
        my_bank.register_acct_app(acct2)
        find_acct = acct1.get_account_number()
        find_acct2 = acct2.get_account_number()

        self.assertIsNotNone(my_bank.find_account_with_account_number(find_acct))
        self.assertIsNotNone(my_bank.find_account_with_account_number(find_acct2))
        self.assertIsNotNone(my_bank.register_acct_bank('White', 'Black', 'pin'))

    def test_for_deposit(self):
        bank = Bank('UBA')
        acct = Account('Alpha', 'Black',
                       bank.generate_account_number(), 'pin')
        bank.register_acct_app(acct)
        bank.deposit(5000, acct.get_account_number())
        self.assertEqual(5000, acct.check_account_balance('pin'))

    def test_find_account(self):
        bank = Bank('UBA')
        acct = Account('Alpha', 'Black',
                       bank.generate_account_number(), 'pin')
        bank.register_acct_app(acct)
        find_acct = acct.get_account_number()
        self.assertIsNotNone(bank.find_account_with_account_number(find_acct))

    def test_withdraw(self):
        bank = Bank('UBA')
        acct = Account('Alpha', 'Black',
                       bank.generate_account_number(), 'pin')
        bank.register_acct_app(acct)
        acct.deposit(3000)
        bank.withdraw(1000, acct.get_account_number(), 'pin')
        self.assertEqual(2000, acct.check_account_balance('pin'))

    def test_update_pin(self):
        bank = Bank('UBA')
        acct = Account('Alpha', 'Black',
                       bank.generate_account_number(), 'pin')
        bank.register_acct_app(acct)
        bank.update_pin('pin', 'NewPin', acct.get_account_number())
        self.assertEqual('NewPin', acct.request_pin())

    def test_account_name_update(self):
        self.bank.account_name_update('Nero', 'White', 'pin', self.acct.get_account_number())
        self.assertEqual('Nero White', self.acct.get_account_name())

    def test_transfer(self):
        bank = Bank('UBA')
        bank1 = Bank('Semicolon')
        acct = Account('Alpha', 'Black',
                       bank.generate_account_number(), 'pin')
        acct1 = Account('Alpha', 'Black',
                        bank1.generate_account_number(), 'pin')
        bank.register_acct_app(acct)
        bank1.register_acct_app(acct1)
        bank.deposit(5000, acct.get_account_number())
        self.assertEqual(5000, acct.check_account_balance('pin'))
        self.assertEqual(acct1.check_account_balance('pin'), 0)
        print(acct.get_account_number())
        print(acct1.get_account_number())
        bank.transfer(3000, acct.get_account_number(), acct1.get_account_number(), bank1, 'pin')
        self.assertEqual(acct.check_account_balance('pin'), 2000)
        self.assertEqual(acct1.check_account_balance('pin'), 3000)

    def test_intra_bank_transfer(self):
        lucia_acct = Account('lucia', 'white', self.bank.generate_account_number(), 'sex')
        self.bank.register_acct_app(lucia_acct)
        lucia_acct.deposit(1000)
        self.acct.deposit(6000)
        self.bank.transfer(2550, self.acct.get_account_number(), lucia_acct.get_account_number(), self.bank, 'pin')
        self.assertEqual(3450, self.acct.check_account_balance('pin'))
        self.assertEqual(3550, lucia_acct.check_account_balance('sex'))

