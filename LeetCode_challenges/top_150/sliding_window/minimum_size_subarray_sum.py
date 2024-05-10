"""
209. Minimum Size Subarray Sum
Solved
Medium
Topics
Companies

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0



Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Variable to hold minimal length of subarray
        min_len = float('inf')

        # For check the start of the subarray
        pointer = 0

        sub_total = 0

        for index, value in enumerate(nums):
            sub_total += value

            while sub_total >= target:
                sub_len = (index - pointer) + 1
                min_len = min(min_len, sub_len)
                sub_total -= nums[pointer]
                pointer += 1

        return min_len if min_len != float('inf') else 0

