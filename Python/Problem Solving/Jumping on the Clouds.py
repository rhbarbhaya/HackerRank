#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current = 0
    jumps = 0
    end = len(c) - 1
    while current < end:
        if current+2 <= end and c[current+2] == 0:
            jumps += 1
            current += 2
        elif c[current + 1] == 0:
            jumps += 1
            current += 1
        else:
            pass
    return jumps
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()