class BankAccount:
    def __init__(self, val):
        self.set_balance(val)

    def get_balance(self):
        return self.__balance

    def set_balance(self, val):
        if val >= 0:
            self.__balance = val
        else:
            raise ValueError("Invalid amount")

    def deposit(self, val):
        if val > 0:
            self.__balance += val
        else:
            raise ValueError("Deposit must be positive")

    def withdraw(self, val):
        if 0 < val <= self.__balance:
            self.__balance -= val
        else:
            raise ValueError("Cannot withdraw that amount")


from unittest import TestCase
class Test(TestCase):
    def setUp(self):
        self.bank_account = BankAccount(10)

    def test_get_balance(self):
        self.assertEqual(self.bank_account.get_balance(), 10)

    def test_set_balance(self):
        self.bank_account.set_balance(5)
        self.assertEqual(self.bank_account.get_balance(), 5)

    def test_set_balance_negative(self):
        with self.assertRaises(ValueError):
            self.bank_account.set_balance(-5)

    def test_deposit(self):
        self.bank_account.deposit(5)
        self.assertEqual(self.bank_account.get_balance(), 15)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-15)

    def test_withdraw(self):
        self.bank_account.withdraw(10)
        self.assertEqual(self.bank_account.get_balance(), 0)

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-5)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(20)


