import unittest


class SumTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([3, 4, 3]), 10, "result should be 10 ")

    def test_sum_list(self):
        self.assertEqual(sum((1, 3, 5,7)), 15, "result should be 16")

if __name__ == '__main__':
    # Test 2 will fail because sum of [1,3,5,7] is 16 not 15
    unittest.main()