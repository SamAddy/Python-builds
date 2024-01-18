"""
Check Tutorial tab to know how to to solve.

You are given a string
.
Your task is to verify that

is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

Number can start with +, - or . symbol.
For example:
✔+4.50
✔-1.0
✔.5
✔-.7
✔+.4
✖ -+4.5

Number must contain at least

decimal value.
For example:
✖ 12.
✔12.0

Number must have exactly one . symbol.
Number must not give any exceptions when converted using

.

Input Format

The first line contains an integer
, the number of test cases.
The next line(s) contains a string

.

Constraints

Output Format

Output True or False for each test case.

Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output 0

False
True
True
False

Explanation 0

: O is not a digit.
: is valid.
: is valid.
SomeRandomStuff: is not a number.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

pattern = r'^[+-]?(\d*\.\d+|\d+\.\d+)$'

for _ in range(t):
    match = re.match(pattern, input())
    if match:
        print(True)
    else:
        print(False)