#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    str_num = str(n)
    results = 0
    for i in range(len(str_num)):
        if int(str_num[i]) == 0:
            continue
        elif n%int(str_num[i]) == 0:
            results += 1
    return(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
