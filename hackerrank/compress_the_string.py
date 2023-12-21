"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools .
To read more about this function, Check this out (https://docs.python.org/2/library/itertools.html#itertools.groupby).

You are given a string
. Suppose a character '' occurs consecutively times in the string. Replace these consecutive occurrences of
the character 'c' with (X, c) in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string


Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of
denote integers between 0 and 9
1<=| S |<=pow(10, 4)
.

Sample Input

1222311

Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

Explanation

First, the character occurs only once. It is replaced by (1, 1). Then the character occurs three times,
and it is replaced by and so on.

Also, note the single space within each compression and between the compressions.
"""

from itertools import groupby

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    s = input()

    for k, g in groupby(s):
        print((len(list(g)), int(k)), end=" ")
