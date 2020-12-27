#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    ans = []
    for i in range(len(grades)):
        if grades[i] <= 37:
            ans.append(grades[i])
        elif (grades[i]+2)%5 == 0:
            ans.append(grades[i]+2)
        elif (grades[i]+1)%5 == 0:
            ans.append(grades[i]+1)
        else:
            ans.append(grades[i])
    return(ans) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()