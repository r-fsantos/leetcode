#!/usr/bin/env python3


class MaxCount:
    """
    Return max(positives, negatives) on a given array
    Zeros are neutral
    """

    def maximumCountWithLinearSearch(self, nums: list[int]) -> int:
        """no optimizations, no guard clauses, O(n) for sure"""
        p, n = 0, 0

        for i in range(len(nums)):
            if nums[i] > 0:
                p += 1
            if nums[i] < 0:
                n += 1

        return max(p, n)

    def maximumCountWithLinearSeachOptimized(self, nums: list[int]) -> int:
        """
        Iterate from left until zero to count negatives and
        iterate from right until zero to count positives
        """
        # fst considering all negatives or all positives
        p, n = len(nums), len(nums)

        for i in range(len(nums)):
            if nums[i] >= 0:
                n = i
                break

        # Interval [Nth -1, -1)
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= 0:
                p = (len(nums) - 1) - j
                break

        return max(p, n)

    def maximumCountWithBinarySearch(self, nums: list[int]) -> int:
        p = self._countPositives(nums)
        n = self._countNegatives(nums)

        return max(p, n)

    def _countPositives(self, nums: list[int]) -> int:
        """
        guard clauses:
            ignore zeros,
            consider all positives
            or none positives
        """
        # all positives
        if nums[0] > 0:
            return len(nums)

        # zero positives
        if nums[-1] <= 0:
            return 0

        p = 0
        lo = 0
        hi = len(nums)
        while lo < hi:
            m = (lo + hi) // 2

            if nums[m] > 0 and nums[m - 1] <= 0:
                p = len(nums) - m
                break
            elif nums[m] > 0:
                hi = m
            else:
                lo = m + 1
        return p

    def _countNegatives(self, nums: list[int]) -> int:
        """
        guard clauses:
            ignore zeros,
            consider all negatives
            or none negatives

        binary search
        """
        if nums[-1] < 0:
            return len(nums)

        if nums[0] >= 0:
            return 0

        n = 0
        lo = 0
        hi = len(nums)
        while lo < hi:
            m = (lo + hi) // 2

            if nums[m] < 0 and nums[m + 1] >= 0:
                n = m + 1
                break
            elif nums[m] < 0:
                lo = m + 1
            else:
                hi = m

        return n


if __name__ == "__main__":
    _rdm = [-4, -3, -2, -1, 0, 0, 0, 1, 2, 3]
    _rdm2 = [-2, -1, 0, 0, 0, 1, 2, 3]
    _zeros = [0, 0, 0, 0, 0, 0]
    _no_zeros = [-3, -2, -1, 1, 2, 3]
    _all_negs = [-5, -4, -3, -2, -1]
    _all_poss = [1, 2, 3, 4, 5, 6]
    print(MaxCount().maximumCountWithBinarySearch(_rdm))
    print(MaxCount().maximumCountWithBinarySearch(_rdm2))

    print(MaxCount().maximumCountWithBinarySearch(_zeros))
    print(MaxCount().maximumCountWithBinarySearch(_no_zeros))
    print(MaxCount().maximumCountWithBinarySearch(_all_negs))
    print(MaxCount().maximumCountWithBinarySearch(_all_poss))
