#!/usr/bin/env python3

def reverseString(s: list[str]):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    mid = len(s) // 2

    while i < mid:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s
