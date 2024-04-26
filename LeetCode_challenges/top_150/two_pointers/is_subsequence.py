"""
392. Is Subsequence
Solved
Easy
Topics
Companies

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false



Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one
to see if t has its subsequence. In this scenario, how would you change your code?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Version 2
        # Return False if lenght of s greater than t
        if len(s) > len(t):
            return False

        if not s:
            return True

        s_index = 0
        # Iterate through t and compare char with s
        for index, char in enumerate(t):
            if s[s_index] == char:
                s_index += 1

                if s_index == len(s):
                    return True

        return s_index == len(s)

        # Version 1
        # if len(s) > len(t):
        #     return False

        # if s == "":
        #     return True

        # s_index , t_index = 0, 0

        # # Iterate the strings and compare chars
        # while s_index < len(s) and t_index < len(t):

        #     if s[s_index] == t[t_index]:
        #         if s_index == len(s) - 1:
        #             return True

        #         # Increase the pointers
        #         s_index += 1
        #         t_index += 1
        #     else:
        #         t_index += 1

        # # Return False if s not a subsequence of t
        # return False

