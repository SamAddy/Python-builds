
'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

    Mat size must be

X. ( is an odd natural number, and is times

    .)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format

A single line containing the space separated values of
and

.

Constraints

Output Format

Output the design pattern.
'''


def print_door_mat(rows, cols):
    for i in range(1, rows, 2):
        pattern = (".|." * i).center(cols, "-")
        print(pattern)

    welcome_line = "WELCOME".center(cols, "-")
    print(welcome_line)

    for i in range(rows-2, 0, -2):
        pattern = (".|." * i).center(cols, "-")
        print(pattern)


if __name__ == "__main__":
    n, m = map(int, input().split())
    print_door_mat(n, m)
