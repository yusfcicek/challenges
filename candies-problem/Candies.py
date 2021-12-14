#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Write your code here
    candie_arr = [1] * n

    for i in range(n-1):
        if arr[i+1] > arr[i]:
            candie_arr[i+1] = candie_arr[i] + 1
            
    for j in range(n-1, 0, -1):
        if arr[j-1] > arr[j] and candie_arr[j-1] <= candie_arr[j]:
            candie_arr[j-1] = candie_arr[j] + 1
            
    return sum(candie_arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
