#!/usr/bin/python3
""" Module for a minOperations function """


def smallestNumber(n):
    """ Return The samllest prime number can be divide number n """
    for i in range(2, int(n+1)):
        if (n % i == 0):
            return i


def minOperations(n):
    """ Return the fewest number of operations needed """
    sN = smallestNumber(n)
    if sN == n:
        return 0

    ops = 0
    while (n > 1):
        sN = smallestNumber(n)
        ops = ops + sN
        n = n / sN

    return ops
