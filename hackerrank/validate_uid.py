"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

*  It must contain at least 2 uppercase English alphabet characters.
* It must contain at least 3 digits
* It should only contain alphanumeric characters
* No character should repeat.
* There must be exactly 10 characters in a valid UID.

Input Format

The first line contains an integer
, the number of test cases.
The next

lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines.
Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354

Sample Output

Invalid
Valid

Explanation

B1CD102354:
is repeating → Invalid
B1CDEF2354: Valid
"""

import re


def is_valid(emp_uid):
    """
    ^: Asserts the start of the string.

    (?!.*(.).*\1): This is a negative lookahead assertion. It ensures that no character repeats. (?! ... )
    is a way of saying "assert that what follows is not this pattern".

    (?=(?:.*[A-Z]){2,}): This is a positive lookahead assertion. It ensures that there are at least 2 uppercase
    English alphabet characters. (?: ... ) is a non-capturing group, and {2,} specifies that there should be at
    least 2 occurrences.

    (?=(?:.*\\d){3,}): This is another positive lookahead assertion. It ensures that there are at least 3 digits.

    [A-Za-z0-9]{10}: This part specifies that the UID should consist of exactly 10 alphanumeric characters. [A-Za-z0-9]
    includes both uppercase and lowercase English alphabet characters, as well as digits.

    $: Asserts the end of the string.
    """
    pattern = r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})[A-Za-z0-9]{10}$'
    return re.match(pattern, emp_uid)


for _ in range(int(input())):
    employee_uid = input()

    if is_valid(employee_uid):
        print("Valid")
    else:
        print("Invalid")
