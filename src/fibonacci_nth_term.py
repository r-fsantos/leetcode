#!/usr/bin/env python3


def fibonacci_nth_term(n: int) -> int:
    """
    Optimal solution
    if n == 0:
        return 0
    if n == 1:
        return 1

    f = [0, 1]
    i = 2
    while i < n:
        fst = f[0]
        snd = f[1]
        tmp = fst + snd
        f[0] = snd
        f[1] = tmp
        i += 1
    return f[1] + f[0]
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, (n + 1)):
        f[i] = f[i - 2] + f[i - 1]
    return f[n]
