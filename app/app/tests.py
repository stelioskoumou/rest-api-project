from django.test import TestCase
from calc import addition

class CalcTests(TestCase):

    def test_add_nums(self):
        self.assertEqual((addition(3,8), 11))