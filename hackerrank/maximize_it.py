"""
You are given a function f(x) = X^2. You are also given K lists. The ith list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:
 s=(f(x1)+f(x2)+…+f(xk))mod M
% denotes the element picked from the list . Find the maximized value

obtained.

denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element.
You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the ith list, followed by Ni space
separated integers denoting the elements in the list.

Constraints

Output Format

Output a single integer denoting the value

.

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output

206

Explanation

Picking
from the st list, from the nd list and from the rd list gives the maximum value equal to % = .
"""

from itertools import product

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    k, m = map(int, input().split())
    lists = []

    for _ in range(k):
        elements = list(map(int, input().split()[1:]))
        lists.append(elements)

    max_sum = 0

    for combination in product(*lists):
        s = sum(x ** 2 for x in combination) % m
        max_sum = max(max_sum, s)

    print(max_sum)
