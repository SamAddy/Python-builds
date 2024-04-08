"""
1544. Make The String Great
Attempted
Easy
Topics
Companies
Hint

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can
keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.



Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:

Input: s = "s"
Output: "s"



Constraints:

    1 <= s.length <= 100
    s contains only lower and upper case English letters.


"""

class Solution:

    # Naive solution (Updating in-place)
    # Didnt pass all test cases
    def makeGood(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        i = 1
        while i < n and n >= 2:
            j = i -1
            if s[i].isupper() or s[j].isupper():
                if s[j].lower() == s[i].lower():
                    s = s.replace(s[i], '', 1)
                    s = s.replace(s[j], '', 1)
                    n = len(s)
                    i = 1
                else:
                    i += 1
            else:
                i += 1
        return s

    # The stack approach

    def makeGood2(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1].lower() == c.lower() and stack[-1] != c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

    # Improvement of my naive solution to pass all test using the ord() method

    def makeGood(self, s: str) -> str:
        n = len(s)
        i = 1

        while i < n:
            if abs(ord(s[i]) - ord(s[i - 1])) == 32:
                s = s[:i - 1] + s[i + 1:]
                n -= 2
                i = max(i - 2, 1)
            else:
                i += 1

        return s