"""
30. Substring with Concatenation of All Words
Solved
Hard
Topics
Companies

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

    For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are
    all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any
    permutation of words.

Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        results = []
        words_freq = {}
        word_len = len(words[0])
        combined_words_len = len(words) * word_len

        # Get and store frequency of words
        for word in words:
            if word in words_freq:
                words_freq[word] += 1
            else:
                words_freq[word] = 1

        # Iterate through s
        for index in range(len(s) - combined_words_len + 1):
            # Get substring with len of combined words
            substr = s[index:index+combined_words_len]

            # Get words in substrings
            substr_words = [substr[j:j+word_len] for j in range(0, combined_words_len, word_len)]

            substr_freq = {}

            # Store substr words frequency
            for word in substr_words:
                if word in substr_freq:
                    substr_freq[word] += 1
                else:
                    substr_freq[word] = 1

            # Add index to result
            if substr_freq == words_freq:
                results.append(index)

        return results
