"""
88. Merge Sorted Array
Easy
Topics
Companies
Hint

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.



Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109



Follow up: Can you come up with an algorithm that runs in O(m + n) time?
Seen this question in a real interview before?
1/4
Yes
No
Accepted
2.9M
Submissions
5.9M
Acceptance Rate
49.3%
Topics
Array
Two Pointers
Sorting
Companies
Hint 1
You can easily solve this problem if you simply think about two elements at a time rather than two arrays.
We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a
local decision and arrive at an optimal solution?
Hint 2
If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you
will arrive at the optimal solution.
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            key = nums2[i]

            j = key - 1

            if nums1[j] == 0:
                nums1[j] = key

            elif key >= nums1[j]:
                tmp = nums1[key]
                nums1[key] = key
                nums1[key + 1] = tmp

            elif key < nums1[j]:
                tmp = nums1[j]
                nums1[j] = key
                nums1[key] = tmp

        # Solution that passes all test

        c = m + n - 1
        idx1 = m - 1
        idx2 = n - 1

        for i in range(c, -1, -1):
            if idx2 < 0:
                nums1[i] = nums1[i]
            elif idx1 < 0:
                nums1[i] = nums2[idx2]
                idx2 -= 1
            else:
                if nums1[idx1] > nums2[idx2]:
                    nums1[i] = nums1[idx1]
                    idx1 -= 1
                else:
                    nums1[i] = nums2[idx2]
                    idx2 -= 1








