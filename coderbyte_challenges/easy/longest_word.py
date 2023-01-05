import re


"""
Longest Word
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
"""


def longest_word(sen):
    sentence = re.sub(r"[^a-zA-Z0-9 ]", "", sen)
    words = sentence.split()

    longest_w = words[0]
    longest = len(words[0])

    for word in range(len(words)):
        if len(words[word]) > longest:
            longest = len(words[word])
            longest_w = words[word]

    return longest_w


def longest_words(sen):
    """
    This is my second solution to the question. This function will append all the words and return the max with key=len

    :param sen:
    The sentence to be processed
    :return:
    string
    """
    sentence = re.sub(r"[^a-zA-Z0-9 ]", "", sen)
    words = sentence.split()

    return max(words, key=len)


print(longest_word("fun&!! school! Samuel days! time Sherif"))
print(longest_words("fun&!! school Samuel days! time Sherif"))
