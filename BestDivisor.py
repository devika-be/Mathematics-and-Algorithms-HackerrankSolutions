#!/bin/python3

import math
import os
import random
import re
import sys


def divisor(n):
    div = [i for i in range(1,n+1) if n%i==0]
    return max(div,key=lambda x: sum(int(i) for i in str(x)))

if __name__ == '__main__':
    n = int(input().strip())
    print(divisor(n))
