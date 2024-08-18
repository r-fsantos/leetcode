#!/usr/bin/env python3

import unittest

from main import Palindrome


class TestIsPalindrome(unittest.TestCase):

    _false_1 = "race a car"
    _false_2 = "renato"
    _false_3 = "renato @ otanea"

    _true_1 = " "
    _true_2 = "bob"
    _true_3 = "A man, a plan, a canal: Panama"

    _sut = Palindrome()

    def test_it_should_return_true(self):
        self.assertTrue(self._sut.isPalindrome(self._true_1))
        self.assertTrue(self._sut.isPalindrome(self._true_2))
        self.assertTrue(self._sut.isPalindrome(self._true_3))

    def test_it_should_return_false(self):
        self.assertFalse(self._sut.isPalindrome(self._false_1))
        self.assertFalse(self._sut.isPalindrome(self._false_2))
        self.assertFalse(self._sut.isPalindrome(self._false_3))


if __name__ == "__main__":
    unittest.main()
