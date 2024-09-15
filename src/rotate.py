class Solution(object):
    def reverse_arr(self, arr, lo, hi):
        while lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
            hi -= 1
        return arr

    def rotate(self, nums, k):
        r = k % len(nums)

        nums = self.reverse_arr(nums, 0, len(nums) - 1 - r)
        nums = self.reverse_arr(nums, len(nums) - r, len(nums))
        nums = self.reverse_arr(nums, 0, len(nums))
