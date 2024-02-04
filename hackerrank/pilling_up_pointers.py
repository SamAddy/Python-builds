"""
There is a horizontal row of cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube |i| is on top of cube |j| then sideLength |j| >= sideLength |i|.

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example
blocks = [1, 2, 3, 8, 7]
Result: No

After choosing the rightmost element, 7, choose the leftmost element, 1. After than, the choices are 2 and 8. These are both larger than the top block of size

.
b = [1, 2, 3, 7, 8]
Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

Input Format

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains space separated integers, denoting the sideLengths of each cube in that order.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
results = []

for _ in range(t):
    b_size = int(input())
    b = list(map(int, input().split()))

    left = 0
    right = b_size - 1
    last_picked_cube = float('inf')
    can_stack = True

    while left <= right:
        if b[left] >= b[right] and b[left] <= last_picked_cube:
            last_picked_cube = b[left]
            left += 1
        elif b[right] >= b[left] and b[right] <= last_picked_cube:
            last_picked_cube = b[right]
            right -= 1

        else:
            can_stack = False
            break
    results.append("Yes" if can_stack else "No")

for result in results:
    print(result)
