# Algorithms Techniques

# 1. Sliding window:
# The sliding window pattern is used to perform a required operation on a specific window size of a given array or
# linked list, such as finding the longest subarray containing all 1s. Sliding windows start from the first element and
# keep shifting right by one element. Adjust the length of the window to meet the criteria in your coding interview.
# The window size can grow, shrink or stay constant.

# Sliding Window Technique Tips:
# 1. Define window size based on problem requirements.
# 2. Initialize window by processing initial elements.
# 3. Process and update efficiently when sliding.
# 4. Handle edge cases to ensure proper initialization.
# 5. Optimize for time and space complexity.
# 6. Visualize as two pointers moving through the array.
# 7. Practice with different examples and variations.
# 8. Consider the two pointers approach for efficiency.
# 9. Choose appropriate data structures for window elements.
# 10. Test thoroughly for correctness with various inputs.
# 11. Document code clearly to aid understanding.

def max_subarray_sum(arr, k):
    n = len(arr)

    # Check on base cases
    if n < k:
        return 'Array length must be greater than or equal to k'

    if n == k:
        return arr

    # Initialize the initial window (sub array)
    subarray_sum = sum(arr[:k])
    max_sum = subarray_sum

    for i in range(k, n):
        # Process the current window
        subarray_sum = subarray_sum - arr[i - k] + arr[i]

        # Update max sum if needed
        max_sum = max(max_sum, subarray_sum)

    return max_sum


def subarray_sum_to_k(arr, k):
    """

    """
    n = len(arr)
    results = []
    subarray_sum = 0
    start = 0

    for i in range(n):
        subarray_sum += arr[i]

        while subarray_sum > k:
            subarray_sum -= arr[start]
            start += 1

        if subarray_sum == k:
            results.append(arr[start:i+1])
    return results


def minimum_size_subarray_sum(arr, target):
    """
    Problem: Minimum Size Subarray Sum

    Given an array of positive integers and a target sum, find the minimum length of a contiguous subarray whose sum is
    at least the target sum. If there is no such subarray, return 0.

    For example:

    python

    arr = [2, 3, 1, 2, 4, 3]
    target = 7

    The minimum size subarray with a sum at least 7 is [4, 3], so the expected output is 2.
    """

    min_length = float('inf')
    subarray_sum = 0
    count = 0
    start = 0

    for i in range(len(arr)):
        subarray_sum += arr[i]
        count += 1

        while subarray_sum > target:
            subarray_sum -= arr[start]
            count -= 1
            start += 1

        if subarray_sum == target:
            min_length = min(min_length, count)

    return min_length if min_length != float('inf') else 0


def longest_substring_with_at_most_k_distinct_characters(string, k):
    """
    Problem: Longest Substring with At Most K Distinct Characters

    Given a string, find the length of the longest substring that contains at most k distinct characters.

    For example:

    python

    string = "eceba"
    k = 2

    The longest substring with at most 2 distinct characters is "ece," so the expected output is 3.
    """
    # If we say at most k, then we have the potential of having diff chars < k
    # eg: if string = 'eeeeee' and k = 2
    # then longest = len(string)
    # so what will help is, we will first iterate thru the string
    # take the first char, store it in an dictionary or something.
    # take the next until k
    # and when we encounter any new character greater than take
    # then we restart our store set our longest = counter and then restart counter
    # we repeat till we found the longest.

    char_count = {}
    count = 0
    longest_substring = 0

    for c in string:
        if c in char_count:
            char_count[c] += 1
            count += 1
        else:
            if len(char_count) < k:
                char_count[c] = 1
                count += 1
            else:
                longest_substring = max(longest_substring, count)
                count = 1
                char_count = {c: 1}

    return max(longest_substring, count)


def find_all_anagrams_in_a_string(string, p):
    """
    Problem: Find All Anagrams in a String

    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

    An anagram of a string is another string with the same characters, possibly in a different order.
    The order of characters in an anagram is not significant.

    For example:

    python

    s = "cbaebabacd"
    p = "abc"

    The output should be [0, 6], as the substrings with starting indices 0 and 6 in s are anagrams of p
    ("cba" and "bac").
    """
    p_len = len(p)
    n = len(string)

    # Initialize list to hold indices
    indices_p = []

    # Store chars and their value count
    p_freq = {}
    for char in p:
        p_freq[char] = p_freq.get(char, 0) + 1

    # Iterate through the string and store their char count
    window_freq = {}
    for i in range(n):
        if i >= p_len:
            left_char = string[i - p_len]
            if window_freq[left_char] == 1:
                del window_freq[left_char]
            else:
                window_freq[left_char] -= 1

        char = string[i]
        window_freq[char] = window_freq.get(char, 0) + 1

        if window_freq == p_freq:
            indices_p.append(i - p_len + 1)

        # sub_string = string[i:i+p_len]

        # if sorted(sub_string) == sorted(p):
        #     indices_p.append(i)
    return indices_p


s = "cbaebabacd"
p = "abc"

print(find_all_anagrams_in_a_string(s, p))


def fraudulent_activity_notfification(expenditure, d):
    n = len(expenditure)
    notifications = 0
    # Count and store
    expense_freq = {}

    def get_meadian():
        days = d
        elem1 = days // 2
        elem2 = elem1 + 1 if days % 2 == 0 else 0
        # if days % 2 == 0:
        #     elem2 = elem1 + 1

        for j, e in enumerate(sorted(expense_freq)):
            pass
            # if j = elem1:
            #     median

    for i in range(n):
        median = 0
        if i >= d:
            median = get_meadian()

            # Update the window slide
            left_day = i - d
            if expense_freq[left_day] == 1:
                del expense_freq[left_day]
            else:
                expense_freq[left_day] -= 1

        expense = expenditure[i]
        expense_freq[expense] = expense_freq.get(expense, 0) + 1

        if expense == median * 2:
            notifications += 1

    return notifications


expenditure = [10, 20, 30, 40, 50]
d = 3
print(fraudulent_activity_notfification(expenditure, d))
