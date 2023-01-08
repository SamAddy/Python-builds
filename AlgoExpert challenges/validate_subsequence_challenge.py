"""
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren’t necessarily adjacent in the array but that are in the same order 
as they appear in the array. For example these numbers [1, 3, 4] from a subsequence of the array [1, 2, 3, 4], and so do the numbers
[2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
"""


def isValidSubsequence(array, sequence):
    # Write your code here.
    # Initialize index to 0
    pos = 0

     # Iterate through the elements of sequence
    for elem in sequence:
        # Check if elem is present in arr1 starting from index i
        while pos < len(array) and array[pos] != elem:
            pos += 1
        # If elem is not found in arr1, return False
        if pos == len(array):
            return False
        # Increment index
        pos += 1

    # All elements of arr2 were found in arr1, so return True
    return True


    print(isValidSubsequence([1, 1, 1, 1, 1], [1, 1, 1]))