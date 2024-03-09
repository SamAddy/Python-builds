"""
Sample Challenge
This is a simple challenge to get things started. Given a sorted array () and a number (), can you print the
index location of

in the array?

Example


Return

for a zero-based index array.

If you are going to use the provided code for I/O, this next section is for you.

Function Description

Complete the introTutorial function in the editor below. It must return an integer representing the zero-based index of

.

introTutorial has the following parameter(s):

    int arr[n]: a sorted array of integers
    int V: an integer to search for

Returns

    int: the index of

in

The next section describes the input format. You can often skip it, if you are using included methods or code stubs.

Input Format

The first line contains an integer,
, a value to search for.
The next line contains an integer, , the size of . The last line contains space-separated integers, each a value of where

.

The next section describes the constraints and ranges of the input. You should check this section to know the
range of the input.

Constraints

will occur in

    exactly once.

This "sample" shows the first input test case. It is often useful to go through the sample to understand a challenge.

Sample Input 0

STDIN           Function
-----           --------
4               V = 4
6               arr[] size n = 6 (not passed, see function description parameters)
1 4 5 7 9 12    arr = [1, 4, 5, 7, 9, 12]

Sample Output 0

1

Explanation 0
. The value is the element in the array. Its index is since the array indices start from (see array definition
under Input Format).
"""


import os

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#

def introTutorial(V, arr):
    # Write your code here
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == V:
            return mid
        elif arr[mid] > V:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
