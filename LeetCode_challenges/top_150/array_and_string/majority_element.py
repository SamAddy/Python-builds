"""
169. Majority Element
Solved
Easy
Topics
Companies

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time complexity is O(n)
        # Space complexity is O(n)
        nums_freq = Counter(nums)
        for key, val in nums_freq.items():
            if val > len(nums) / 2:
                return key
        # return max(nums_freq, key=nums_freq.get)

        # Second solution
        # Space complexity is O(1)

        count = 0
        majority_candidate = None

        for num in nums:
            if count == 0:
                majority_candidate = num
                count = 1
            elif num == majority_candidate:
                count += 1
            else:
                count -= 1

        return majority_candidate
