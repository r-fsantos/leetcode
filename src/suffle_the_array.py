#!/usr/bin/env python3


class SuffleTheArray(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ret = []
        i = 0

        while i < n:
            ret.append(nums[i])
            ret.append(nums[i + n])
            i += 1

        return ret
