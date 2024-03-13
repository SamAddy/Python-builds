"""
Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's
in over his head! Can you help George understand Lily's homework so she can hang out with him?

Consider an array of
distinct integers, arr = [a[0], a[1], ... a[n-1]] . George can swap any two elements of the array any number of times.
An array is beautiful if the sum of [arr[i] - arr[i - 1]] among 0 < i < nis minimal


Given the array, determine and return the minimum number of swaps that should be performed in order to make the array
beautiful.

Example
arr = [7, 15, 12, 3
One minimal array is [3, 7, 12, 15]. To get there, George performed the following swaps:

    Swap      Result
          [7, 15, 12, 3]
    3 7   [3, 15, 12, 7]
    7 15  [3, 7, 12, 15]


It took 2 swaps to make the array beautiful. This is minimal among the choices of beautiful arrays possible.
"""
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    def count_swaps(arr_):
        n = len(arr_)
        idx_map = {val: idx for idx, val in enumerate(arr_)}
        sorted_arr = sorted(arr_)
        swaps = 0

        for i in range(n):
            if arr_[i] != sorted_arr[i]:
                j = idx_map[sorted_arr[i]]
                arr_[i], arr_[j] = arr_[j], arr_[i]
                idx_map[arr_[i]], idx_map[arr_[j]] = idx_map[arr_[j]], idx_map[arr_[i]]
                swaps += 1
        return swaps

    forward_result = count_swaps(arr.copy())
    backward_result = count_swaps(arr.copy()[::-1])

    return min(forward_result, backward_result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
