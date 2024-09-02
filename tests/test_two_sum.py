#!/usr/bin/env python3

import unittest

from main import TwoSum


class TestTwoSum(unittest.TestCase):
    _sut = TwoSum()

    def test_it_should_return_expected(self):
        self.assertEqual(self._sut.two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self._sut.two_sum([3, 3], 6), [0, 1])
        self.assertEqual(self._sut.two_sum([2, 7, 11, 15], 9), [0, 1])


if __name__ == "__main__":
    unittest.main()
