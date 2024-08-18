class Palindrome(object):
    def isPalindrome(self, s):
        """
        lower all chars
        copy it to a new array: O(n) Spatial Complexity
        move all non-alpha to the end of the array, count the non-alpha
        Use two-pointers to compare from zero until the first non-alpha - 1

        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s_len = len(s)
        ss = [0] * s_len
        for i in range(s_len):
            ss[i] = s[i]

        nonAlphaIdx = 0
        for i in range(s_len):
            if ss[i].isalnum():
                ss[nonAlphaIdx], ss[i] = ss[i], ss[nonAlphaIdx]
                nonAlphaIdx += 1

        for i in range(nonAlphaIdx):
            if ss[i] != ss[nonAlphaIdx - 1 - i]:
                return False
        return True
