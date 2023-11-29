#!usr/bin/python3
"""Unit test for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([8, 9, 3]), 9)
        self.assertEqual(max_integer([8, 2, 5]), 8)
        self.assertEqual(max_integer([5, 9, 9]), 9)
        self.assertEqual(max_integer([6, 8, -9]), 8)
        self.assertEqual(max_integer([6, -5, -9]), 6)
        self.assertEqual(max_integer([-1, -5, -9]), -1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([4]), 4)
    
    def test_error(self):
        """Tests if max_integer is not a list"""
        with self.assertRaises(TypeError):
            max_integer(2)


    def test_empty_input(self):
        """Tests if max_integer is called with empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    if __name__ == '__main__':
        unittest.main()
