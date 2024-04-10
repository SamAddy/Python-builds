"""
42. Trapping Rain Water
Solved
Hard
Topics
Companies

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.



Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6
units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9



Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105


"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        total_water = 0

        # Taking care of edge case
        if n <= 1:
            return total_water

        # Calculate left max value for each height
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])

        # Calculate right max value for each height
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])

        # Calculate water over bar for each height
        for i in range(n):
            water_over_bar = min(left_max[i], right_max[i]) - height[i]

            if water_over_bar > 0:
                total_water += water_over_bar
        return total_water