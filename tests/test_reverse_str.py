#!/usr/bin/env python3

import unittest

from main import reverseString


class TestReverseString(unittest.TestCase):
    def test_it_shoul_revert_renato(self):
        s = ["r", "e", "n", "a", "t", "o"]
        exp = ["o", "t", "a", "n", "e", "r"]

        ret = reverseString(s)

        self.assertEqual(ret, exp)

    def test_it_should_revert_test(self):
        s = ["t", "e", "s", "t"]
        exp = ["t", "s", "e", "t"]

        ret = reverseString(s)

        self.assertEqual(ret, exp)


if __name__ == "__main__":
    unittest.main()
