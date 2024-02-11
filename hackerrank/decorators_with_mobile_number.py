"""
Let's dive into decorators! You are given

mobile numbers. Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx


The given mobile numbers may have +91, 91  or 0 written before the actual 10 digit number. Alternatively,
there may not be any prefix at all.

Input Format

The first line of input contains an integer N, the number of mobile phone numbers.

lines follow each containing a mobile number.

Output Format

Print

mobile numbers on separate lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230

Concept

Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators,
which are an invaluable asset. You can learn about decorators in 12 easy steps here.
To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in
ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.
"""


def wrapper(f):
    def fun(l):
        # complete the function
        refactored_lines = []
        for line in l:
            length = line(l)

            if length == 10:
                refactored_lines.append(f'+91 {line[0:5]} {line[5:]}')
            elif length == 11 and line[0] == '0':
                refactored_lines.append(f'+91 {line[1:6]} {line[6:]}')
            elif length == 12:
                refactored_lines.append(f'+91 {line[2:7]} {line[7:]}')
            elif length == 13:
                refactored_lines.append(f'+91 {line[3:8]} {line[8:]}')

        # or efficient way will be
        #     match = re.match(r'^(0|91|\+91)?(\d{5})(\d{5})$', line)
        #     if match:
        #         refactored_lines.append(f'+91 {match.group(2)} {match.group(3)}')

        refactored_lines = sorted(refactored_lines)
        print("\n".join(refactored_lines))

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


