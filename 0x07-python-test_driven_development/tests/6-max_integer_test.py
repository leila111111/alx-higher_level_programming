#!/usr/bin/python3
"""
unittest to test max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class to test the max_integer function
    """
    def test_one(self):
        """ test one """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

    def test_two(self):
        """test 2 """
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1.2, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1]), -1)

    def test_three(self):
        """test 3"""
        self.assertEqual(max_integer("milo"), "o")
        self.assertEqual(max_integer(["donga", "zebra"]), "zebra")


if __name__ == '__main__':
    unittest.main()
