"""
205. Isomorphic Strings
Solved
Easy
Topics
Companies

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true



Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.


"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map_t = {}
        t_map_s = {}

        for index in range(len(s)):
            if s[index] in s_map_t:
                if s_map_t[s[index]] != t[index]:
                    return False
            else:
                if t[index] in t_map_s:
                    return False
                s_map_t[s[index]] = t[index]
                t_map_s[t[index]] = s[index]

        return True