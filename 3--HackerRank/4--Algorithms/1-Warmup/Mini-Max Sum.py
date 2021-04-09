#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_max_number = max(arr)
    arr_min_number = min(arr)
    max_remove_arr_sum = sum(arr)-arr_max_number
    min_remove_arr_sum = sum(arr)-arr_min_number

    print(max_remove_arr_sum,min_remove_arr_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
