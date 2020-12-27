#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    l_stair = []
    for i in range(1,n+1):
        l_stair.append("#"*i)
    
    max_len = max(len(i) for i in l_stair)
    
    for item in l_stair:
        print('{0:>{1}}'.format(item, max_len))

if __name__ == '__main__':
    n = int(input())

    staircase(n)