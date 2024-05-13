"""
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint

Given a string s, find the length of the longest
substring
without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


"""

class Solution:
    # Using extra space
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to hold characters and their index
        char_index = {}
        longest_substring_length = 0
        start = 0  # Start of the current substring

        # Iterate through the string
        for index, char in enumerate(s):
            # If the char exist in char_index, we update the start point since a duplicate have been encountered
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1

            # Update char index dictionary
            char_index[char] = index

            # Get the longest substring length
            longest_substring_length = max(longest_substring_length, index - start + 1)

        return longest_substring_length



     # Using the two pointers approach
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_sub = float('-inf')
        counter = 1

        if len(s) == 0:
            return 0

        for right in range(1, len(s)):
            if s[right] in s[left:right]:
                left = right
                counter = 1
            else:
                counter += 1

            longest_sub = max(longest_sub, counter)

        return longest_sub if longest_sub != float('-inf') else 1
