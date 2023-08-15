#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'restaurant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER b
#

def restaurant(l, b):
    A = l*b
    for x in range(1,A):
        if (x == math.sqrt(A)):
            return (1)
    if (l==b):
        return (1)
    else:
        m = max(l,b)
        n = min(l,b)
        while(n!=0):
            m,n=n,m%n
        gcd = m
        a = l//gcd
        b = b//gcd
        return (a*b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
