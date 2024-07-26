#!/usr/bin/env python3

import unittest

from main import fibonacci_nth_term as fibo


class TestFibonacciNthTerms(unittest.TestCase):
    #     0  1  2  3  4  5  6   7   8  9   10  11  12    13
    _f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    def test_it_should_return_0_for_0th(self):
        self.assertEqual(fibo(0), self._f[0])

    def test_it_should_return_1_for_1th(self):
        self.assertEqual(fibo(1), self._f[1])

    def test_it_should_return_3_for_4th(self):
        self.assertEqual(fibo(4), self._f[4])


if __name__ == "__main__":
    unittest.main()
