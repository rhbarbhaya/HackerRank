#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    s = s.split(":")
    hour = s[0]
    mins = int(s[1])
    if "AM" in s[-1]:
        hour = (int(hour)%12)
    if "PM" in s[-1]:
        hour = (12+(int(hour)%12))
    sec = int(s[2][:2])
    return("{:02d}:{:02d}:{:02d}".format(hour, mins, sec))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()