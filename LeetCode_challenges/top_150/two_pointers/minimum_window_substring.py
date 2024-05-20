"""
76. Minimum Window Substring
Attempted
Hard
Topics
Companies
Hint

Given two strings s and t of lengths m and n respectively, return the minimum window
substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring,
return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Handle edge case where length of t is greater than length of s
        if len(t) > len(s):
            return ""

        min_window_substring = None

        # Get character frequency for t
        t_freq = Counter(t)
        required_chars = len(t)
        formed_chars = 0
        left, right = 0, 0

        # Now we iterate through s
        while right < len(s):
            # If char in t, reduce its frequency count
            if s[right] in t_freq:
                t_freq[s[right]] -= 1

                # Increase formed chars by 1
                if t_freq[s[right]] >= 0:
                    formed_chars += 1

            # Updating min window substring
            while formed_chars == required_chars:
                window_size = right - left + 1
                if min_window_substring is None or window_size < len(min_window_substring):
                    min_window_substring = s[left:right + 1]

                # Update t_freq back to its nomral frequency
                if s[left] in t_freq:
                    t_freq[s[left]] += 1
                    if t_freq[s[left]] > 0:
                        formed_chars -= 1

                left += 1

            right += 1

        return min_window_substring if min_window_substring is not None else ""

    # This solution is quite expensive
    def minWindow2(s: str, t: str) -> str:
        # Handle edge case
        if len(t) > len(s):
            return ""

        min_window_substring = None

        i = 0
        while i <= len(s) - len(t):
            right = i
            t_index = 0
            t_freq = {}

            for char in t:
                if char in t_freq:
                    t_freq[char] += 1
                else:
                    t_freq[char] = 1

            while right < len(s):
                if s[right] in t_freq:
                    if t_freq[s[right]] > 1:
                        t_freq[s[right]] -= 1
                    else:
                        del t_freq[s[right]]

                if len(t_freq) == 0:
                    if min_window_substring == None or len(s[i:right + 1]) < len(min_window_substring):
                        min_window_substring = s[i:right + 1]
                        break

                right += 1
            i += 1
            right = i

        return min_window_substring if min_window_substring is not None else ""
