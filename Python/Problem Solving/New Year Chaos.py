#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for final_pos, start_pos in enumerate(q):
        # Abort if I am more than two bribes ahead of where I started
        if  final_pos + 1 < start_pos - 2:
            print('Too chaotic')
            return
        potential_bribers = range(max(start_pos - 2, 0), final_pos)
        bribes += [q[briber] > start_pos for briber in potential_bribers].count(True)
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)