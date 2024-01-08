# tests/test_max_integer.py
import unittest
from your_module import max_integer  # Replace 'your_module' with the actual module name

class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 5, 8, 2]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -7]), -1)
        self.assertEqual(max_integer([-10, -2, -8, -3]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 3, -7]), 5)
        self.assertEqual(max_integer([-10, 2, -8, 3]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.9]), 3.9)
        self.assertEqual(max_integer([-1.5, -2.7, -3.9]), -1.5)

if __name__ == '__main__':
    unittest.main()

