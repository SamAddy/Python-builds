"""
Questions Marks
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters,
and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
If so, then your program should return the string true, otherwise it should return the string false. If there aren't
any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question
marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true 
"""


def questions_marks(strparam):
    count = 0
    prev_num = 0
    start_counter = False
    passed = False
    # Iterate through the characters in teh param
    for ch in range(len(strparam)):
        # Check if the character is a number
        if strparam[ch].isnumeric():
            # If the number + prev num = 10 then passed = True
            if prev_num + int(strparam[ch]) == 10 and count == 3:
                passed = True
            # We start counter and check if prev num + ch = 10 and count is not eq to 3 then return false
            if start_counter and prev_num + int(strparam[ch]) == 10 and count != 3:
                return "false"
            prev_num = int(strparam[ch])
            count = 0
            start_counter = True
        # while counter is true if ch = "?" the increase counter by 1
        elif start_counter and strparam[ch] == "?":
            count += 1

    return "true" if passed else "false"


print(questions_marks("aa6?9"))  # false
print(questions_marks("arrb6???4xxb|5???eee5"))  # true
print(questions_marks("9???1???9??1???9"))  # false
print(questions_marks("5??aaaaaaaaaaaaaaaaaaa?5?5"))  # false
