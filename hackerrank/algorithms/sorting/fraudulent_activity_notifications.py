"""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the
amount spent by a client on a particular day is greater than or equal to

the client's median spending for a trailing number of days, they send the client a notification about potential fraud.
The bank doesn't send the client any notifications until they have at least that trailing number of prior days'
transaction data.

Given the number of trailing days
and a client's total daily expenditures for a period of days, determine the number of times the client will receive a
notification over all

days.

Example

On the first three days, they just collect spending data. At day , trailing expenditures are . The median is and the
day's expenditure is . Because , there will be a notice. The next day, trailing expenditures are and the expenditures
are . This is less than

so no notice will be sent. Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number
of values, the middle one is picked. If there is an even number of values, the median is then defined to be the average
of the two middle values. (Wikipedia)

Function Description

Complete the function activityNotifications in the editor below.

activityNotifications has the following parameter(s):

    int expenditure[n]: daily expenditures
    int d: the lookback days for median spending

Returns

    int: the number of notices sent

Input Format

The first line contains two space-separated integers
and , the number of days of transaction data, and the number of trailing days' data used to calculate median spending
respectively.
The second line contains space-separated non-negative integers where each integer denotes

.

Constraints

Output Format

Sample Input 0

STDIN               Function
-----               --------
9 5                 expenditure[] size n =9, d = 5
2 3 4 2 3 6 8 4 5   expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

Sample Output 0

2

Explanation 0

Determine the total number of
the client receives over a period of days. For the first five days, the customer receives no notifications because the
bank has insufficient transaction data:

.

On the sixth day, the bank has
days of prior transaction data, , and dollars. The client spends dollars, which triggers a notification because :

.

On the seventh day, the bank has
days of prior transaction data, , and dollars. The client spends dollars, which triggers a notification because :

.

On the eighth day, the bank has
days of prior transaction data, , and dollars. The client spends dollars, which does not trigger a notification because:

.

On the ninth day, the bank has
days of prior transaction data, , and a transaction median of dollars. The client spends dollars, which does not trigger
a notification because :

.

Sample Input 1

5 4
1 2 3 4 4

Sample Output 1

0

There are
days of data required so the first day a notice might go out is day . Our trailing expenditures are with a median of
The client spends which is less than so no notification is sent.
"""

# First naive implementation but didnt pass all test.

def countSort(arr):
    max_val = max(arr)
    index_count = [0] * (max_val + 1)
    results = []

    for i in range(len(arr)):
        index_count[arr[i]] += 1

    for i in range(len(index_count)):
        results.extend([i] * index_count[i])
    return results


def activityNotifications1(expenditure, d):
    # Write your code her
    notifications = 0
    n = len(expenditure)
    s = 0

    # Find the median
    for i in range(d, n):
        median = 0
        elem1 = d // 2
        trailing_days = countSort(expenditure[s:i])

        if d % 2 == 0:
            elem2 = elem1 + 1
            median = (trailing_days[elem1] + trailing_days[elem2]) / 2
        else:
            median = trailing_days[elem1]

        # print(f"i: {i}, expd: {expenditure[i]}, m*2: {median * 2}, t_days: {trailing_days}")
        # Increase starting index for trailing days
        s += 1

        # Increase notifications by 1
        if expenditure[i] >= median * 2:
            notifications += 1

    return notifications


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    # Solution using the sliding window technique
    notifications = 0

    # Store frequency of expenses
    expense_freq = {}

    def get_median():
        # Get indices
        index1 = (d + 1) // 2
        index2 = index1 + 1 if d % 2 == 0 else index1

        # Count frequency of expense
        freq = 0

        val1 = val2 = -1

        for e in sorted(expense_freq):
            freq += expense_freq[e]

            if freq >= index1 and val1 == -1:
                val1 = e

            if freq >= index2:
                val2 = e

            if val1 > -1 and val2 > -1:
                return (val1 + val2) / 2

    for i in range(len(expenditure)):
        expense = expenditure[i]

        if i >= d:
            median = get_median()

            if expense >= 2 * median:
                notifications += 1

            # Update sliding window
            old_expense = expenditure[i - d]
            if expense_freq[old_expense] == 1:
                del expense_freq[old_expense]
            else:
                expense_freq[old_expense] -= 1

        expense_freq[expense] = expense_freq.get(expense, 0) + 1

    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

