"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from subscription.forms import SubscriptionForms
from subscription.validators import CpfValidator


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class SubscriptionTest(TestCase):
    def test_cpf_integer(self):
        
