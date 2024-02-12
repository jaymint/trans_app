""" 
Sample Tests

"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5,8)
        self.assertEqual(res,13)

    def test_substract_numbers(self):
        res = calc.substract(10,15)
        self.assertEqual(res,5)