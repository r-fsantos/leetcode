#!/usr/bin/env python3

import unittest

from main import SuffleTheArray


class TestSuffleTheAray(unittest.TestCase):

    _sut = SuffleTheArray()

    def test_it_should_shuffle_successfully(self):
        l1 = [2, 5, 1, 3, 4, 7]
        n1 = 3
        exp1 = [2, 3, 5, 4, 1, 7]

        l2 = [1, 2, 3, 4, 4, 3, 2, 1]
        n2 = 4
        exp2 = [1, 4, 2, 3, 3, 2, 4, 1]

        l3 = [1, 1, 2, 2]
        n3 = 2
        exp3 = [1, 2, 1, 2]

        self.assertEqual(self._sut.shuffle(l1, n1), exp1)
        self.assertEqual(self._sut.shuffle(l2, n2), exp2)
        self.assertEqual(self._sut.shuffle(l3, n3), exp3)


if __name__ == "__main__":
    unittest.main()
