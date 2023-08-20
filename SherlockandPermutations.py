#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def noverkmodm(n, k, m):
    c = 1
    k = min([k, n - k])
    n = n - k;
    for i in range(1, k + 1):
        c = (c * ((n + i) % m) * pow(i, m - 2, m)) % m;
    return c

def solve(n, m):
    return noverkmodm(n + m - 1, n, 10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
