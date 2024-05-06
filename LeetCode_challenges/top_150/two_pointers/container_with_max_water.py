"""
11. Container With Most Water
Solved
Medium
Topics
Companies
Hint

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1



Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104


"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Using two pointers approach
        # time complexity O(n)
        # space complexity O(1)

        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        # Brute force
        # Time complexity O(n^2)

        # max_area = 0

        # for index in range(len(height)):
        #     for j in range(index + 1, len(height)):
        #         width = j - index
        #         area = min(height[index], height[j]) * width

        #         max_area = max(max_area, area)

        # return max_area