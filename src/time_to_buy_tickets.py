#!/usr/bin/env python3

"""
Clarifying problem

    size of tickets?
    may I assume that tickets are an array?
    about entries, there are only integers?
    if so, all of them are positives?
    do we have enough tickets for the people in line?

    index ?
    0 < k < n
"""


def timeRequiredToBuyBigO_mn(tickets: list[int], k: int) -> int:
    time = 0
    t_size = len(tickets)  # ticket size

    while tickets[k] > 0:
        for i in range(t_size):  # [0, t_size)
            if not tickets[k]:
                break
            if tickets[i] > 0:
                time += 1
                tickets[i] -= 1
    return time


def timeRequiredToBuyBigO_n(tickets: list[int], k: int) -> int:
    time = 0

    for i in range(k + 1):
        time += min(tickets[i], tickets[k])
    for i in range(k + 1, len(tickets)):
        time += min(tickets[k] - 1, tickets[i])

    return time


if __name__ == "__main__":
    assert timeRequiredToBuyBigO_mn([1, 2, 3], 2) == 6
    assert timeRequiredToBuyBigO_n([1, 2, 3], 2) == 6
