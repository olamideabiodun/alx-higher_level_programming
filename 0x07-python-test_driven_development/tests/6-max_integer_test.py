#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_one(self):
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1, 6, 4,]), 6)
        self.assertEqual(max_integer([6, 4]), 6)
        self.assertEqual(max_integer([6, 4, 5]), 6)
        self.assertEqual(max_integer([1, 3, 7]), 7)

    def test_empty_input(self):
        result = max_integer([])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
