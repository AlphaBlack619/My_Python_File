import unittest
from decimal import Decimal

from oop.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('Alpha', 'Black', Decimal('00.00'), '*1', 'pin')

    def test_deposit(self):
        self.account.deposit(Decimal('5000'))
        self.assertEqual(5000, self.account.account_balance)

    def test_withdraw(self):
        self.account.deposit(Decimal('5000'))
        self.assertEqual(5000, self.account.account_balance)
        self.account.withdraw(Decimal('3000'), 'pin')
        self.assertEqual(2000, self.account.account_balance)

    def test_canUpdatePin(self):
        self.account.update_pin("pin", 'NewPin')
        self.assertEqual("NewPin", self.account.account_pin)

    def test_canUpdateName(self):
        self.account.account_name_update("Nero", "White", 'pin')
        self.assertEqual("Nero White", self.account.get_account_name())

    def test_check_account_balance(self):
        self.assertEqual(0, self.account.check_account_balance('pin'))

    def test_get_account_number(self):
        self.assertEqual('*1', self.account.account_number)

    def test_values(self):
        self.assertRaises(ValueError, self.account.deposit, -1)
        with self.assertRaises(ValueError):
            self.account.deposit(-5)

