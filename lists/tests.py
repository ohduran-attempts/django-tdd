"""
This file demonstrates writing tests using the unittest module.
They will pass when you run 'manage.py test'
"""
from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """Test that 1 + 1 always equals 2."""
        self.assertEqual(1+1, 2)
