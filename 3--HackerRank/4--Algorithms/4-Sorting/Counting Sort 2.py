#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    count = [0] * 100
    for x in arr:
        count[x] = count[x] + 1

    sorted_list = []
    for ind, val in enumerate(count):
        if val > 0:
            sorted_list.extend([ind] * val)

    return sorted_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
