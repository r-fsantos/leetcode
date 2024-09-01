#!/usr/bin/env python3

import unittest

from main import HasDuplicate


class TestHasDuplicate(unittest.TestCase):

    _true = [1, 2, 3, 1, 4]
    _false = [1, 3, 5, 6, 2]

    _sut = HasDuplicate()

    def test_it_should_return_true(self):
        self.assertTrue(self._sut.hasDuplicate(self._true))

    def test_it_should_return_false(self):
        self.assertFalse(self._sut.hasDuplicate(self._false))


if __name__ == "__main__":
    unittest.main()
