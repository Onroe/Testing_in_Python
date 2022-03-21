import unittest

from my_sum import add
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list(self):
        data = [3, 4, 3]
        result = add(data)
        self.assertEqual(result,10)

    def test_list_fraction(self):
        list = [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)]
        result = add(list)
        self.assertEqual(result,2)
        

if __name__ == '__main__':
    unittest.main()