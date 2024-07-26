#!/usr/bin/env python3

import unittest

from main import MaxCount


class TestMaxCount(unittest.TestCase):
    _rdm = [-2, -1, -1, 0, 0, 0, 1, 2, 3]
    _neg_greater_than_pos = [-3, -2, -1, 0, 0, 0, 1, 2]
    _pos_greater_than_neg = [-2, -1, -1, 0, 0, 0, 1, 2, 3, 4]
    _zeros = [0, 0, 0, 0, 0, 0]
    _no_zeros = [-3, -2, -1, 1, 2, 3]
    _all_negs = [-5, -4, -3, -2, -1]
    _all_poss = [1, 2, 3, 4, 5, 6]

    _sut = MaxCount()

    def test_rdm_nums(self):
        # linear search
        self.assertEqual(self._sut.maximumCountWithLinearSearch(self._rdm), 3)
        self.assertEqual(
            self._sut.maximumCountWithLinearSearch(self._neg_greater_than_pos),
            3,
        )
        self.assertEqual(
            self._sut.maximumCountWithLinearSearch(self._pos_greater_than_neg),
            4,
        )

        # linear search optimized
        self.assertEqual(
            self._sut.maximumCountWithLinearSeachOptimized(self._rdm), 3
        )
        self.assertEqual(
            self._sut.maximumCountWithLinearSeachOptimized(
                self._neg_greater_than_pos
            ),
            3,
        )
        self.assertEqual(
            self._sut.maximumCountWithLinearSeachOptimized(
                self._pos_greater_than_neg
            ),
            4,
        )

        # binary search
        self.assertEqual(self._sut.maximumCountWithBinarySearch(self._rdm), 3)
        self.assertEqual(
            self._sut.maximumCountWithBinarySearch(self._neg_greater_than_pos),
            3,
        )
        self.assertEqual(
            self._sut.maximumCountWithBinarySearch(self._pos_greater_than_neg),
            4,
        )

    def test_zeros(self):
        self.assertEqual(
            self._sut.maximumCountWithLinearSearch(self._zeros), 0
        )  # noqa

        self.assertEqual(
            self._sut.maximumCountWithLinearSeachOptimized(self._zeros), 0
        )

        self.assertEqual(self._sut.maximumCountWithBinarySearch(self._zeros), 0)

    def test_no_zeros(self):
        self.assertEqual(
            self._sut.maximumCountWithLinearSearch(self._no_zeros), 3
        )

        self.assertEqual(
            self._sut.maximumCountWithLinearSeachOptimized(self._no_zeros), 3
        )

        self.assertEqual(
            self._sut.maximumCountWithBinarySearch(self._no_zeros), 3
        )

    def test_all_negatives(self):
        self.assertEqual(
            self._sut.maximumCountWithLinearSearch(self._all_negs), 5
        )

        self.assertEqual(
            self._sut.maximumCountWithLinearSeachOptimized(self._all_negs), 5
        )

        self.assertEqual(
            self._sut.maximumCountWithBinarySearch(self._all_negs), 5
        )

    def test_all_positives(self):
        self.assertEqual(
            self._sut.maximumCountWithLinearSearch(self._all_poss), 6
        )

        self.assertEqual(
            self._sut.maximumCountWithLinearSeachOptimized(self._all_poss), 6
        )

        self.assertEqual(
            self._sut.maximumCountWithBinarySearch(self._all_poss), 6
        )


if __name__ == "__main__":
    unittest.main()
