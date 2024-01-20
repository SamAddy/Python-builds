"""
This problem is a programming version of Problem 1 from projecteuler.net

If we list all the natural numbers below
that are multiples of or , we get and . The sum of these multiples is

.

Find the sum of all the multiples of
or below

.

Input Format

First line contains
that denotes the number of test cases. This is followed by lines, each containing an integer,

.

Constraints

Output Format

For each test case, print an integer that denotes the sum of all the multiples of
or below

.

Sample Input 0

2
10
100

Sample Output 0

23
2318

Explanation 0

For N = 10, if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23

Similarly for N = 100, we get 2318.
"""

# !/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1

    # mul_of_3_5 = [x for x in range(n) if x % 3 == 0 or x % 5 == 0]
    # print(sum(mul_of_3_5))
    # Use the arithmetic series sum formula

    def sum_of_multiples(k):
        num_of_terms = n // k
        return k * (num_of_terms * (num_of_terms + 1)) // 2


    sum_multiples = sum_of_multiples(3) + sum_of_multiples(5) - sum_of_multiples(15)

    print(sum_multiples)
