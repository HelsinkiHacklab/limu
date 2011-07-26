"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from tilit.models import Account

class AccountTest(TestCase):
    def setUp(self):
        "Create two accounts: one with balance of 20 and one with balance of 0."
        self.account1=Account.objects.create(name="Account 1",balance=20)
        self.account2=Account.objects.create(name="Account 2",balance=0)
    def test_deposit(self):
        "Deposit 10 euros on both accounts and check balance."
        self.account1.deposit(10)
        self.account2.deposit(10)
        self.assertEqual(self.account1.balance, 30)
        self.assertEqual(self.account2.balance, 10)
    def test_withdraw(self):
        "Withdraw 10 euros from both accounts and check balance."
        self.account1.withdraw(10)
        with self.assertRaises(ValueError):
            self.account2.withdraw(10)
        self.assertEqual(self.account1.balance, 10)
        self.assertEqual(self.account2.balance, 0)
    def test_negatives(self):
        "Test that trying to withdraw or deposit negative sums don't work."
        with self.assertRaises(ValueError):
            self.account1.deposit(-10)
        with self.assertRaises(ValueError):
            self.account2.withdraw(-10)
        self.assertEqual(self.account1.balance,20)
        self.assertEqual(self.account2.balance,0)
