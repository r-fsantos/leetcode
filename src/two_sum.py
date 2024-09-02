#!/usr/bin/env python3


class TwoSum:
    """
    Approach:
        Iterate
        Keep track
        Lookup for a mapped element n[i], in a way that satisfy the following:
            `n[i] + n[i + j] = target`
        To match that, we define a candidate n[j], j > i (non-repeated element)
            `candidate = target - n[i]`

    Time Complexity: O(n)
    Space Complexity: 0(n)

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def two_sum(self, nums, target) -> list[int]:
        lookup = dict()
        ret = [0] * 2

        for i, v in enumerate(nums):
            candidate = target - v
            if candidate in lookup:
                ret[0], ret[1] = lookup[candidate], i
                break
            lookup[v] = i

        return ret
