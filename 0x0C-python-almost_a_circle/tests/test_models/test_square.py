#!/usr/bin/python3
"""Tests the square"""


import io
import sys
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Square(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_two_args(self):
        s1 = Square(10)
        s1 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)
